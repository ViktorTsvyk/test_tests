import time
import os

from .tenv import TEnv
from devsure.rpc.test.rpc_to_bpm_emu.bpm_emulator_rpc import PinState, BpmEmulatorRpc


def test_emulator_loaded(tenv: TEnv):
    call_test(tenv)


def call_test(tenv: TEnv):
    emulator: BpmEmulatorRpc = tenv.emulator

    start_emulation_status = emulator.emulator_start_emulation()

    assert start_emulation_status == 0, "Emulator shall start normally"

    assert start_emulation_status == 0, "Other API provided by the emulator shall work as well"

    time.sleep(1.5)  # let display bytes to arrive for sure

    remember_display_refreshes = emulator.display_refreshes
    assert remember_display_refreshes > 0, "There shall be display refreshes since start"

    time.sleep(1)

    new_refreshes = emulator.display_refreshes
    assert new_refreshes == remember_display_refreshes, "There shall be no display refreshes while no buttons were pressed"

    emulator.click_pin(PinState.ButtonOk)
    new_refreshes = emulator.display_refreshes
    print(f"new_refreshes={new_refreshes}, remember_display_refreshes={remember_display_refreshes}")
    assert new_refreshes > remember_display_refreshes, "There shall be display refreshes after ButtonOk"
    remember_display_refreshes = new_refreshes

    # Where to store captured images
    report_folder = os.environ["DEVSURE_REPORT_FOLDER"]

    for i in range(10):
        print(f"\n ------------------\n Pressing button BUTTON1 {i+1} of 10")
        emulator.click_pin(PinState.ButtonDown)

        # Save captured image
        save_at = f"{report_folder}/Image{i}.png"
        print(f"!!!!!!!!!!!!!!! Saving image to {save_at}")
        emulator.screen_image.save(save_at)

        new_refreshes = emulator.display_refreshes
        print(f"new_refreshes={new_refreshes}, remember_display_refreshes={remember_display_refreshes}")
        assert new_refreshes > remember_display_refreshes, "There shall be display refreshes while buttons were pressed"
        remember_display_refreshes = new_refreshes
        time.sleep(1)
