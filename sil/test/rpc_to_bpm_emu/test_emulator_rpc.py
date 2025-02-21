""" Describe PRC interface for the Emulator """

import unittest
import time
import os
from typing import Final

from .tenv import TEnv
from devsure.rpc.test.rpc_to_bpm_emu.bpm_emulator_rpc import PinState

# Where to store captured images
DEVSURE_REPORT_FOLDER: Final[str] = os.environ.get(
    "DEVSURE_REPORT_FOLDER",
    os.getcwd()  # TODO: DEVSURE_REPORT_FOLDER shall always be present
)


class TestConnectionEstablished(unittest.TestCase):
    def setUp(self) -> None:
        """ Start Emulator """
        self.tenv = TEnv()
        self.start_emulation_status = self.tenv.emulator.emulator_start_emulation()

    def tearDown(self):
        """ Shut down Emulator """
        try:
            # TODO: also to move this to common fixture))
            self.tenv.emulator.mark_for_exit()
            self.tenv.emulator.emulator_stop_emulation()
            time.sleep(2)
        except Exception as e:
            print(f"tearDown exception {e}")

    def test_emulator_loaded(self):
        self.assertEqual(
            0, self.start_emulation_status,
            msg="Emulator shall start normally"
        )
        self.assertEqual(
            0, self.start_emulation_status,
            msg="Other API provided by the emulator shall work as well"
        )

        time.sleep(1.5)  # let display bytes to arrive for sure
        self.assertGreater(
            self.tenv.emulator.display_refreshes, 0,
            msg="There shall be display refreshes since start"
        )

        remember_display_refreshes = self.tenv.emulator.display_refreshes
        self.assertGreater(
            remember_display_refreshes, 0
        )

        time.sleep(1)

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

        for i in range(10):
            print(f"\n ------------------\n Pressing button BUTTON1 {i+1} of 10")
            self.tenv.emulator.click_pin(PinState.ButtonDown)

            # Save captured image
            save_at = f"{DEVSURE_REPORT_FOLDER}/Image{i}.png"
            print(f"!!!!!!!!!!!!!!! Saving image to {save_at}")
            self.tenv.emulator.screen_image.save(save_at)

            new_refreshes = self.tenv.emulator.display_refreshes
            print(f"new_refreshes={new_refreshes}, remember_display_refreshes={remember_display_refreshes}")
            self.assertGreater(
                new_refreshes, remember_display_refreshes,
                msg="There shall be display refreshes while buttons were pressed"
            )
            remember_display_refreshes = new_refreshes
            time.sleep(1)
