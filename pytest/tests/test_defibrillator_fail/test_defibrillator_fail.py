""" 131 tests fail """
from .tenv import TEnv
import random
import time
from common_items.use_variables import *


# ---------------------------------------
def rand_pause():
    pause_sec = random.randint(0, 2)
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
    assert tenv.power_source.battery_level != 100.0


def test_normal_rhythm_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"

def test_normal_rhythm_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    bat_level = tenv.power_source.battery_level + COMMON_NUMBER
    assert bat_level == 100.0


def test_normal_rhythm_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"

# ______________________________________________
# Test ventricular fibrillation rhythm
def test_ventricular_fibrillation_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    assert tenv.power_source.battery_level == 100.0


def test_ventricular_fibrillation_capacitor_discharge(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage != 0.0

def test_ventricular_fibrillation_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    assert tenv.power_source.battery_level == 100.0


def test_ventricular_fibrillation_capacitor_discharge_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage == 1.0
# ______________________________________________
# Test pulseless ventricular tachycardia rhythm
def test_pulseless_ventricular_tachycardia_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level == 105.0


def test_pulseless_ventricular_tachycardia_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia without pulse"

def test_pulseless_ventricular_tachycardia_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    print(COMMON_STRING)
    assert tenv.power_source.battery_level < 1.0


def test_pulseless_ventricular_tachycardia_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia with pulse"
# ______________________________________________
# Test speaker
def test_speaker_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"


def test_speaker_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "No shock needed. Continue monitoring"


def test_speaker_not_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "Preparing to deliver shock. Touch the body!"

def test_speaker_initial_state_text(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"


def test_speaker_normal_rhythm_analyze_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction != "No shock needed. Continue monitoring..."


def test_speaker_not_normal_rhythm_analyze_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction != "Preparing to deliver shock. Do not touch the body!"

# ______________________________________________
# Test switch
def test_switch_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.switch.state


def test_switch_normal_rhythm_state(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    print(not_global_string)
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state


def test_switch_state_dropped_after_shock(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state

def test_switch_initial_state_text(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.switch.state


def test_switch_normal_rhythm_state_value(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state


def test_switch_state_dropped_after_shock_value(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state

# ______________________________________________
# Test normal rhythm
def test_smoke_normal_rhythm_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.power_source.battery_level != 100.0


def test_smoke_normal_rhythm_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"

def test_smoke_normal_rhythm_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.power_source.battery_level != 100.0


def test_smoke_normal_rhythm_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"

# ______________________________________________
# Test ventricular fibrillation rhythm
def test_smoke_ventricular_fibrillation_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    assert tenv.power_source.battery_level == 100.0


def test_smoke_ventricular_fibrillation_capacitor_discharge(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage != 0.0

def test_smoke_ventricular_fibrillation_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    assert tenv.power_source.battery_level == 100.0


def test_smoke_ventricular_fibrillation_capacitor_discharge_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage == 1.0
# ______________________________________________
# Test pulseless ventricular tachycardia rhythm
def test_smoke_pulseless_ventricular_tachycardia_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level == 105.0


def test_smoke_pulseless_ventricular_tachycardia_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia without pulse"

def test_smoke_pulseless_ventricular_tachycardia_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level < 1.0


def test_smoke_pulseless_ventricular_tachycardia_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia with pulse"
# ______________________________________________
# Test speaker
def test_smoke_speaker_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"


def test_smoke_speaker_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "No shock needed. Continue monitoring"


def test_smoke_speaker_not_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "Preparing to deliver shock. Touch the body!"

def test_smoke_speaker_initial_state_text(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"


def test_smoke_speaker_normal_rhythm_analyze_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction != "No shock needed. Continue monitoring..."


def test_smoke_speaker_not_normal_rhythm_analyze_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction != "Preparing to deliver shock. Do not touch the body!"

# ______________________________________________
# Test switch
def test_smoke_switch_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.switch.state


def test_smoke_switch_normal_rhythm_state(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state


def test_smoke_switch_state_dropped_after_shock(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state

def test_smoke_switch_initial_state_text(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.switch.state


def test_smoke_switch_normal_rhythm_state_value(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state


def test_smoke_switch_state_dropped_after_shock_value(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state


# ______________________________________________
# Test normal rhythm
def test_regression_normal_rhythm_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.power_source.battery_level != 100.0


def test_regression_normal_rhythm_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"


def test_regression_normal_rhythm_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.power_source.battery_level != 100.0


def test_regression_normal_rhythm_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"


# ______________________________________________
# Test ventricular fibrillation rhythm
def test_regression_ventricular_fibrillation_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    assert tenv.power_source.battery_level == 100.0


def test_regression_ventricular_fibrillation_capacitor_discharge(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage != 0.0


def test_regression_ventricular_fibrillation_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    assert tenv.power_source.battery_level == 100.0


def test_regression_ventricular_fibrillation_capacitor_discharge_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage == 1.0


# ______________________________________________
# Test pulseless ventricular tachycardia rhythm
def test_regression_pulseless_ventricular_tachycardia_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level == 105.0


def test_regression_pulseless_ventricular_tachycardia_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia without pulse"


def test_regression_pulseless_ventricular_tachycardia_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level < 1.0


def test_regression_pulseless_ventricular_tachycardia_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia with pulse"


# ______________________________________________
# Test speaker
def test_regression_speaker_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"


def test_regression_speaker_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "No shock needed. Continue monitoring"


def test_regression_speaker_not_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "Preparing to deliver shock. Touch the body!"


def test_regression_speaker_initial_state_text(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"


def test_regression_speaker_normal_rhythm_analyze_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction != "No shock needed. Continue monitoring..."


def test_regression_speaker_not_normal_rhythm_analyze_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction != "Preparing to deliver shock. Do not touch the body!"


# ______________________________________________
# Test switch
def test_regression_switch_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.switch.state


def test_regression_switch_normal_rhythm_state(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state


def test_regression_switch_state_dropped_after_shock(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state


def test_regression_switch_initial_state_text(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.switch.state


def test_regression_switch_normal_rhythm_state_value(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state


def test_regression_switch_state_dropped_after_shock_value(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state


# ______________________________________________
# Test normal rhythm
def test_regression_smoke_normal_rhythm_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.power_source.battery_level != 100.0


def test_regression_smoke_normal_rhythm_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"


def test_regression_smoke_normal_rhythm_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.power_source.battery_level != 100.0


def test_regression_smoke_normal_rhythm_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"

def test_alpha_speaker_not_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "Preparing to deliver shock. Touch the body!"


def test_alpha_speaker_initial_state_text(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"


def test_alpha_speaker_normal_rhythm_analyze_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction != "No shock needed. Continue monitoring..."


def test_alpha_speaker_not_normal_rhythm_analyze_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction != "Preparing to deliver shock. Do not touch the body!"

def test_fix_normal_rhythm_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.power_source.battery_level != 100.0


def test_fix_normal_rhythm_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"

def test_fix_normal_rhythm_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.power_source.battery_level != 100.0


def test_fix_normal_rhythm_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"

# ______________________________________________
# Test ventricular fibrillation rhythm
def test_fix_ventricular_fibrillation_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    assert tenv.power_source.battery_level == 100.0


def test_fix_ventricular_fibrillation_capacitor_discharge(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage != 0.0

def test_fix_ventricular_fibrillation_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    assert tenv.power_source.battery_level == 100.0


def test_fix_ventricular_fibrillation_capacitor_discharge_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage == 1.0
# ______________________________________________
# Test pulseless ventricular tachycardia rhythm
def test_fix_pulseless_ventricular_tachycardia_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level == 105.0


def test_fix_pulseless_ventricular_tachycardia_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia without pulse"

def test_fix_pulseless_ventricular_tachycardia_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level < 1.0


def test_fix_pulseless_ventricular_tachycardia_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia with pulse"
# ______________________________________________
# Test speaker
def test_fix_speaker_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"


def test_fix_speaker_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "No shock needed. Continue monitoring"


def test_fix_speaker_not_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "Preparing to deliver shock. Touch the body!"

def test_fix_speaker_initial_state_text(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"


def test_fix_speaker_normal_rhythm_analyze_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction != "No shock needed. Continue monitoring..."


def test_fix_speaker_not_normal_rhythm_analyze_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction != "Preparing to deliver shock. Do not touch the body!"

# ______________________________________________
# Test switch
def test_fix_switch_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.switch.state


def test_fix_switch_normal_rhythm_state(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state


def test_fix_switch_state_dropped_after_shock(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state

def test_fix_switch_initial_state_text(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.switch.state


def test_fix_switch_normal_rhythm_state_value(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state


def test_fix_switch_state_dropped_after_shock_value(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    assert tenv.switch.state

# ______________________________________________
# Test normal rhythm
def test_update_normal_rhythm_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.power_source.battery_level != 100.0


def test_update_normal_rhythm_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"

def test_update_normal_rhythm_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.power_source.battery_level != 100.0


def test_update_normal_rhythm_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    rand_pause()
    assert rhythm_status != "Normal rhythm"

# ______________________________________________
# Test ventricular fibrillation rhythm
def test_update_ventricular_fibrillation_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    assert tenv.power_source.battery_level == 100.0


def test_update_ventricular_fibrillation_capacitor_discharge(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage != 0.0

def test_update_ventricular_fibrillation_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    assert tenv.power_source.battery_level == 100.0


def test_update_ventricular_fibrillation_capacitor_discharge_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage == 1.0
# ______________________________________________
# Test pulseless ventricular tachycardia rhythm
def test_update_pulseless_ventricular_tachycardia_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level == 105.0


def test_update_pulseless_ventricular_tachycardia_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia without pulse"

def test_update_pulseless_ventricular_tachycardia_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level < 1.0


def test_update_pulseless_ventricular_tachycardia_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia with pulse"
# ______________________________________________
# Test speaker
def test_update_speaker_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"


def test_update_speaker_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "No shock needed. Continue monitoring"


def test_update_speaker_not_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "Preparing to deliver shock. Touch the body!"

def test_update_speaker_initial_state_text(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"

def test_n_a_ventricular_fibrillation_capacitor_discharge(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage != 0.0

def test_n_a_ventricular_fibrillation_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(VENTRICULAR_FIBRILLATION)
    assert tenv.power_source.battery_level == 100.0


def test_n_a_ventricular_fibrillation_capacitor_discharge_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(NORMAL_RHYTHM)
    rand_pause()
    assert tenv.capacitor.charge_voltage == 1.0
# ______________________________________________
# Test pulseless ventricular tachycardia rhythm
def test_n_a_pulseless_ventricular_tachycardia_battery(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level == 105.0


def test_n_a_pulseless_ventricular_tachycardia_microprocessor_status(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia without pulse"

def test_n_a_pulseless_ventricular_tachycardia_battery_level(tenv: TEnv) -> None:
    tenv.defibrillator.defibrillate(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    assert tenv.power_source.battery_level < 1.0


def test_n_a_pulseless_ventricular_tachycardia_microprocessor_status_text(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(PULSELESS_VENTRICULAR_TACHYCARDIA)
    rand_pause()
    rhythm_status = tenv.microprocessor.analyze_rhythm()
    assert rhythm_status == "Tachycardia with pulse"
# ______________________________________________
# Test speaker
def test_n_a_speaker_initial_state(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"


def test_n_a_speaker_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(NORMAL_RHYTHM)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "No shock needed. Continue monitoring"


def test_n_a_speaker_not_normal_rhythm_analyze(tenv: TEnv) -> None:
    tenv.electrodes.detect_heart_rhythm(VENTRICULAR_FIBRILLATION)
    tenv.microprocessor.analyze_rhythm()
    rand_pause()
    tenv.microprocessor.process_rhythm()
    rand_pause()
    assert tenv.speaker.instruction == "Preparing to deliver shock. Touch the body!"

def test_n_a_speaker_initial_state_text(tenv: TEnv) -> None:
    rand_pause()
    assert tenv.speaker.instruction == "Awaiting instructions"
