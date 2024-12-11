""" 180 TESTS FAIL """
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
        # Set up testing environment
        self.tenv = TEnv()
        logging.debug(
            f"Testing the pressure inside the cuff with the target pressure:"
            f" {self.tenv.blood_pressure_md.target_pressure}"
        )

    def tearDown(self) -> None:
        # Tear down testing environment
        self.tenv.tear_down()

    def test_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure(self) -> None:
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

    def test_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_greater_then_additional(self):
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

    def test_add_pressure_is_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_val(self) -> None:
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

    def test_the_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_the_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_is_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_val_target_pressure(self) -> None:
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

    def test_cuff_connection_initial_state_txt(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_inside_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_present_in_pump(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_present(self) -> None:
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

    def test_cuff_connection_initial_text(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_greater_then_additional_value(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_present_pump(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_pump(self) -> None:
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

    def test_cuff_connection_initial_txt(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_greater_then_additional_val(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_present_for_pump(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_in_pump(self) -> None:
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

    def test_cuff_connection_initial_state_text(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_greater_then_additional_compare(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_value_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_value_pressure(self) -> None:
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

    def test_the_cuff_connection_initial_state(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_is_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_is_present_pump(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

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

    def test_target_pressure_value_for_pump(self) -> None:
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

    def test_cuff_connection_state_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_add_pressure_present_val(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_value_of_target_pressure(self) -> None:
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

    def test_state_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_value_of_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_is_present_for_pump(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_pump_target_pressure_value(self) -> None:
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

    def test_value_of_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_value_of_pressure_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_in_pump_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_in_pump_target_pressure(self) -> None:
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

    def test_in_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_in_pump_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_for_pump_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_the_target_pressure(self) -> None:
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

    def test_the_state_of_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_the_pressure_in_cuff(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_present_pump_pumping(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_not_equal(self) -> None:
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

    def test_cuff_connection_initial_error(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_greater_then_additional_values(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_present_for_pumping(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_pumping(self) -> None:
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

    def test_cuff_device_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_greater_then_additional_for_device(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_present_for_device(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_pump_device(self) -> None:
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

    def test_cuff_connection_initial_state_message(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_greater_then_additional_pressure(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_present_for_pump_device(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_for_device(self) -> None:
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

    def test_cuff_connection_initial_message_state(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_greater_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_value_is_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_pump_device_target_pressure(self) -> None:
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

    def test_cuff_device_connection_initial_state(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_for_pump_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_for_pump_additional_pressure_is_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_for_pumping_target_pressure(self) -> None:
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

    def test_msg_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_less_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_less(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_information(self) -> None:
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

    def test_cuff_connection_initial_information(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_less_then_additional_pressure(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_for_device(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_info(self) -> None:
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

    def test_cuff_connection_initial_info(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_for_cuff_less_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_present_is_less(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_value_info(self) -> None:
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

    def test_cuff_connection_initial_state_info(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_less(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pump_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pump_pressure(self) -> None:
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

    def test_initial_cuff_connection_info(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_in_cuff_pressure_less_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_in_pump_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_in_pump_target_pressure_val(self) -> None:
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

    def test_cuff_connection_initial_state_information(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_less_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_for_pumping(self) -> None:
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

    def test_the_cuff_connection_initial_val(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_val_pressure_in_cuff_less_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_val_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_value_of_target_pressure_pump(self) -> None:
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

    def test_msg_cuff_connection(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_less_add(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_appears(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_pumping_target_pressure(self) -> None:
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

    def test_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_cuff_greater_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_press(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_press_pump(self) -> None:
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

    def test_cuff_connection_initial_msg_val(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_cuff_pressure_is_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_is_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_is_target_pressure(self) -> None:
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

    def test_message_of_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_if_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_if_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_val_of_target_pressure(self) -> None:
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

    def test_infp_for_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_value_of_the_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_the_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_pumping_val_target_pressure(self) -> None:
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

    def test_val_of_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_less_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_the_target_value_pressure(self) -> None:
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

    def test_device_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_device_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_device_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_the_device_target_pressure(self) -> None:
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

    def test_the_cuff_device_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_the_pressure_in_cuff_device_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_device_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_device_pressure(self) -> None:
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

    def test_cuff_device_connection_initial_msg(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_device_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_device_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_device_pressure_val(self) -> None:
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

    def test_device_cuff_connection_init(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_greater_then_additional_pressure_of_device(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_pump_device_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_pump_device_target_pressure_value(self) -> None:
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

    def test_value_of_cuff_connection_initial_message(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_device_pressure_inside_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_addit_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_info_for_pump(self) -> None:
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

    def test_cuff_connection_initial_txt_check(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_is_less_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_is_present_for_pumping(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_the_target_pressure_val(self) -> None:
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

    def test_cuff_connection_initial_information_text(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_is_not_greater(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_true(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_not_equal_val(self) -> None:
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

    def test_cuff_connection_state(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_in_cuff_compare(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_pumping(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_pump_pumping(self) -> None:
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

    def test_connection_of_cuff_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_target_pressure_values(self) -> None:
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

    def test_cuff_connection_initial_msg_text(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_pressure_cuff_is_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_pressure_less_then(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_device_pump_target_pressure(self) -> None:
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

    def test_device_cuff_connection(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_device_pressure_in_cuf(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_device_additional_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_pumping_of_pump_target_pressure(self) -> None:
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

    def test_is_cuff_connection_initial(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff has been connected"

    def test_is_pressure_in_cuff_less_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

if __name__ == "__main__":
    unittest.main()
