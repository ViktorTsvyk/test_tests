""" Setups the environment for the test case """
import time

from devsure.tenv_setup import Create, TEnvSetup, Find
from devsure.rpc.test.rpc_to_bpm_emu.bpm_emulator_rpc import BpmEmulatorRpc
from devsure.web.ui import ViewBase
from flask import Blueprint, render_template


class View(ViewBase):
    tenv: 'TEnv'

    name = "test_bpm"

    blueprint = Blueprint(name, __name__, template_folder="static", static_folder="static", url_prefix="/" + name)

    def index(self):
        return render_template(
            "index.html",
            form=self.tenv.emulator.Form(),
            form_second=self.tenv.emulator_second.Form(),
        )


class TEnv(TEnvSetup):
    """ Setups the environment for the test case """

    title = "Test case that interacts with the emulators"
    comment = "Demonstrate basic RPC & Web UI interactions with the emulators"

    emulator: BpmEmulatorRpc = Find()
    emulator_second: BpmEmulatorRpc = Find()

    view: View = Create()
