""" Setups the environment for the test case """

from devsure.tenv_setup import TEnvSetup, Find
from devsure.rpc.test.rpc_to_emul.emulator_rpc import EmulatorRpc


class TEnv(TEnvSetup):
    """ Setups the environment for the test case """

    title = "Test case that interacts with the emulator"
    comment = "Demonstrate basic RPC interaction with the emulator"

    emulator: EmulatorRpc = Find()
