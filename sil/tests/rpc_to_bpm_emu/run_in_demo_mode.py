""" Describe PRC interface for the Emulator """

import unittest
import time
from .tenv import TEnv


class TestConnectionEstablished(unittest.TestCase):
    def setUp(self) -> None:
        """ Start Emulator """
        self.tenv = TEnv()
        self.start_emulation_status = self.tenv.emulator.emulator_start_emulation()

    def tearDown(self):
        """ Shut down Emulator """
        try:
            # TODO: also to move this to common fixture))
            self.tenv.emulator.emulator_stop_emulation()
        except Exception as e:
            print(f"tearDown exception {e}")

    def test_emulator_loaded(self):
        self.assertEqual(0, self.start_emulation_status)
        self.assertEqual(0, self.start_emulation_status)
        print("\n\n\n_________________________________________________________________")
        print("#################################################################\n")
        input("USE GUI TO CONTROL EMULATOR\nPress Enter to end testing...\n\n\n")
        self.assertGreater(
            self.tenv.emulator.display_refreshes,
            0
        )

