""" Setups the environment for the test case """
from devsure.tenv_setup import TEnvSetup, Find
from devsure.rpc.test.rpc_to_bpm_emu.bpm_emulator_rpc import BpmEmulatorRpc


class TEnv(TEnvSetup):
    """ Setups the environment for the test case """

    title = "Blood pressure measurement Negative"
    comment = "Testing timeout on cuff inflation"

    emulator: BpmEmulatorRpc = Find()
