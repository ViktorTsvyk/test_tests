""" Describe PRC interface for the Emulator """

import os

from devsure.test_base.test_case_base import TestCaseBase
from devsure.time_simulator.simulation import simulated_sleep_ms

from .tenv import TEnv
from devsure.rpc.test.rpc_to_bpm_emu.bpm_emulator_rpc import PinState


class TestConnectionEstablished(TestCaseBase):
    tenv: TEnv

    def test_emulator_loaded(self):
        simulated_sleep_ms(200)  # let display bytes to arrive for sure

        remember_display_refreshes = self.tenv.emulator.display_refreshes
        self.assertGreater(
            remember_display_refreshes, 0, msg="There shall be display refreshes since start"
        )

        simulated_sleep_ms(1000)

        new_refreshes = self.tenv.emulator.display_refreshes
        self.assertEqual(
            new_refreshes, remember_display_refreshes,
            msg="There shall be no display refreshes while no buttons were pressed"
        )

        self.tenv.emulator.click_pin(PinState.ButtonOk)
        new_refreshes = self.tenv.emulator.display_refreshes
        print(f"new_refreshes={new_refreshes}, remember_display_refreshes={remember_display_refreshes}")
        self.assertGreater(
            new_refreshes, remember_display_refreshes,
            msg="There shall be display refreshes after ButtonOk"
        )
        remember_display_refreshes = new_refreshes

        # Where to store captured images
        report_folder = os.environ["DEVSURE_REPORT_FOLDER"]

        for i in range(10):
            print(f"\n ------------------\n Pressing button BUTTON1 {i+1} of 10")
            self.tenv.emulator.click_pin(PinState.ButtonDown)

            # Save captured image
            save_at = f"{report_folder}/Image{i}.png"
            print(f"!!!!!!!!!!!!!!! Saving image to {save_at}")
            self.tenv.emulator.screen_image.save(save_at)

            new_refreshes = self.tenv.emulator.display_refreshes
            print(f"new_refreshes={new_refreshes}, remember_display_refreshes={remember_display_refreshes}")
            self.assertGreater(
                new_refreshes, remember_display_refreshes,
                msg="There shall be display refreshes while buttons were pressed"
            )
            remember_display_refreshes = new_refreshes
            simulated_sleep_ms(1000)
