#import pytest
from .tenv import TEnv
from lib.lib import load_images, verify_image

from devsure.rpc.test.rpc_to_bpm_emu.tools import PinState
from devsure.time_simulator import SimulatedTimeScope, SimulatedThread

def test_measurement_nominal(tenv: TEnv) -> None:
    print("4 TEST STARTED!!!!! ==============================================================")
    images = load_images()

    with SimulatedTimeScope(f"Test Case"):
        SimulatedThread.sleep_ms(100)
        assert verify_image(tenv.emulator.screen_image, images.Home)

        tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Menu_1_Measurement, images.mask_time)

        tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Measurement)

        tenv.emulator.click_button(PinState.ButtonDown)
        assert verify_image(tenv.emulator.screen_image, images.Measurement_Start)

        tenv.emulator._hand_simulator.break_pump(True)

        tenv.emulator.click_button(PinState.ButtonOk)
        assert verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)

        #assert tenv.emulator.is_pump_enabled == True
        #assert tenv.emulator.is_valve_enabled == False

        SimulatedThread.sleep_ms(10000)
        # # it should still be pumping
        # assert verify_image(tenv.emulator.screen_image, images.Measurement_InProgress, images.mask_measurement_progress)
        # #assert tenv.emulator.is_pump_enabled == True
        # #assert tenv.emulator.is_valve_enabled == False

        # SimulatedThread.sleep_ms(50000)
        assert verify_image(tenv.emulator.screen_image, images.Error_PreasureRemainsUnchanged)

        #assert tenv.emulator.is_pump_enabled == False
        #assert tenv.emulator.is_valve_enabled == True

    print("4 TEST STARTED!!!!! ==============================================================")
