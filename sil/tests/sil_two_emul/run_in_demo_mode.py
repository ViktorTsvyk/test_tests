""" Describe PRC interface for the Emulator """

import unittest
from .tenv import TEnv


class TestConnectionEstablished(unittest.TestCase):
    def setUp(self) -> None:
        """ Start Emulator """
        self.tenv = TEnv.setUpUnittest(self)

    def test_emulator_loaded(self):
        print("\n\n\n_________________________________________________________________")
        print("#################################################################\n")
        input("USE GUI TO CONTROL EMULATOR\nPress Enter to end testing...\n\n\n")
        self.assertGreater(self.tenv.emulator.display_refreshes, 0)
        self.assertGreater(self.tenv.emulator_second.display_refreshes, 0)
