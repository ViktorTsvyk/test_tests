from .tenv import TEnv
from .test_emulator_bpm import call_test


def test_emulator_loaded(tenv_func: TEnv):
    call_test(tenv_func)


def test_emulator_loaded_again(tenv_func: TEnv):
    call_test(tenv_func)
