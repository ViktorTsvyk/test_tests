""" Test file to test the Blood Measure Device

NOTE: the tenv_instance fixture is used in this file!
Please, see the "conftest.py" file content in order to see the fixture details

To run the tests make sure that pytest is set as a default tests runner in your IDE

Run the following commands from the Terminal to run tests:
* current directory is devsure *
    pytest
        (to run all tests under the "tests" directory)
    pytest devsure_demo/tests_demo/pytest/tests/test_blood_more_1
        (to run all tests under the "test_blood_more_1" directory)
    pytest devsure_demo/tests_demo/pytest/tests/test_blood_more_1/test_blood_more1.py
        (to run all tests from the "test_blood_more1.py" test file)
    or simply run specific test with your IDE (click on the test name and select Run option)

"""


import pytest
from .tenv import TEnv
import random
import time

# ---------------------------------------
def rand_pause():
    pause_sec = random.randint(0, 3)
    time.sleep(pause_sec)

# ---------------------------------------


def test_additional_pressure(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure > 0


def test_pressure_inside_cuff(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    rand_pause()
    result_pressure = tenv.pump.pressure.measurement
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure - additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_cuff_connection_negative(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Inflatable Cuff is not connected"


def test_pressure_in_cuff_more_then_additional(tenv: TEnv):
    rand_pause()
    assert tenv.pump.pressure.measurement > tenv.pump.pumping()


def test_power_adapter_efficiency(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 0.2