import os
from time import sleep

import numpy as np
from pytest_bdd import given, when, then, parsers
from devsure.rpc.test.rpc_to_bpm_emu.bpm_emulator_rpc import PinState
from devsure.time_simulator import SimulatedThread
from sil_tests_i.Core.assertions.Assertions import Assertions
from sil_tests_i.Core.context.context import Context
from sil_tests_i.Core.image_manager.image_manager import convert_np_array_to_img, convert_img_to_np_array, \
    get_text_center_coordinates, create_and_apply_mask, create_mask, apply_mask, is_text_present, get_text
from sil_tests_i.tenv import TEnv
from PIL import Image

from sil_tests_i.pageobjects.components.button.button import is_button_present, is_button_selected

MEASUREMENT_FINISHED = "Measurement is finished"
MEASUREMENT_ERROR_VALVE_OFF = "Pressure remains unchanged"
MEASUREMENT_STOPPED = "Measurement was stopped"
PRESSURE_CUFF_ABBR = "HG"


@given("Start bpm emulator rpc")
def start_bpm_emulator_rpc(context: Context, tenv_func: TEnv):
    context.tenv = tenv_func
    wait_until_screen_loaded(context)


@then(parsers.cfparse("Verify button {button_name} is selected"))
def verify_is_button_selected(context: Context, button_name):
    Assertions.assert_true(is_button_selected(context.tenv.emulator.screen_image, button_name))


@when(parsers.cfparse("Click button {button}"))
def click_button(context: Context, button):
    context.tenv.emulator.click_pin(get_pin_state(button))


@when(parsers.cfparse("Press button {button}"))
def press_button(context: Context, button):
    context.tenv.emulator.set_pin(get_pin_state(button))


@when(parsers.cfparse("Release button {button}"))
def release_button(context: Context, button):
    context.tenv.emulator.clear_pin(get_pin_state(button))


@when(parsers.cfparse("Device waiting {time} milliseconds"))
def device_waiting(context: Context, time):
    SimulatedThread.sleep_ms(int(time))


@then("Verify current screen image is equal provided one, ignoring the timestamp section")
def verify_screen_image_equal_provided(context):
    feature_dir = os.path.dirname(os.path.abspath(context.feature.filename))
    image_full_path = os.path.join(feature_dir, context.table[0]["Image"])

    expected_image = Image.open(image_full_path)
    expected_image_np_array = convert_img_to_np_array(expected_image)
    expected_image_np_array = apply_mask_ignore_timestamp(context, expected_image_np_array)
    expected_img_png = convert_np_array_to_img(expected_image_np_array)

    actual_image = context.tenv.emulator.screen_image
    actual_image_np_array = convert_img_to_np_array(actual_image)
    actual_image_np_array = apply_mask_ignore_timestamp(context, actual_image_np_array)
    actual_img_png = convert_np_array_to_img(actual_image_np_array)

    is_images_array_equal = np.array_equiv(expected_image_np_array, actual_image_np_array)
    Assertions.assert_true(is_images_array_equal, "Image comparison failed")


@then(parsers.cfparse("Verify screen contains button {button_name}"))
def screen_contains_button(context, button_name):
    is_present = is_button_present(context.tenv.emulator.screen_image, button_name)
    Assertions.assert_true(is_present)


@then(parsers.cfparse("Verify screen contains text {text}"))
def verify_screen_contains_text(context, text):
    is_present = is_text_present(context.tenv.emulator.screen_image, text)
    Assertions.assert_true(is_present)


@then(("Wait until perform measurement finished"))
def wait_until_perform_measurement_is_finished(context):
    measurement_waiting_time = 100000  # millisecond
    interval = 10000  # millisecond
    waited_time = 0  # millisecond
    while waited_time <= measurement_waiting_time:
        SimulatedThread.sleep_ms(int(interval))
        waited_time += interval
        screen_image = context.tenv.emulator.screen_image
        is_finished = is_text_present(screen_image, MEASUREMENT_FINISHED)
        is_error = is_text_present(screen_image, "ERROR")
        if (is_finished or is_error):
            break

@then("Verify pressure in the cuff displaying")
def step_temp_verify_pressure_cuff_displaying(context):
    screen_data = get_text(context.tenv.emulator.screen_image)
    actual_hg_value = None
    for value in screen_data:
        normalized_value = value.replace(" ", "").lower()
        if PRESSURE_CUFF_ABBR.lower() in normalized_value:
            try:
                hg_value = normalized_value.split(":")[-1]
                actual_hg_value = int(hg_value)
            except (ValueError, IndexError):
                actual_hg_value = None
    Assertions.assert_true(
        actual_hg_value is not None and 0 <= actual_hg_value <= 300,
        f"Pressure value is invalid or out of range: {actual_hg_value}"
    )

@then(parsers.cfparse(
    "Verify measurement result: SYS equal to {expected_sys_value:d}, DIA equal to {expected_dia_value:d}; With deviation uf {deviation:d} units"))
def verify_measurement_result(context: Context, expected_sys_value, expected_dia_value, deviation):
    screen_data = get_text(context.tenv.emulator.screen_image)
    actual_sys_value = None
    actual_dia_value = None
    for i, value in enumerate(screen_data):
        if "SYS" in value and i + 1 < len(screen_data):
            next_value = screen_data[i + 1]
            try:
                actual_sys_value = int(next_value)
            except ValueError:
                actual_sys_value = None

    for i, value in enumerate(screen_data):
        if "DIA" in value and i + 1 < len(screen_data):
            next_value = screen_data[i + 1]
            try:
                actual_dia_value = int(next_value)
            except ValueError:
                actual_dia_value = None

    Assertions.assert_true(expected_sys_value - deviation <= actual_sys_value <= expected_sys_value + deviation)
    Assertions.assert_true(expected_dia_value - deviation <= actual_dia_value <= expected_dia_value + deviation)


def apply_mask_four_menu_item(context, image):
    masked_image = create_and_apply_mask(image, context.tenv.emulator.SCREEN_H, context.tenv.emulator.SCREEN_W, 90, 390,
                                         260, 310, True)
    return masked_image


def apply_mask_ignore_header(context, image):
    masked_image = create_and_apply_mask(image, context.tenv.emulator.SCREEN_H, context.tenv.emulator.SCREEN_W, 0, 480,
                                         0, 25)
    return masked_image


def apply_mask_ignore_timestamp(context, image):
    mask_ignore_timestamp = create_mask(context.tenv.emulator.SCREEN_H, context.tenv.emulator.SCREEN_W, 200, 275, 0, 25)
    masked_image = apply_mask(image, mask_ignore_timestamp)
    return masked_image


def wait_until_screen_loaded(context, waiting_time=20):
    for i in range(waiting_time):
        if context.tenv.emulator.screen_image is None:
            sleep(1)


def get_pin_state(button: str):
    button_map = {
        "ok": PinState.ButtonOk,
        "down": PinState.ButtonDown,
        "up": PinState.ButtonUp,
    }
    return button_map.get(button.lower())
