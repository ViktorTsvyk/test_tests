""" 92 TESTS PASS """

import unittest
from devsure.test_base.test_case_base import TestCaseBase
from .tenv import TEnv
import time
import random
import logging

# ---------------------------------------
def rand_pause():
    pause_sec = random.randint(0,2)
    time.sleep(pause_sec)
# ---------------------------------------

class TestOurModel(TestCaseBase):
    def setUp(self) -> None:
        logging.debug("The most basic demo for GL TAF using unittest available 'out of the box'")
        self.tenv = TEnv()

    def tearDown(self):
        self.tenv.tear_down()

    def test_power_source(self):
        logging.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            120.1
        )
        logging.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            5.1
        )

    def test_voltage(self):
        logging.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 122.0)

    def test_nominal_power(self):
        logging.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        logging.info("Check nominal power value...")
        rand_pause()
        logging.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 25.0])

    def test_current(self):
        logging.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 5.0)

    def test_heat_coefficient(self):
        logging.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        logging.info("Check heat coefficient value...")
        rand_pause()
        logging.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertNotIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_pressure_coefficient(self):
        logging.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.01)

    def test_power_is_connected(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNotNone(connected_power)

    def test_connected_power_is_motor(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        logging.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCMotor", connected_power)

    def test_pressure_class(self):
        logging.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        logging.info(f"Pressure: {vent_pressure}")
        self.assertTrue("class" in vent_pressure)

    def test_heat_not_int(self):
        logging.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertFalse(heat_coefficient.is_integer())

    def test_heat_real(self):
        logging.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        logging.info(f"Value is {heat_coefficient_real}")
        self.assertEqual(heat_coefficient_real, 0.5)

    def test_power_source_info(self):
        logging.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            120.1
        )
        logging.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            5.1
        )

    def test_voltage_value(self):
        logging.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 122.0)

    def test_nominal_power_value(self):
        logging.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        logging.info("Check nominal power value...")
        rand_pause()
        logging.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 25.0])

    def test_current_value(self):
        logging.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 5.0)

    def test_heat_coefficient_value(self):
        logging.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        logging.info("Check heat coefficient value...")
        rand_pause()
        logging.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertNotIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_pressure_coefficient_value(self):
        logging.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.01)

    def test_power_is_connected_to_ventilator(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNotNone(connected_power)

    def test_connected_power_is_motor_type(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        logging.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCMotor", connected_power)

    def test_pressure_class_info(self):
        logging.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        logging.info(f"Pressure: {vent_pressure}")
        self.assertTrue("class" in vent_pressure)

    def test_heat_not_int_type(self):
        logging.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertFalse(heat_coefficient.is_integer())

    def test_heat_real_value(self):
        logging.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        logging.info(f"Value is {heat_coefficient_real}")
        self.assertEqual(heat_coefficient_real, 0.5)

    def test_power_source_information(self):
        logging.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            120.1
        )
        logging.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            5.1
        )

    def test_voltage_limit_value(self):
        logging.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 122.0)

    def test_nom_power_value(self):
        logging.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        logging.info("Check nominal power value...")
        rand_pause()
        logging.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 25.0])

    def test_current_limit_value(self):
        logging.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 5.0)

    def test_heat_coef_value(self):
        logging.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        logging.info("Check heat coefficient value...")
        rand_pause()
        logging.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertNotIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_pressure_coef_value(self):
        logging.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.01)

    def test_power_connected_to_ventilator(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNotNone(connected_power)

    def test_connected_power_motor_type(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        logging.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCMotor", connected_power)

    def test_pressure_class_information(self):
        logging.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        logging.info(f"Pressure: {vent_pressure}")
        self.assertTrue("class" in vent_pressure)

    def test_heat_is_not_int_type(self):
        logging.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertFalse(heat_coefficient.is_integer())

    def test_heat_real_info(self):
        logging.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        logging.info(f"Value is {heat_coefficient_real}")
        self.assertEqual(heat_coefficient_real, 0.5)

    def test_power_source_is_as_declared(self):
        logging.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            120.1
        )
        logging.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            5.1
        )

    def test_voltage_value_less_limit(self):
        logging.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 122.0)

    def test_nominal_power_in_values(self):
        logging.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        logging.info("Check nominal power value...")
        rand_pause()
        logging.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 25.0])

    def test_current_limit_info(self):
        logging.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 5.0)

    def test_heat_coefficient_not_in_values(self):
        logging.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        logging.info("Check heat coefficient value...")
        rand_pause()
        logging.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertNotIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_pressure_coefficient_info(self):
        logging.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.01)

    def test_power_is_connected_to_motor(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNotNone(connected_power)

    def test_connected_power_is_dc_motor(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        logging.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCMotor", connected_power)

    def test_pressure_information(self):
        logging.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        logging.info(f"Pressure: {vent_pressure}")
        self.assertTrue("class" in vent_pressure)

    def test_heat_not_integer(self):
        logging.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertFalse(heat_coefficient.is_integer())

    def test_heat_value_real(self):
        logging.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        logging.info(f"Value is {heat_coefficient_real}")
        self.assertEqual(heat_coefficient_real, 0.5)

    def test_tenv_connected_power_motor_type(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        logging.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCMotor", connected_power)

    def test_tenv_pressure_class_information(self):
        logging.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        logging.info(f"Pressure: {vent_pressure}")
        self.assertTrue("class" in vent_pressure)

    def test_tenv_heat_is_not_int_type(self):
        logging.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertFalse(heat_coefficient.is_integer())

    def test_tenv_heat_real_info(self):
        logging.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        logging.info(f"Value is {heat_coefficient_real}")
        self.assertEqual(heat_coefficient_real, 0.5)

    def test_tenv_power_source_is_as_declared(self):
        logging.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            120.1
        )
        logging.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            5.1
        )

    def test_tenv_voltage_value_less_limit(self):
        logging.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 122.0)

    def test_tenv_nominal_power_in_values(self):
        logging.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        logging.info("Check nominal power value...")
        rand_pause()
        logging.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 25.0])

    def test_tenv_current_limit_info(self):
        logging.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 5.0)

    def test_tenv_heat_coefficient_not_in_values(self):
        logging.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        logging.info("Check heat coefficient value...")
        rand_pause()
        logging.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertNotIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_tenv_pressure_coefficient_info(self):
        logging.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.01)

    def test_tenv_power_is_connected_to_motor(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNotNone(connected_power)

    def test_tenv_connected_power_is_dc_motor(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        logging.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCMotor", connected_power)

    def test_tenv_pressure_information(self):
        logging.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        logging.info(f"Pressure: {vent_pressure}")
        self.assertTrue("class" in vent_pressure)

    def test_tenv_heat_not_integer(self):
        logging.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertFalse(heat_coefficient.is_integer())

    def test_tenv_heat_value_real(self):
        logging.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        logging.info(f"Value is {heat_coefficient_real}")
        self.assertEqual(heat_coefficient_real, 0.5)

    def test_source_power(self):
        logging.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            120.1
        )
        logging.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            5.1
        )

    def test_limit_of_voltage(self):
        logging.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 122.0)

    def test_power_nominal(self):
        logging.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        logging.info("Check nominal power value...")
        rand_pause()
        logging.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 25.0])

    def test_limit_of_current(self):
        logging.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 5.0)

    def test_coefficient_of_heat(self):
        logging.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        logging.info("Check heat coefficient value...")
        rand_pause()
        logging.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertNotIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_coefficient_of_pressure(self):
        logging.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.01)

    def test_if_power_is_connected(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNotNone(connected_power)

    def test_if_connected_power_is_motor(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        logging.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCMotor", connected_power)

    def test_class_of_pressure(self):
        logging.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        logging.info(f"Pressure: {vent_pressure}")
        self.assertTrue("class" in vent_pressure)

    def test_value_heat_not_int(self):
        logging.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertFalse(heat_coefficient.is_integer())

    def test_value_heat_real(self):
        logging.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        logging.info(f"Value is {heat_coefficient_real}")
        self.assertEqual(heat_coefficient_real, 0.5)

    def test_source_of_power(self):
        logging.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            120.1
        )
        logging.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            5.1
        )

    def test_limit_voltage(self):
        logging.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 122.0)

    def test_power_nominal_value(self):
        logging.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        logging.info("Check nominal power value...")
        rand_pause()
        logging.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 25.0])

    def test_limit_current(self):
        logging.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 5.0)

    def test_coefficient_heat(self):
        logging.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        logging.info("Check heat coefficient value...")
        rand_pause()
        logging.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertNotIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_coefficient_pressure(self):
        logging.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.01)

    def test_if_power_is_connected_to_ventilator(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNotNone(connected_power)

    def test_if_connected_power_is_motor_class(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        logging.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCMotor", connected_power)

    def test_pressure_returns_class(self):
        logging.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        logging.info(f"Pressure: {vent_pressure}")
        self.assertTrue("class" in vent_pressure)

    def test_value_heat_is_not_int(self):
        logging.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertFalse(heat_coefficient.is_integer())

    def test_value_of_heat_real(self):
        logging.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        logging.info(f"Value is {heat_coefficient_real}")
        self.assertEqual(heat_coefficient_real, 0.5)

    def test_source_power_voltage_and_limit(self):
        logging.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            120.1
        )
        logging.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            5.1
        )

    def test_limit_voltage_value(self):
        logging.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 122.0)

    def test_power_nominal_in_values(self):
        logging.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        logging.info("Check nominal power value...")
        rand_pause()
        logging.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 25.0])

    def test_limit_current_greater_than_value(self):
        logging.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 5.0)

    def test_coefficient_heat_not_in_values(self):
        logging.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        logging.info("Check heat coefficient value...")
        rand_pause()
        logging.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertNotIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_coefficient_pressure_less_than_value(self):
        logging.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.01)

    def test_power_is_connected_to_ventilator_device(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNotNone(connected_power)

    def test_connected_power_is_motor_class(self):
        logging.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        logging.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCMotor", connected_power)

    def test_pressure_return_type(self):
        logging.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        logging.info(f"Pressure: {vent_pressure}")
        self.assertTrue("class" in vent_pressure)

    def test_value_heat_is_not_integer(self):
        logging.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertFalse(heat_coefficient.is_integer())

    def test_value_of_heat_real_value(self):
        logging.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        logging.info(f"Value is {heat_coefficient_real}")
        self.assertEqual(heat_coefficient_real, 0.5)

if __name__ == "__main__":
    unittest.main()
