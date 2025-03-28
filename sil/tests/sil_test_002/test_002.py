#import pytest
from .tenv import TEnv
from lib.lib import load_images, verify_image

from devsure.rpc.test.rpc_to_bpm_emu.tools import PinState
from devsure.time_simulator import SimulatedTimeScope, SimulatedThread

def test_keypad_debounce(tenv: TEnv) -> None:
    images = load_images()

    nominal_duration_ms = 40
    duration_delta_ms = 5

    with SimulatedTimeScope(f"Test Case"):
        SimulatedThread.sleep_ms(100)
        #_capture_screen(tenv) # home
        verify_image(tenv.emulator.screen_image, images.Home)

        # 1 - pressing duration

        # 1.1 - negative
        tenv.emulator.set_pin(PinState.ButtonOk)
        SimulatedThread.sleep_ms(nominal_duration_ms - duration_delta_ms)
        tenv.emulator.clear_pin(PinState.ButtonOk)
        SimulatedThread.sleep_ms(200)
        verify_image(tenv.emulator.screen_image, images.Home)

        # 1.2 - positive
        tenv.emulator.set_pin(PinState.ButtonOk)
        SimulatedThread.sleep_ms(nominal_duration_ms + duration_delta_ms)
        tenv.emulator.clear_pin(PinState.ButtonOk)
        SimulatedThread.sleep_ms(200)
        verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)

        # 2 - releasing duration
        # strategy: will unpress for a short time and compare between 1 and 2 keypresses

        # 2.1 - negative
        tenv.emulator.set_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(200)

        tenv.emulator.clear_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(nominal_duration_ms - duration_delta_ms)
        tenv.emulator.set_pin(PinState.ButtonDown)

        SimulatedThread.sleep_ms(200)
        tenv.emulator.clear_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(200)

        # 1 click should be accepted
        verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        # return back
        tenv.emulator.click_button(PinState.ButtonUp)
        verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)

        # 2.2 - positive
        tenv.emulator.set_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(200)

        tenv.emulator.clear_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(nominal_duration_ms + duration_delta_ms)
        tenv.emulator.set_pin(PinState.ButtonDown)

        SimulatedThread.sleep_ms(200)
        tenv.emulator.clear_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(200)

        # 2 clicks should be accepted
        verify_image(tenv.emulator.screen_image, images.Menu_3_Visit, images.mask_time)

