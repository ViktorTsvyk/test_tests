""" Describe PRC interface for the Emulator """

import unittest
from .tenv import TEnv


class TestConnectionEstablished(unittest.TestCase):
    def setUp(self) -> None:
        """ Start Emulator """
        self.tenv = TEnv.setUpUnittest(self)

        self.start_emulation_statuses = (
            self.tenv.emulator.emulator_start_emulation(),
            self.tenv.emulator_second.emulator_start_emulation(),
        )

    def test_emulator_loaded(self):
        self.assertEqual(self.start_emulation_statuses, (0, 0), msg="Emulators shall start normally")
        print("\n\n\n_________________________________________________________________")
        print("#################################################################\n")
        input("USE GUI TO CONTROL EMULATOR\nPress Enter to end testing...\n\n\n")
        self.assertGreater(self.tenv.emulator.display_refreshes, 0)
        self.assertGreater(self.tenv.emulator_second.display_refreshes, 0)
