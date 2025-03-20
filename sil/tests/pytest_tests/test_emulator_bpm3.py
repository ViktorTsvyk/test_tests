from .tenv import TEnv
from .test_emulator_bpm import call_test


def test_emulator_loaded(tenv: TEnv):
    call_test(tenv)
