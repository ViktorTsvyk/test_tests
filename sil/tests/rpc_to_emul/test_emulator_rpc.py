""" Describe PRC interface for the Emulator """

import unittest
from .tenv import TEnv


class TestConnectionEstablished(unittest.TestCase):
    def setUp(self) -> None:
        self.tenv = TEnv()

    def test_emulator_loaded(self):
        self.tenv.emulator.cpp_api1()  # This will raise an exception if the emulator is not loaded
        self.assertIsNotNone(self.tenv.emulator)
        cpp_res = self.tenv.emulator.cpp_api2(b"A");
        self.assertEqual(
            ord('A') + 1,
            cpp_res
        )

    def test_emulator_api3(self):
        cpp_res = self.tenv.emulator.cpp_api3()
        self.assertEqual(
            42,
            cpp_res
        )
