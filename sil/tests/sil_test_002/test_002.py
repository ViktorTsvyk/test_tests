#import pytest
from .tenv import TEnv
from lib.lib import load_images, verify_image

from devsure.rpc.test.rpc_to_bpm_emu.tools import PinState
from devsure.time_simulator import SimulatedTimeScope, SimulatedThread
from devsure.formal import Step


import threading


def test_keypad_debounce(tenv: TEnv) -> None:
    print("2 TEST STARTED!!!!! ==============================================================")

    images = load_images()

    nominal_duration_ms = 40
    duration_delta_ms = 5

    with SimulatedTimeScope(f"Test Case"):
        with Step("Wait 100 ms for the device to initialize"):
            SimulatedThread.sleep_ms(100)

        assert verify_image(tenv.emulator.screen_image, images.Home)

        print("2### 1 ==============================================================")
        # 1 - pressing duration

        print("2### 1.1 ==============================================================")
        # 1.1 - negative
        with Step("Click time below duration"):
            tenv.emulator.set_pin(PinState.ButtonOk)
            SimulatedThread.sleep_ms(nominal_duration_ms - duration_delta_ms)
            tenv.emulator.clear_pin(PinState.ButtonOk)
            SimulatedThread.sleep_ms(200)
        assert verify_image(tenv.emulator.screen_image, images.Home)

        print("2### 1.2 ==============================================================")
        # 1.2 - positive
        with Step("Click time above duration"):
            tenv.emulator.set_pin(PinState.ButtonOk)
            SimulatedThread.sleep_ms(nominal_duration_ms + duration_delta_ms)
            tenv.emulator.clear_pin(PinState.ButtonOk)
            SimulatedThread.sleep_ms(200)
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)

        print("2### 2 ==============================================================")
        # 2 - releasing duration
        # strategy: will unpress for a short time and compare between 1 and 2 keypresses

        print("2### 2.1 ==============================================================")
        # 2.1 - negative

        with Step("Hold a button"):
            tenv.emulator.set_pin(PinState.ButtonDown)
            SimulatedThread.sleep_ms(200)

        with Step("Release time below duration"):
            tenv.emulator.clear_pin(PinState.ButtonDown)
            SimulatedThread.sleep_ms(nominal_duration_ms - duration_delta_ms)
            tenv.emulator.set_pin(PinState.ButtonDown)

        with Step("Release a button"):
            SimulatedThread.sleep_ms(200)
            tenv.emulator.clear_pin(PinState.ButtonDown)
            SimulatedThread.sleep_ms(200)

        print("One click should be accepted ==============================================================")
        # 1 click should be accepted
        assert verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        # return back
        with Step("Return focus back"):
            tenv.emulator.click_button(PinState.ButtonUp)
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)

        print("2### 2.2 ==============================================================")
        # 2.2 - positive
        with Step("Hold a button"):
            tenv.emulator.set_pin(PinState.ButtonDown)
            SimulatedThread.sleep_ms(200)

        with Step("Release time above duration"):
            tenv.emulator.clear_pin(PinState.ButtonDown)
            SimulatedThread.sleep_ms(nominal_duration_ms + duration_delta_ms)
            tenv.emulator.set_pin(PinState.ButtonDown)

        with Step("Release a button"):
            SimulatedThread.sleep_ms(200)
            tenv.emulator.clear_pin(PinState.ButtonDown)
            SimulatedThread.sleep_ms(200)

        print("2### 2 clicks should be accepted ==============================================================")
        # 2 clicks should be accepted
        assert verify_image(tenv.emulator.screen_image, images.Menu_3_Visit, images.mask_time)

    print("2 TEST ENDED!!!!! ==============================================================")
