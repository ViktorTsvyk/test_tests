""" Test that causes crash - Fatal Python error: Segmentation fault"""

import unittest
import ctypes
import random
import time
import logging
from devsure.test_base.test_case_base import TestCaseBase
from .tenv import TEnv


# ---------------------------------------------
def rand_pause():
    pause_sec = random.randint(3, 6)
    time.sleep(pause_sec)

# ______________________________________________

class TestOurModel(TestCaseBase):
    tenv: TEnv

    def setUp(self) -> None:
        super().setUp()
        rand_pause()
        logging.debug(
            f"Testing the pressure inside the cuff with the target pressure:"
            f" {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_pressure_in_cuff_greater_then_additional(self):
        logging.debug("First test started...")
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure in cuff is {pressure_in_cuff}")
        rand_pause()
        additional = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional}")
        self.assertGreater(pressure_in_cuff, additional)

    def test_crash_ctypes(self) -> None:
        logging.debug("Second (crash) test started...")
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        result_pressure = self.tenv.pump.pressure.measurement
        rand_pause()
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        logging.debug("........Reference to zero memory address........")
        rand_pause()
        logging.debug("........Causes a segmentation fault through ctypes........")
        ctypes.string_at(0)
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_additional_pressure_present(self) -> None:
        logging.debug("Third test started...")
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

if __name__ == "__main__":
    unittest.main()
