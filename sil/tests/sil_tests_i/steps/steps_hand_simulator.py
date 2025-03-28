from pytest_bdd import when, parsers

from sil_tests_i.Core.assertions.Assertions import Assertions
from sil_tests_i.Core.context.context import Context

@when(parsers.parse("Turn {state} the valve"))
def click_button(context: Context, state):
    Assertions.assert_true(state in ("on", "off"), f"Unexpected state: {state}")
    is_break = state == "off"
    context.tenv.emulator._hand_simulator.break_pump(is_break)


#TODO
@when(parsers.cfparse("Set high pressure for hand simulator to {high_pressure}"))
def click_button(context: Context, high_pressure):
    context.tenv.emulator._hand_simulator.high_pressure(high_pressure)