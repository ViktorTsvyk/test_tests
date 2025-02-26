""" Setups the environment for the test case """
import time

from devsure.tenv_setup import TEnvSetup, Find
from devsure.rpc.test.rpc_to_bpm_emu.bpm_emulator_rpc import BpmEmulatorRpc


class TEnv(TEnvSetup):
    """ Setups the environment for the test case """

    title = "Test case that interacts with the emulator"
    comment = "Demonstrate basic RPC interaction with the emulator"

    emulator: BpmEmulatorRpc = Find()

    def tear_down(self):
        """ Shut down Emulator """
        try:
            self.emulator.mark_for_exit()
            self.emulator.emulator_stop_emulation()
            time.sleep(2)
        except Exception as e:
            print(f"tearDown exception {e}")
