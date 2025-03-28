#import pytest
from .tenv import TEnv
from lib.lib import load_images, verify_image

from devsure.rpc.test.rpc_to_bpm_emu.tools import PinState
from devsure.time_simulator import SimulatedTimeScope, SimulatedThread

def test_measurement_cancel(tenv: TEnv) -> None:
    images = load_images()

    with SimulatedTimeScope(f"Test Case"):
        SimulatedThread.sleep_ms(100)
        verify_image(tenv.emulator.screen_image, images.Home)

        tenv.emulator.click_button(PinState.ButtonOk)
        verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonOk)
        verify_image(tenv.emulator.screen_image, images.Measurement)

        tenv.emulator.click_button(PinState.ButtonDown)
        verify_image(tenv.emulator.screen_image, images.Measurement_Start)

        tenv.emulator.click_button(PinState.ButtonOk)
        verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)

        SimulatedThread.sleep_ms(3000)

        # it should still be pumping
        verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)
        #assert tenv.emulator.is_pump_enabled == True
        #assert tenv.emulator.is_valve_enabled == False

        tenv.emulator.click_button(PinState.ButtonOk)
        verify_image(tenv.emulator.screen_image, images.Measurement_Canceled, images.mask_measurement_canceled)

        # restart and cancel later, when pump is already off

        tenv.emulator.click_button(PinState.ButtonOk)
        verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)

        SimulatedThread.sleep_ms(25000)

        # it should not be pumping
        verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)
        #assert tenv.emulator.is_pump_enabled == False
        #assert tenv.emulator.is_valve_enabled == False

        tenv.emulator.click_button(PinState.ButtonOk)
        verify_image(tenv.emulator.screen_image, images.Measurement_Canceled, images.mask_measurement_canceled)



