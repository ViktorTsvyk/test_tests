#import pytest
from .tenv import TEnv
from lib.lib import load_images, verify_image

from devsure.rpc.test.rpc_to_bpm_emu.tools import PinState
from devsure.time_simulator import SimulatedTimeScopeDebug, SimulatedThread


import threading


def test_keypad_debounce(tenv_func: TEnv) -> None:
    tenv = tenv_func
    print("2 TEST STARTED!!!!! ==============================================================")
    thread_id = threading.current_thread().ident
    print(f"!!!!!! test_keypad_debounce Current thread ID: {thread_id}")

    print("2 load_images before ==============================================================")

    images = load_images()

    print("2 load_images after ==============================================================")

    nominal_duration_ms = 40
    duration_delta_ms = 5

    with SimulatedTimeScopeDebug(f"Test Case"):
        print("Before simulated sleep =================================================")
        SimulatedThread.sleep_ms(100)
        #_capture_screen(tenv) # home
        verify_image(tenv.emulator.screen_image, images.Home)

        print("2### 1 ==============================================================")
        # 1 - pressing duration

        print("2### 1.1 ==============================================================")
        # 1.1 - negative
        tenv.emulator.set_pin(PinState.ButtonOk)
        SimulatedThread.sleep_ms(nominal_duration_ms - duration_delta_ms)
        tenv.emulator.clear_pin(PinState.ButtonOk)
        SimulatedThread.sleep_ms(200)
        verify_image(tenv.emulator.screen_image, images.Home)

        print("2### 1.2 ==============================================================")
        # 1.2 - positive
        tenv.emulator.set_pin(PinState.ButtonOk)
        SimulatedThread.sleep_ms(nominal_duration_ms + duration_delta_ms)
        tenv.emulator.clear_pin(PinState.ButtonOk)
        SimulatedThread.sleep_ms(200)
        verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)

        print("2### 2 ==============================================================")
        # 2 - releasing duration
        # strategy: will unpress for a short time and compare between 1 and 2 keypresses

        print("2### 2.1 ==============================================================")
        # 2.1 - negative
        tenv.emulator.set_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(200)

        tenv.emulator.clear_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(nominal_duration_ms - duration_delta_ms)
        tenv.emulator.set_pin(PinState.ButtonDown)

        SimulatedThread.sleep_ms(200)
        tenv.emulator.clear_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(200)

        print("click should be accepted ==============================================================")
        # 1 click should be accepted
        verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        # return back
        tenv.emulator.click_button(PinState.ButtonUp)
        verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)

        print("2### 2.2 ==============================================================")
        # 2.2 - positive
        tenv.emulator.set_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(200)

        tenv.emulator.clear_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(nominal_duration_ms + duration_delta_ms)
        tenv.emulator.set_pin(PinState.ButtonDown)

        SimulatedThread.sleep_ms(200)
        tenv.emulator.clear_pin(PinState.ButtonDown)
        SimulatedThread.sleep_ms(200)

        print("2### clicks should be accepted ==============================================================")
        # 2 clicks should be accepted
        verify_image(tenv.emulator.screen_image, images.Menu_3_Visit, images.mask_time)

    print("2 TEST ENDED!!!!! ==============================================================")
