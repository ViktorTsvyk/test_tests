""" 11 tests fail, 91 tests pass """
import unittest
from devsure.test_base.test_case_base import TestCaseBase
from .tenv import TEnv
import time
import random
from common_items.use_variables import *

# ---------------------------------------
def rand_pause():
    pause_sec = random.randint(0, 3)
    time.sleep(pause_sec)


# ---------------------------------------


class TestOurModel(TestCaseBase):
    def setUp(self) -> None:
        # Set up testing environment
        self.tenv = TEnv()
        self.log.debug(
            f"Testing the pressure inside the cuff with the target pressure:"
            f" {self.tenv.blood_pressure_md.target_pressure}"
        )

    def tearDown(self) -> None:
        # Tear down testing environment
        self.tenv.tear_down()

    def test_additional_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        self.log.debug(f"Some test value: '{COMMON_DICT}'")
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
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
        self.log.debug(f"Some test value: '{not_global_dict}'")
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_additional_pressure_exists(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_pressure_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_additional_val_pressure_exists(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure_value(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        self.log.debug(f"Some test value: '{COMMON_LIST}'")
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
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

    def test_pressure_in_cuff_greater_then_additional_pressure(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_additional_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure_value_info(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_pressure_inside_the_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        self.log.debug(f"Some test value: '{not_global_list}'")
        additional = self.tenv.pump.pumping()
        self.assertLess(pressure_in_cuff, additional)

    def test_additional_value_pressure_exists(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertLess(additional_pump_pressure, 0)

    def test_cuff_connection_initial_message(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_in_cuff_greater_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertIsNone(pressure_in_cuff)

    def test_add_pressure_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_pressure_value(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.log.debug(f"Some test value: '{COMMON_STRING}'")
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_no_connection_msg(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff connected"

    def test_pressure_inside_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_addit_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure_info(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.log.debug(f"Some test value: '{not_global_string}'")
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure + additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_msg_text(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_in_cuff_greater_then_addit_pressure(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_present_additional_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 350)

    def test_value_of_target_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_msg_initial(self) -> None:
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

    def test_additional_pressure_value_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_value_info_target_pressure(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
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

    def test_pressure_cuff_greater_additional_val(self):
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
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
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
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_in_cuff_greater_of_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_additional_pressure_present_for_pump(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure_pump(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_state_msg(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_in_cuff_greater_additional_pump_pressure(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_addit_pressure_is_present(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure_calc(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_message_text(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_cuff_greater_then_additional_pressure(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_target_pressure_information(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_warning(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_calc_pressure_in_cuff_greater_then_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_calc_pressure_in_cuff(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        self.log.info(f"Pressure in cuff is: {pressure_in_cuff}")
        self.assertTrue(pressure_in_cuff)

    def test_target_pressure_info_about(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_target_pressure_measurement(self) -> None:
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertIsNotNone(
            result_pressure,
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connect_initial_message_text(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_in_cuff_greater_additional_pressure(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_initial_pressure_information(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_warning_message(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_calc_pressure_in_cuff_greater_then_additional_value(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_calculation_pressure_in_cuff(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        self.log.info(f"Pressure in cuff is: {pressure_in_cuff}")
        self.assertTrue(pressure_in_cuff)

    def test_calc_target_pressure_info(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_the_target_pressure_measurement(self) -> None:
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertIsNotNone(
            result_pressure,
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_state_info(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_in_cuff_greater_of_additional_pressure(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_additional_pressure_present_for_pump_device(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure_pump_device(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_state_msg_text(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_in_cuff_greater_additional_pump_pressure_value(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_addit_pressure_is_present_for_pump(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure_calc_value(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_message_txt(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_cuff_greater_then_additional_pressure_info(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_target_pressure_value_equal(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_warning_txt(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_calc_pressure_in_cuff_greater_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_calc_pressure_cuff(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        self.log.info(f"Pressure in cuff is: {pressure_in_cuff}")
        self.assertTrue(pressure_in_cuff)

    def test_target_pressure_about(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_the_target_pressure_calc(self) -> None:
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertIsNotNone(
            result_pressure,
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connect_initial_message_warning(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_calc_target_pressure_inform(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_the_target_pressure_measurement_val(self) -> None:
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertIsNotNone(
            result_pressure,
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_state_info_message(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_in_cuff_greater_of_additional_pressure_val(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_additional_pressure_present_pump_device(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure_for_pump_device(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_state_msg_val(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_in_cuff_greater_additional_pump_pressure_val(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_addit_pressure_is_present_pump(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 0)

    def test_target_pressure_calculation_value(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_msg_txt(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_pressure_cuff_val_greater_then_additional_pressure(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_target_pressure_val_equal(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_warning_val(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_calculation_pressure_in_cuff_greater_additional(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional)

    def test_calculation_pressure_cuff(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        self.log.info(f"Pressure in cuff is: {pressure_in_cuff}")
        self.assertTrue(pressure_in_cuff)

    def test_target_pressure_about_values(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_the_target_pressure_calculation_value(self) -> None:
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertIsNotNone(
            result_pressure,
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connect_initial_message_warning_txt(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Inflatable Cuff is not connected"

    def test_cuff_connection_initial_information(self) -> None:
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

    def test_additional_pressure_val_exists(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 1000)

    def test_target_pressure_val(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertNotEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure - additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

    def test_cuff_connection_initial_msg_present(self) -> None:
        self.tenv.pump._cuff = None
        rand_pause()
        try:
            self.tenv.pump.connected_cuff()
        except ValueError as error:
            assert str(error) == "Cuff is not connected"

    def test_pressure_in_cuff_greater_then_additional_press(self):
        pressure_in_cuff = self.tenv.pump.pressure.measurement
        rand_pause()
        additional = self.tenv.pump.pumping()
        self.assertGreater(pressure_in_cuff, additional + 15)

    def test_additional_press(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        rand_pause()
        self.assertGreater(additional_pump_pressure, 13)

    def test_target_pressure_val_info(self) -> None:
        additional_pump_pressure = self.tenv.pump.pumping()
        self.log.info(f"Additional pump pressure is {additional_pump_pressure}")
        rand_pause()
        result_pressure = self.tenv.pump.pressure.measurement
        self.log.info(f"Pressure inside the cuff is {result_pressure}")
        rand_pause()
        self.assertEqual(
            first=self.tenv.blood_pressure_md.target_pressure,
            second=(result_pressure * additional_pump_pressure),
            msg=f"User did not get the target pressure value - {self.tenv.blood_pressure_md.target_pressure}"
        )

if __name__ == "__main__":
    unittest.main()