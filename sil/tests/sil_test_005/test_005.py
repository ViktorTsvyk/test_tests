#import pytest
from .tenv import TEnv
from lib.lib import load_images, verify_image

from devsure.rpc.test.rpc_to_bpm_emu.tools import PinState
from devsure.time_simulator import SimulatedTimeScope, SimulatedThread
from devsure.formal import Step

def test_measurement_cancel(tenv: TEnv) -> None:
    print("5 TEST STARTED!!!!! ==============================================================")
    images = load_images()

    with SimulatedTimeScope(f"Test Case"):
        with Step("Wait 100 ms for the device to initialize"):
            SimulatedThread.sleep_ms(100)

        assert verify_image(tenv.emulator.screen_image, images.Home), "Home screen is shown"

        with Step("Start measurement"):
            tenv.emulator.click_button(PinState.ButtonOk)
            assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)

            tenv.emulator.click_button(PinState.ButtonOk)
            assert verify_image(tenv.emulator.screen_image, images.Measurement)

            tenv.emulator.click_button(PinState.ButtonDown)
            assert verify_image(tenv.emulator.screen_image, images.Measurement_Start)

            tenv.emulator.click_button(PinState.ButtonOk)
            assert verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)

        with Step("Wait 3 sec"):
            SimulatedThread.sleep_ms(3000)

        # it should still be pumping
        assert verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)
        assert tenv.emulator.is_pumping == True, "Pumping is on"
        assert tenv.emulator.is_valve_open == False

        with Step("Cancel measurement"):
            tenv.emulator.click_button(PinState.ButtonOk)

        assert verify_image(tenv.emulator.screen_image, images.Measurement_Canceled, images.mask_measurement_canceled)
        assert tenv.emulator.is_pumping == False
        assert tenv.emulator.is_valve_open == True

        # restart and cancel later, when pump is already off
        with Step("Restart the measurement"):
            tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)

        with Step("Wait 25 sec"):
            SimulatedThread.sleep_ms(25000)

        # it should not be pumping
        assert verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)
        assert tenv.emulator.is_pumping == False
        assert tenv.emulator.is_valve_open == False

        with Step("Cancel measurement"):
            tenv.emulator.click_button(PinState.ButtonOk)

        assert verify_image(tenv.emulator.screen_image, images.Measurement_Canceled, images.mask_measurement_canceled)
        assert tenv.emulator.is_pumping == False
        assert tenv.emulator.is_valve_open == True

    print("1 TEST STARTED!!!!! ==============================================================")
