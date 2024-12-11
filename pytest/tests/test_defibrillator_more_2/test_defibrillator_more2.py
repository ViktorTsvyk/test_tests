""" Test file to test the Defibrillator Device

NOTE: the tenv_instance fixture is used in this file!
Please, see the "conftest.py" file content in order to see the fixture details

To run the tests make sure that pytest is set as a default tests runner in your IDE

Run the following commands from the Terminal to run tests:
* current directory is devsure *
    pytest
        (to run all tests under the "tests" directory)
    pytest devsure_demo/tests_demo/pytest/tests/test_defibrillator_more_2
        (to run all tests under the "test_defibrillator_more_2" directory)
    pytest devsure_demo/tests_demo/pytest/tests/test_defibrillator_more_2/test_defibrillator_more2.py
        (to run all tests from the "test_defibrillator_more2.py" test file)
    or simply run specific test with your IDE (click on the test name and select Run option)

"""
import pytest
from .tenv import TEnv
import random
import time

# ---------------------------------------
def rand_pause():
    pause_sec = random.randint(0, 1)
    time.sleep(pause_sec)

# ---------------------------------------

# ______________________________________________
# Test data - heart rhythm
NORMAL_RHYTHM = [75.0, 80.0, 72.0, 75.0, 78.0, 76.0]
VENTRICULAR_FIBRILLATION = [50.0, 55.0, 45.0, 52.0, 53.0]
PULSELESS_VENTRICULAR_TACHYCARDIA = [120.0, 110.0, 115.0, 118.0, 122.0]


# ______________________________________________
# Test normal rhythm
def test_normal_rhythm_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.power_source.battery_level == 100.0


def test_normal_rhythm_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Normal rhythm"


# ______________________________________________
# Test ventricular fibrillation rhythm
def test_ventricular_fibrillation_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    rand_pause()
    assert tenv.power_source.battery_level < 100.0


def test_ventricular_fibrillation_capacitor_discharge(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage == 0.0


# ______________________________________________
# Test pulseless ventricular tachycardia rhythm
def test_pulseless_ventricular_tachycardia_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level < 100.0


def test_pulseless_ventricular_tachycardia_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status == "Tachycardia without a pulse"


# ______________________________________________
# Test speaker
def test_speaker_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions..."


def test_speaker_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.speaker.instruction == "No shock needed. Continue monitoring..."


def test_speaker_not_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.speaker.instruction == "Preparing to deliver shock. Do not touch the body!"


# ______________________________________________
# Test switch
def test_switch_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert not tenv.switch.state


def test_switch_normal_rhythm_state(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert not tenv.switch.state


def test_switch_state_dropped_after_shock(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert not tenv.switch.state
