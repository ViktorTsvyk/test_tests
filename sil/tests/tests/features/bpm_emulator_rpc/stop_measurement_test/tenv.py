from devsure.tenv_setup import TEnvSetup, Find
from devsure.rpc.test.rpc_to_bpm_emu.bpm_emulator_rpc import BpmEmulatorRpc


class TEnv(TEnvSetup):
    emulator: BpmEmulatorRpc = Find()
