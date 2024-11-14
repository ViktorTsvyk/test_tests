""" 106 TESTS FAIL """

import unittest
from devsure.test_base.test_case_base import TestCaseBase
from .tenv import TEnv
import time
import random

# ---------------------------------------
def rand_pause():
    pause_sec = random.randint(0,2)
    time.sleep(pause_sec)
# ---------------------------------------

class TestOurModel(TestCaseBase):
    def setUp(self) -> None:
        self.log.debug("The most basic demo for GL TAF using unittest available 'out of the box'")
        self.tenv = TEnv()

    def tearDown(self):
        self.tenv.tear_down()

    def test_power_source(self):
        self.log.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            121.1
        )
        self.log.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            6.2
        )

    def test_voltage(self):
        self.log.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 1.0)

    def test_nominal_power(self):
        self.log.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        self.log.info("Check nominal power value...")
        rand_pause()
        self.log.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 22.0, 27.0])

    def test_current(self):
        self.log.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 25.0)

    def test_heat_coefficient(self):
        self.log.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.log.info("Check heat coefficient value...")
        rand_pause()
        self.log.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_pressure_coefficient(self):
        self.log.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.00000000000000001)

    def test_power_is_connected(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = None
        self.assertIsNotNone(connected_power)

    def test_connected_power_is_motor(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        self.log.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCPowerAdapter", connected_power)

    def test_pressure_class(self):
        self.log.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        self.log.info(f"Pressure: {vent_pressure}")
        self.assertTrue("class" not in vent_pressure)

    def test_heat_not_int(self):
        self.log.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertTrue(heat_coefficient.is_integer())

    def test_heat_real(self):
        self.log.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        self.log.info(f"Value is {heat_coefficient_real}")
        self.assertNotEqual(heat_coefficient_real, 0.5)

    def test_power_source_info(self):
        self.log.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            127.2
        )
        self.log.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            16.3
        )

    def test_voltage_value(self):
        self.log.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 3.2)

    def test_nominal_power_value(self):
        self.log.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        self.log.info("Check nominal power value...")
        rand_pause()
        self.log.info(f"Nominal power value is {nom_power}")
        self.assertNotIn(nom_power, [23.0, 24.0, 25.0])

    def test_current_value(self):
        self.log.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertLessEqual(current, 4.1)

    def test_heat_coefficient_value(self):
        self.log.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.log.info("Check heat coefficient value...")
        rand_pause()
        self.log.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertIn(heat_coefficient , [3.0, 15.0, 163.0])

    def test_pressure_coefficient_value(self):
        self.log.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.00000000000001)

    def test_power_is_connected_to_ventilator(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNone(connected_power)

    def test_connected_power_is_motor_type(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        self.log.info(f"Power: {connected_power}")
        rand_pause()
        self.assertNotIn("DCMotor", connected_power)

    def test_pressure_class_info(self):
        self.log.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        self.log.info(f"Pressure: {vent_pressure}")
        self.assertFalse("class" in vent_pressure)

    def test_heat_not_int_type(self):
        self.log.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertTrue(heat_coefficient.is_integer())

    def test_connected_power_motor(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        self.log.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCPowerAdapter", connected_power)

    def test_pressure_is_not_class(self):
        self.log.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        self.log.info(f"Pressure: {vent_pressure}")
        self.assertTrue("class" not in vent_pressure)

    def test_heat_in_int(self):
        self.log.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertTrue(heat_coefficient.is_integer())

    def test_heat_not_real(self):
        self.log.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        self.log.info(f"Value is {heat_coefficient_real}")
        self.assertNotEqual(heat_coefficient_real, 0.5)

    def test_power_source_info_value(self):
        self.log.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            127.2
        )
        self.log.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            16.3
        )

    def test_voltage_value_info(self):
        self.log.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 3.2)

    def test_nominal_power_values(self):
        self.log.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        self.log.info("Check nominal power value...")
        rand_pause()
        self.log.info(f"Nominal power value is {nom_power}")
        self.assertNotIn(nom_power, [23.0, 24.0, 25.0])

    def test_current_value_less(self):
        self.log.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertLessEqual(current, 4.1)

    def test_heat_coefficient_values(self):
        self.log.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.log.info("Check heat coefficient value...")
        rand_pause()
        self.log.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertIn(heat_coefficient , [3.0, 15.0, 163.0])

    def test_pressure_coefficient_value_less(self):
        self.log.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.00000000000001)

    def test_power_is_none(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNone(connected_power)

    def test_connected_power_is_not_motor_type(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        self.log.info(f"Power: {connected_power}")
        rand_pause()
        self.assertNotIn("DCMotor", connected_power)

    def test_pressure_class_false(self):
        self.log.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        self.log.info(f"Pressure: {vent_pressure}")
        self.assertFalse("class" in vent_pressure)

    def test_heat_int_type(self):
        self.log.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertTrue(heat_coefficient.is_integer())

    def test_heat_real_value(self):
        self.log.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        self.log.info(f"Value is {heat_coefficient_real}")
        self.assertNotEqual(heat_coefficient_real, 0.5)

    def test_power_source_information(self):
        self.log.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            130.1
        )
        self.log.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            8.1
        )

    def test_voltage_limit_value(self):
        self.log.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertGreater(voltage, 122.0)

    def test_nom_power_value(self):
        self.log.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        self.log.info("Check nominal power value...")
        rand_pause()
        self.log.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 29.0])

    def test_current_limit_value(self):
        self.log.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 7.2)

    def test_heat_coef_value(self):
        self.log.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.log.info("Check heat coefficient value...")
        rand_pause()
        self.log.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertNotIn(heat_coefficient , [3.0, 11.0, 67.0, 0.5])

    def test_pressure_coef_value(self):
        self.log.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertEqual(pressure_coef, 0.01)

    def test_power_connected_to_ventilator(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = None
        self.assertIsNotNone(connected_power)

    def test_connected_power_motor_type(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        self.log.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("PowerDevice", connected_power)

    def test_pressure_class_information(self):
        self.log.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        self.log.info(f"Pressure: {vent_pressure}")
        self.assertFalse("class" in vent_pressure)

    def test_heat_is_not_int_type(self):
        self.log.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertTrue(heat_coefficient.is_integer())

    def test_heat_real_info(self):
        self.log.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        self.log.info(f"Value is {heat_coefficient_real}")
        self.assertNotEqual(heat_coefficient_real, 0.5)

    def test_power_source_is_as_declared(self):
        self.log.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            120.1
        )
        self.log.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertNotEqual(
            self.tenv.power_source.current_limit,
            5.1
        )

    def test_voltage_value_less_limit(self):
        self.log.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertGreater(voltage, 122.0)

    def test_nominal_power_in_values(self):
        self.log.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        self.log.info("Check nominal power value...")
        rand_pause()
        self.log.info(f"Nominal power value is {nom_power}")
        self.assertNotIn(nom_power, [23.0, 24.0, 25.0])

    def test_current_limit_info(self):
        self.log.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertLessEqual(current, 3.0)

    def test_heat_coefficient_not_in_values(self):
        self.log.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.log.info("Check heat coefficient value...")
        rand_pause()
        self.log.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_pressure_coefficient_info(self):
        self.log.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertGreater(pressure_coef, 0.01)

    def test_power_is_connected_to_motor(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNone(connected_power)

    def test_connected_power_is_dc_motor(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        self.log.info(f"Power: {connected_power}")
        rand_pause()
        self.assertNotIn("DCMotor", connected_power)

    def test_pressure_information(self):
        self.log.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        self.log.info(f"Pressure: {vent_pressure}")
        self.assertTrue("cass" in vent_pressure)

    def test_heat_not_integer(self):
        self.log.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertTrue(heat_coefficient.is_integer())

    def test_heat_value_real(self):
        self.log.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        self.log.info(f"Value is {heat_coefficient_real}")
        self.assertNotEqual(heat_coefficient_real, 0.5)

    def test_tenv_connected_power_motor_type(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        self.log.info(f"Power: {connected_power}")
        rand_pause()
        self.assertNotIn("DCMotor", connected_power)

    def test_tenv_pressure_class_information(self):
        self.log.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        self.log.info(f"Pressure: {vent_pressure}")
        self.assertFalse("class" in vent_pressure)

    def test_tenv_heat_is_not_int_type(self):
        self.log.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertTrue(heat_coefficient.is_integer())

    def test_tenv_heat_real_info(self):
        self.log.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        self.log.info(f"Value is {heat_coefficient_real}")
        self.assertNotEqual(heat_coefficient_real, 0.5)

    def test_tenv_power_source_is_as_declared(self):
        self.log.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertNotEqual(
            self.tenv.power_source.voltage_limit,
            120.1
        )
        self.log.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertNotEqual(
            self.tenv.power_source.current_limit,
            5.1
        )

    def test_tenv_voltage_value_less_limit(self):
        self.log.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 10.0)

    def test_tenv_nominal_power_in_values(self):
        self.log.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        self.log.info("Check nominal power value...")
        rand_pause()
        self.log.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 31.0])

    def test_tenv_current_limit_info(self):
        self.log.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 12.0)

    def test_tenv_heat_coefficient_not_in_values(self):
        self.log.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.log.info("Check heat coefficient value...")
        rand_pause()
        self.log.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertNotIn(heat_coefficient , [3.0, 11.0, 67.0, 0.5])

    def test_tenv_pressure_coefficient_info(self):
        self.log.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0)

    def test_tenv_power_is_connected_to_motor(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNone(connected_power)

    def test_tenv_connected_power_is_dc_motor(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        self.log.info(f"Power: {connected_power}")
        rand_pause()
        self.assertNotIn("DCMotor", connected_power)

    def test_tenv_pressure_information(self):
        self.log.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        self.log.info(f"Pressure: {vent_pressure}")
        self.assertFalse("class" in vent_pressure)

    def test_tenv_heat_not_integer(self):
        self.log.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertTrue(heat_coefficient.is_integer())

    def test_tenv_heat_value_real(self):
        self.log.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        self.log.info(f"Value is {heat_coefficient_real}")
        self.assertNotEqual(heat_coefficient_real, 0.5)

    def test_source_power(self):
        self.log.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            155.1
        )
        self.log.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            15.1
        )

    def test_limit_of_voltage(self):
        self.log.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertGreater(voltage, 203.0)

    def test_power_nominal(self):
        self.log.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        self.log.info("Check nominal power value...")
        rand_pause()
        self.log.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 41.0])

    def test_limit_of_current(self):
        self.log.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 17.0)

    def test_coefficient_of_heat(self):
        self.log.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.log.info("Check heat coefficient value...")
        rand_pause()
        self.log.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_coefficient_of_pressure(self):
        self.log.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertGreaterEqual(pressure_coef, 0.01)

    def test_if_power_is_connected(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNone(connected_power)

    def test_if_connected_power_is_motor(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        self.log.info(f"Power: {connected_power}")
        rand_pause()
        self.assertIn("DCRotor", connected_power)

    def test_class_of_pressure(self):
        self.log.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        self.log.info(f"Pressure: {vent_pressure}")
        self.assertFalse("class" in vent_pressure)

    def test_value_heat_not_int(self):
        self.log.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertTrue(heat_coefficient.is_integer())

    def test_value_heat_real(self):
        self.log.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        self.log.info(f"Value is {heat_coefficient_real}")
        self.assertEqual(heat_coefficient_real, 0.13)

    def test_source_of_power(self):
        self.log.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            180.1
        )
        self.log.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            8.1
        )

    def test_limit_voltage(self):
        self.log.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 18.0)

    def test_power_nominal_value(self):
        self.log.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        self.log.info("Check nominal power value...")
        rand_pause()
        self.log.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [23.0, 24.0, 28.0])

    def test_limit_current(self):
        self.log.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 8.0)

    def test_coefficient_heat(self):
        self.log.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.log.info("Check heat coefficient value...")
        rand_pause()
        self.log.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertIn(heat_coefficient , [3.0, 11.0, 67.0])

    def test_coefficient_pressure(self):
        self.log.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0)

    def test_if_power_is_connected_to_ventilator(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = None
        self.assertIsNotNone(connected_power)

    def test_if_connected_power_is_motor_class(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        self.log.info(f"Power: {connected_power}")
        rand_pause()
        self.assertNotIn("DCMotor", connected_power)

    def test_pressure_returns_class(self):
        self.log.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        self.log.info(f"Pressure: {vent_pressure}")
        self.assertFalse("class" in vent_pressure)

    def test_value_heat_is_not_int(self):
        self.log.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertTrue(heat_coefficient.is_integer())

    def test_value_of_heat_real(self):
        self.log.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        self.log.info(f"Value is {heat_coefficient_real}")
        self.assertFalse(heat_coefficient_real)

    def test_source_power_voltage_and_limit(self):
        self.log.info(f"Voltage limit: {self.tenv.power_source.voltage_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.voltage_limit,
            113.1
        )
        self.log.info(f"Current limit: {self.tenv.power_source.current_limit}")
        rand_pause()
        self.assertEqual(
            self.tenv.power_source.current_limit,
            5.3
        )

    def test_limit_voltage_value(self):
        self.log.info("Determining voltage...")
        rand_pause()
        voltage = self.tenv.power_source.voltage_limit
        self.assertLess(voltage, 16.0)

    def test_power_nominal_in_values(self):
        self.log.info("Determining nominal power...")
        rand_pause()
        nom_power = self.tenv.motor.nominal_power
        self.log.info("Check nominal power value...")
        rand_pause()
        self.log.info(f"Nominal power value is {nom_power}")
        self.assertIn(nom_power, [33.0, 54.0, 45.0])

    def test_limit_current_greater_than_value(self):
        self.log.info("Determining current limit...")
        rand_pause()
        current = self.tenv.power_source.current_limit
        self.assertGreaterEqual(current, 33.0)

    def test_coefficient_heat_not_in_values(self):
        self.log.info("Determining heat coefficient...")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.log.info("Check heat coefficient value...")
        rand_pause()
        self.log.info(f"Heat coefficient value is {heat_coefficient}")
        self.assertNotIn(heat_coefficient , [3.0, 11.0, 1.0, 0.5])

    def test_coefficient_pressure_less_than_value(self):
        self.log.info("Determining pressure coefficient...")
        rand_pause()
        pressure_coef = self.tenv.ventilator.pressure_coefficient
        self.assertLessEqual(pressure_coef, 0.000000000001)

    def test_power_is_connected_to_ventilator_device(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = self.tenv.ventilator.connected_power
        self.assertIsNone(connected_power)

    def test_connected_power_is_motor_class(self):
        self.log.info("Read information from the connected power...")
        rand_pause()
        connected_power = str(self.tenv.ventilator.connected_power)
        self.log.info(f"Power: {connected_power}")
        rand_pause()
        self.assertNotIn("DCMotor", connected_power)

    def test_pressure_return_type(self):
        self.log.info("Read information about the ventilator pressure...")
        rand_pause()
        vent_pressure = str(type(self.tenv.ventilator.pressure))
        self.log.info(f"Pressure: {vent_pressure}")
        self.assertFalse("class" in vent_pressure)

    def test_value_heat_is_not_integer(self):
        self.log.info(f"Check the heat coefficient type")
        rand_pause()
        heat_coefficient = self.tenv.ventilator.heat_coefficient
        self.assertTrue(heat_coefficient.is_integer())

    def test_value_of_heat_real_value(self):
        self.log.info(f"Check the heat coefficient...")
        rand_pause()
        heat_coefficient_real = self.tenv.ventilator.heat_coefficient.real
        self.log.info(f"Value is {heat_coefficient_real}")
        self.assertNotEqual(heat_coefficient_real, 0.5)

if __name__ == "__main__":
    unittest.main()
