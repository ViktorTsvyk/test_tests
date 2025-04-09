#import pytest
from .tenv import TEnv
from lib.lib import load_images, verify_image

from devsure.rpc.test.rpc_to_bpm_emu.tools import PinState
from devsure.time_simulator import SimulatedTimeScope, SimulatedThread
from devsure.formal import Step

def test_measurement_nominal(tenv: TEnv) -> None:
    print("3 TEST STARTED!!!!! ==============================================================")

    images = load_images()

    with SimulatedTimeScope(f"Test Case"):
        with Step("Wait 100 ms for the device to initialize"):
            SimulatedThread.sleep_ms(100)

        assert verify_image(tenv.emulator.screen_image, images.Home)

        tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Measurement)

        tenv.emulator.click_button(PinState.ButtonDown)
        assert verify_image(tenv.emulator.screen_image, images.Measurement_Start)

        tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)

        assert tenv.emulator.is_pumping == True
        assert tenv.emulator.is_valve_open == False

        SimulatedThread.sleep_ms(20000)
        assert verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)

        assert tenv.emulator.is_pumping == False
        assert tenv.emulator.is_valve_open == False

        SimulatedThread.sleep_ms(50000)
        assert verify_image(tenv.emulator.screen_image, images.Measurement_Complete)

        assert tenv.emulator.is_pumping == False
        assert tenv.emulator.is_valve_open == True

    print("3 TEST ENDED !!!!! ==============================================================")

