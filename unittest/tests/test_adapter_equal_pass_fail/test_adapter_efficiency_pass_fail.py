""" 38 tests fail, 38 tests pass """
import random
import unittest
import logging
from devsure.test_base.test_case_base import TestCaseBase
from .tenv import TEnv
import time
# ---------------------------------------
def rand_pause():
    pause_sec = random.randint(1, 4)
    time.sleep(pause_sec)

# ---------------------------------------

class TestOurModel(TestCaseBase):
    tenv: TEnv

    def setUp(self):
        super().setUp()

        logging.debug(
            f"Testing the pressure inside the cuff with the target pressure:"
            f" {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_power_adapter_efficiency_more(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertGreaterEqual(efficiency, 0.2)

    def test_power_adapter_efficiency_less(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertLess(efficiency, 0.2)

    def test_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_cuff_connection_initial_state(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_greater_then_add(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_add_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_press(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertNotEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_power_adapter_efficiency(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertGreaterEqual(efficiency, 0.2)

    def test_power_adapter_efficiency_is_less(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertLess(efficiency, 0.2)

    def test_additional_pressure_is_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure_value(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_msg(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_in_cuff_greater_then_additional_val(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_cuff_connection_initial_state_val(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_greater_then_addit(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_pump_add_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_pump_target_press(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertNotEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_devices_power_adapter_efficiency_more(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertGreaterEqual(efficiency, 0.2)

    def test_devices_power_adapter_efficiency_less(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertLess(efficiency, 0.2)

    def test_devices_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_devices_target_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_devices_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_devices_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_devices_cuff_connection_initial_state(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_devices_pressure_in_cuff_greater_then_add(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_devices_add_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_devices_target_press(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertNotEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_devices_power_adapter_efficiency(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertGreaterEqual(efficiency, 0.2)

    def test_devices_power_adapter_efficiency_is_less(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertLess(efficiency, 0.2)

    def test_devices_additional_pressure_is_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_devices_target_pressure_value(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_devices_cuff_connection_initial_msg(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_devices_pressure_in_cuff_greater_then_additional_val(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_devices_cuff_connection_initial_state_val(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_devices_pressure_in_cuff_greater_then_addit(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_devices_pump_add_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_devices_pump_target_press(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertNotEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_smoke_power_adapter_efficiency_more(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertGreaterEqual(efficiency, 0.2)

    def test_smoke_power_adapter_efficiency_less(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertLess(efficiency, 0.2)

    def test_smoke_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_smoke_target_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_smoke_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_smoke_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_smoke_cuff_connection_initial_state(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_smoke_pressure_in_cuff_greater_then_add(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_smoke_add_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_smoke_target_press(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertNotEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_smoke_power_adapter_efficiency(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertGreaterEqual(efficiency, 0.2)

    def test_smoke_power_adapter_efficiency_is_less(self):
        efficiency = self.tenv.power_adapter.efficiency
        rand_pause()
        # Expected efficiency is 80% or more
        self.assertLess(efficiency, 0.2)

    def test_smoke_additional_pressure_is_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_smoke_target_pressure_value(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_smoke_cuff_connection_initial_msg(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_smoke_pressure_in_cuff_greater_then_additional_val(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_smoke_cuff_connection_initial_state_val(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_smoke_pressure_in_cuff_greater_then_addit(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_smoke_pump_add_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_smoke_pump_target_press(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertNotEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_pump_target_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertNotEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_initial_cuff_connection(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_value_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_value_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_value_target_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertNotEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_for_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_val_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_exists(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_pressure_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_additional_pressure_value_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_value_info_target_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_info_msg(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_cuff_greater_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_additional_pressure_for_pump_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure_calculation(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        logging.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        logging.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_state_message(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"
if __name__ == "__main__":
    unittest.main()
