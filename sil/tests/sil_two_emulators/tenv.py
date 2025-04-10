""" Setups the environment for the test case """
from devsure.tenv_setup import TEnvSetup, Find
from devsure.rpc.test.rpc_to_bpm_emu.bpm_emulator_rpc import BpmEmulatorRpc


class TEnv(TEnvSetup):
    """ Setups the environment for the test case """

    title = "Test case that interacts with the emulators"
    comment = "Demonstrate basic RPC & Web UI interactions with the emulators"

    emulator: BpmEmulatorRpc = Find()
    emulator_second: BpmEmulatorRpc = Find()
