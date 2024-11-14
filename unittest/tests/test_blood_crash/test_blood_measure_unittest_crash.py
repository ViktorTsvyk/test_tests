""" Test that causes crash - Fatal Python error: Segmentation fault"""

import unittest
import ctypes
import random
import time
from devsure.test_base.test_case_base import TestCaseBase
from .tenv import TEnv


# ---------------------------------------------
def rand_pause():
    pause_sec = random.randint(3, 6)
    time.sleep(pause_sec)

# ______________________________________________

class TestOurModel(TestCaseBase):
    def setUp(self) -> None:
        self.log.debug("Set up testing environment...")
        self.tenv = TEnv()
        rand_pause()
        self.log.debug(
            f"Testing the pressure inside the cuff with the target pressure:"
            f" {self.tenv.blood_pressure_md.target_pressure}"
        )

    def tearDown(self) -> None:
        self.log.debug("Tear down testing environment...")
        self.tenv.tear_down()

    def test_pressure_in_cuff_greater_then_additional(self):
        self.log.debug("First test started...")
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure in cuff is {pressure_in_cuff}")
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional}")
        self.assertGreater(pressure_in_cuff, additional)

    def test_crash_ctypes(self) -> None:
        self.log.debug("Second (crash) test started...")
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        result_pressure = self.tenv.pump.pressure.measurement
        rand_pause()
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.log.debug("........Reference to zero memory address........")
        rand_pause()
        self.log.debug("........Causes a segmentation fault through ctypes........")
        ctypes.string_at(0)
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_additional_pressure_present(self) -> None:
        self.log.debug("Third test started...")
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

if __name__ == "__main__":
    unittest.main()