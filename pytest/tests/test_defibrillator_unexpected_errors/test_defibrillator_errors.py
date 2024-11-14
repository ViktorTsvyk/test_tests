""" Has tests with unexpected errors (6 fail, 8 pass):
FileNotFoundError
IndexError
ZeroDivisionError
AttributeError
MemoryError
RuntimeError
"""
import json
import os
from pathlib import Path
import random
import time
from .tenv import TEnv
from common_items.use_function import increase_value

# ---------------------------------------
def rand_pause():
    pause_sec = random.randint(3, 6)
    time.sleep(pause_sec)

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

def test_unexpected_error_file(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    dummy_path = os.path.join(Path(__file__).parent, "dummy.txt")
    with open(dummy_path, "r", encoding="utf-8") as dum_file:
        dummy_data = json.load(dum_file)
    assert dummy_data

def test_normal_rhythm_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Normal rhythm"

# ______________________________________________
# Test ventricular fibrillation rhythm
def test_unexpected_error_list(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    rand_pause()
    battery_level = tenv.power_source.battery_level
    some_value = NORMAL_RHYTHM[6]
    assert battery_level < some_value


def test_unexpected_error_division(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    some_value = tenv.power_source.battery_level / tenv.capacitor.charge_voltage
    s_value = increase_value(some_value)
    print(s_value)
    assert some_value > 0

def test_unexpected_error_attribute(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    some_value = tenv.capacitor.charge_voltage.append(56)
    assert len(some_value) > 2

# ______________________________________________
# Test pulseless ventricular tachycardia rhythm
def test_pulseless_ventricular_tachycardia_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level < 100.0


def test_pulseless_ventricular_tachycardia_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
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


def test_unexpected_memory_error(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    my_list = [tenv.speaker.instruction]
    new_value = "New instruction"
    my_list.append(new_value * 10000000000000000)
    assert len(my_list) > 2

# ______________________________________________
# Test switch
def test_switch_initial_state(tenv: TEnv) -> None:
    assert not tenv.switch.state

def test_unexpected_runtime_error(tenv: TEnv) -> None:
    my_set = {1, 2, 3}
    rand_pause()
    my_list = []
    my_iterator = iter(my_set)

    while True:
        item = next(my_iterator)
        my_list.append(item)

    assert my_list

def test_switch_state_dropped_after_shock(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    tenv.microprocessor.analyze_rhythm()
    tenv.microprocessor.process_rhythm()
    assert not tenv.switch.state
