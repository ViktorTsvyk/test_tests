from devsure.time_simulator.simulation import simulated_sleep_ms

from .tenv import TEnv
from .test_emulator_bpm import call_test


def test_emulator_loaded(tenv: TEnv):
    call_test(tenv)


def test_emulator_something(tenv: TEnv):
    simulated_sleep_ms(300)

    assert tenv.emulator.display_refreshes > 0, "There shall be display refreshes in test"
