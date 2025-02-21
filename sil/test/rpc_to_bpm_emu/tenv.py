""" Setups the environment for the test case """

from devsure.tenv_setup import TEnvSetup, Find
from .bpm_emulator_rpc import BpmEmulatorRpc


class TEnv(TEnvSetup):
    """ Setups the environment for the test case """

    title = "Test case that interacts with the emulator"
    comment = "Demonstrate basic RPC interaction with the emulator"

    emulator: BpmEmulatorRpc = Find()
