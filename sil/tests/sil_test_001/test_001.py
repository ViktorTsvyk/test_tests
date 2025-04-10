#import pytest
import time

from .tenv import TEnv
from lib.lib import load_images, verify_image

from devsure.rpc.test.rpc_to_bpm_emu.tools import PinState
from devsure.time_simulator import SimulatedTimeScope, SimulatedThread
from devsure.formal import Step

def test_navigation(tenv: TEnv) -> None:
    print("1 TEST STARTED!!!!! ==============================================================")

    images = load_images()

    with SimulatedTimeScope(f"Test Case"):
        with Step("Wait 100 ms for the device to initialize"):
            SimulatedThread.sleep_ms(100)

        assert verify_image(tenv.emulator.screen_image, images.Home)

        with Step("Click Ok button to enter Menu screen"):
            tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        with Step("Click Ok button to enter Measurement screen"):
            tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Measurement)

        with Step("Click Ok button to exit back to Menu screen"):
            tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        with Step("Click Down button to move focus to History option"):
            tenv.emulator.click_button(PinState.ButtonDown)
        assert verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        with Step("Click Ok button to enter History screen"):
            tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.History)

        with Step("Click Ok button to exit back to Menu screen"):
            tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        with Step("Click Down button to move focus to History option"):
            tenv.emulator.click_button(PinState.ButtonDown)
        assert verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        with Step("Click Down button to move focus to Visit Site option"):
            tenv.emulator.click_button(PinState.ButtonDown)
        assert verify_image(tenv.emulator.screen_image, images.Menu_3_Visit, images.mask_time)

        with Step("Click Ok button to enter Visit Site screen"):
            tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Visit)

        with Step("Click Ok button to exit back to Menu screen"):
            tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)


        with Step("Click Down button to move focus to History option"):
            tenv.emulator.click_button(PinState.ButtonDown)
        assert verify_image(tenv.emulator.screen_image, images.Menu_2_History, images.mask_time)

        with Step("Click Down button to move focus to Visit Site option"):
            tenv.emulator.click_button(PinState.ButtonDown)
        assert verify_image(tenv.emulator.screen_image, images.Menu_3_Visit, images.mask_time)

        with Step("Click Down button to move focus to Exit option"):
            tenv.emulator.click_button(PinState.ButtonDown)
        assert verify_image(tenv.emulator.screen_image, images.Menu_4_Exit, images.mask_time)

        with Step("Click Ok button to exit back to Home screen"):
            tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Home)

    print("1 TEST ENDED!!!!! ==============================================================")
