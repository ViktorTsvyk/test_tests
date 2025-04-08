#import pytest
import time

from .tenv import TEnv
from lib.lib import load_images, verify_image

from devsure.rpc.test.rpc_to_bpm_emu.tools import PinState
from devsure.time_simulator import SimulatedTimeScope, SimulatedThread

def test_navigation(tenv: TEnv) -> None:
    print("1 TEST STARTED!!!!! ==============================================================")

    images = load_images()

    with SimulatedTimeScope(f"Test Case"):
        SimulatedThread.sleep_ms(100)
        #_capture_screen(tenv) # home
        assert verify_image(tenv.emulator.screen_image, images.Home)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Menu.Measurement
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Measurement
        assert verify_image(tenv.emulator.screen_image, images.Measurement)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Menu.Measurement
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.History
        assert verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # History
        assert verify_image(tenv.emulator.screen_image, images.History)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Menu.Measurement
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.History
        assert verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.Visit
        assert verify_image(tenv.emulator.screen_image, images.Menu_3_Visit, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Visit
        assert verify_image(tenv.emulator.screen_image, images.Visit)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # Menu.Measurement
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.History
        assert verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.Visit
        assert verify_image(tenv.emulator.screen_image, images.Menu_3_Visit, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonDown)
        #_capture_screen(tenv) # Menu.Exit
        assert verify_image(tenv.emulator.screen_image, images.Menu_4_Exit, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonOk)
        #_capture_screen(tenv) # home
        assert verify_image(tenv.emulator.screen_image, images.Home)

    print("1 TEST ENDED!!!!! ==============================================================")
