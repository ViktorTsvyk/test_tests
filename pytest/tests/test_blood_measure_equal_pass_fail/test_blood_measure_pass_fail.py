""" 104 tests fail, 104 tests pass """

import pytest
import random
import time
from .tenv import TEnv
from common_items.use_function import increase_value, return_value
from common_items.use_variables import not_global_dict


# ---------------------------------------
def rand_pause():
    pause_sec = random.randint(0, 3)
    time.sleep(pause_sec)


# ---------------------------------------

def test_additional_pressure(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    add_value = return_value(additional_pump_pressure)
    assert add_value < 0


def test_pressure_inside_cuff(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure - additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_cuff_connection_negative(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Inflatable Cuff is connected"

def test_cuff_connection_negative_func(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Inflatable Cuff is not connected"

def test_pressure_in_cuff_more_then_additional(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement > tenv.pump.pumping()


def test_pressure_in_cuff_more_then_additional_v(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement < tenv.pump.pumping()


def test_power_adapter_efficiency(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency <= 0.2  # 0.8 was to demonstrate failure


def test_cuff_thickness(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness == 0


def test_minimum_power_pump(tenv: TEnv):
    min_power = tenv.pump.min_power
    new_power = increase_value(min_power)# 0.1
    rand_pause()
    print(f"Pump minimum power value: {new_power}")
    assert new_power > 0.2


def test_blood_pressure_md_connected_power_class(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert not cls.startswith("DCAdapter")


def test_power_source_current_limit(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [7.0, 6.7, 6.3]


def test_connected_power_supply_class(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[3]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSupply"


def test_power_source_voltage_limit(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [240.5, 240.6, 241.7]


def test_bridge_rectifier_coefficient(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient == 1.5673423236456


def test_additional_pressure_value(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure > 565


def test_pressure_inside_cuff_value(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure + additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_cuff_connection_negative_msg(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Inflatable Cuff not connected"


def test_pressure_in_cuff_more_then_additional_value(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement < tenv.pump.pumping()


def test_power_adapter_efficiency_value(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    print(f"{not_global_dict}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 15


def test_cuff_thickness_value(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness == 0


def test_minimum_power_pump_value(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power == 0.2


def test_blood_pressure_md_connected_power_class_value(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("PCAdapter")


def test_power_source_current_limit_value(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [16.0, 16.1, 16.2]


def test_connected_power_supply_class_value(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPower"


def test_power_source_voltage_limit_value(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [340.0, 340.1, 341.2]


def test_bridge_rectifier_coefficient_value(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient <= 0.5673423236456


def test_additional_pressure_measurement(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure > 783.0


def test_pressure_inside_cuff_measurement(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure - additional_pump_pressure) == 567.3


def test_cuff_connection_negative_message(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Cuff is not connected"


def test_pressure_in_cuff_more_then_additional_measurement(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement < tenv.pump.pumping()


def test_power_adapter_efficiency_measurement(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency < 0.2  # 0.8 was to demonstrate failure


def test_cuff_thickness_measurement(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness < 0


def test_minimum_power_pump_measurement(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power > 0.4


def test_blood_pressure_md_connected_power_class_name(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("DCAdapter")


def test_power_source_current_limit_measurement(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit not in [6.0, 6.1, 6.2]


def test_connected_power_supply_class_name(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSup"


def test_power_source_voltage_limit_measurement(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit not in [240.0, 240.1, 241.2]


def test_bridge_rectifier_coefficient_measurement(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient == 1.5673423236456


def test_pump_additional_pressure(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure == 0


def test_pump_pressure_inside_cuff(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure - additional_pump_pressure) > tenv.blood_pressure_md.target_pressure


def test_cuff_device_connection_negative(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Inflatable Cuff is connected"


def test_pump_pressure_in_cuff_more_then_additional(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement < tenv.pump.pumping()


def test_power_adapter_device_efficiency(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency == 1.2  # 0.8 was to demonstrate failure


def test_cuff_device_thickness(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness < 0


def test_minimum_power_pump_device(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power > 0.2


def test_blood_pressure_md_device_connected_power_class(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[2]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("PowerAdapter")


def test_source_current_limit(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit not in [6.0, 6.1, 6.2]


def test_power_supply_class(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls != "DCPowerSupply"


def test_source_voltage_limit(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit not in [240.0, 240.1, 241.2]


def test_bridge_rectifier_coeff(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient == 1.5673423236456


def test_additional_pressure_calc(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure < 0


def test_pressure_inside_cuff_calc(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure + additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_cuff_connection_negative_calc(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) != "Inflatable Cuff is not connected"


def test_pressure_in_cuff_more_then_additional_calc(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement < tenv.pump.pumping()


def test_power_adapter_efficiency_calc(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency < 0.2  # 0.8 was to demonstrate failure


def test_cuff_thickness_calc(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness < 0


def test_minimum_power_pump_calc(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power > 0.2


def test_blood_pressure_md_connected_power_class_title(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("DCAdapter")


def test_power_source_current_limit_calc(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit not in [6.0, 6.1, 6.2]


def test_connected_power_supply_class_title(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[0]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSupply"


def test_power_source_voltage_limit_calc(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [540.0, 540.1, 541.2]


def test_bridge_rectifier_coefficient_calc(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient == 5.5673423236456


def test_bridge_rectifier_coef(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.4142135623730951


def test_additional_pressure_calculation(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure > 999.9


def test_pressure_inside_cuff_calculation(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure + additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_cuff_connection_negative_calculation(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) != "Inflatable Cuff is not connected"


def test_pressure_in_cuff_more_then_additional_calculation(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement < tenv.pump.pumping()


def test_power_adapter_efficiency_calculation(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency < 0.2  # 0.8 was to demonstrate failure


def test_cuff_thickness_calculation(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness < 0


def test_minimum_power_pump_calculation(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power > 0.2


def test_blood_pressure_md_connected_power_class_val(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCAdapter"


def test_power_source_current_limit_calculation(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [9.0, 9.1, 9.2]


def test_connected_power_supply_class_val(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls != "DCPowerSupply"


def test_power_source_voltage_limit_calculation(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit not in [240.0, 240.1, 241.2]


def test_bridge_rectifier_coefficient_calculation(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient == 1.5673423236456


def test_additional_pressure_of_pump(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure == 0


def test_pressure_in_cuff(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure * additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_for_cuff_connection_negative(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Cuff is not connected"


def test_pressure_inside_cuff_more_then_additional(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement > (tenv.pump.pumping() + 300)


def test_adapter_efficiency(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 112.2  # 0.8 was to demonstrate failure


def test_for_cuff_thickness(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness > 786


def test_min_power_pump_calculation(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power > 0.35


def test_blood_pressure_md_connected_power_val(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert not cls.startswith("DCAdapter")


def test_source_current_limit_calculation(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit not in [6.0, 6.1, 6.2]


def test_power_supply_class_val(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls != "DCPowerSupply"


def test_source_voltage_limit_calculation(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit not in [240.0, 240.1, 241.2]


def test_bridge_rect_coefficient_calculation(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.4142135623730951


def test_additional_pressure_in_pump(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert (additional_pump_pressure * 0) > 0


def test_pressure_of_cuff(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure - additional_pump_pressure) != tenv.blood_pressure_md.target_pressure


def test_device_cuff_connection_negative(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) != "Inflatable Cuff is not connected"


def test_pressure_in_cuff_device_more_then_additional(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement < tenv.pump.pumping()


def test_power_adapter_device_efficiency_val(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 345.2  # 0.8 was to demonstrate failure


def test_for_cuff_device_thickness(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness > 1094


def test_min_power_pump_device_calculation(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power < 0.0000000001


def test_blood_pressure_md_device_connected_power_val(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCAdapterSigilent"


def test_power_source_device_current_limit_calculation(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [66.0, 66.1, 66.2]


def test_power_supply_device_class_val(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls != "DCPowerSupply"


def test_power_source_device_voltage_limit_calculation(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [245.0, 245.1, 245.2]


def test_power_adapter_bridge_rect_coefficient_calculation(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient == 1.5673423236456


def test_for_cuff_device_thickness_val(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness == 0


def test_min_power_pump_device_calculation_info(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power == 0.3


def test_blood_pressure_md_device_connected_power_value(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("DCAdapter")


def test_power_adapter_efficiency_sec(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 0.2  # 0.8 was to demonstrate failure


def test_cuff_thickness_sec(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness > 0


def test_minimum_power_pump_sec(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power < 0.2


def test_blood_pressure_md_connected_power_class_smoke(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("DCAdapter")


def test_power_source_current_limit_smoke(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [6.0, 6.1, 6.2]


def test_connected_power_supply_class_smoke(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSupply"


def test_power_source_voltage_limit_smoke(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [240.0, 240.1, 241.2]


def test_bridge_rectifier_coefficient_smoke(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.5673423236456


def test_additional_pressure_value_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure > 0


def test_pressure_inside_cuff_value_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure - additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_cuff_connection_negative_msg_smoke(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Inflatable Cuff is not connected"


def test_pressure_in_cuff_more_then_additional_value_smoke(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement > tenv.pump.pumping()


def test_power_adapter_efficiency_value_smoke(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 0.2  # 0.8 was to demonstrate failure


def test_cuff_thickness_value_smoke(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness > 0


def test_minimum_power_pump_value_smoke(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power < 0.2


def test_blood_pressure_md_connected_power_class_value_smoke(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("Triceratops")


def test_power_source_current_limit_value_smoke(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [6.0, 6.1, 6.2]


def test_connected_power_supply_class_value_smoke(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSupply"


def test_power_source_voltage_limit_value_smoke(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [240.0, 240.1, 241.2]


def test_bridge_rectifier_coefficient_value_smoke(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.5673423236456


def test_additional_pressure_measurement_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure > 0


def test_pressure_inside_cuff_measurement_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure - additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_cuff_connection_negative_message_smoke(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Inflatable Cuff is not connected"


def test_pressure_in_cuff_more_then_additional_measurement_smoke(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement > tenv.pump.pumping()


def test_power_adapter_efficiency_measurement_smoke(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 0.2  # 0.8 was to demonstrate failure


def test_cuff_thickness_measurement_smoke(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness > 0


def test_minimum_power_pump_measurement_smoke(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power < 0.2


def test_blood_pressure_md_connected_power_class_name_smoke(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("DCAdapter")


def test_power_source_current_limit_measurement_smoke(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [6.0, 6.1, 6.2]


def test_connected_power_supply_class_name_smoke(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSupply"


def test_power_source_voltage_limit_measurement_smoke(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [240.0, 240.1, 241.2]


def test_bridge_rectifier_coefficient_measurement_smoke(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.5673423236456


def test_pump_additional_pressure_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure > 0


def test_pump_pressure_inside_cuff_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure + additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_pump_pressure_in_cuff_more_then_additional_smoke(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement > tenv.pump.pumping()


def test_power_adapter_device_efficiency_smoke(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 0.2  # 0.8 was to demonstrate failure


def test_cuff_device_thickness_smoke(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness > 0


def test_minimum_power_pump_device_smoke(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power < 0.2


def test_blood_pressure_md_device_connected_power_class_smoke(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert not cls.startswith("DCAdapter")


def test_source_current_limit_smoke(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [6.0, 6.1, 6.2]


def test_power_supply_class_smoke(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSupply"


def test_source_voltage_limit_smoke(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [240.0, 240.1, 241.2]


def test_bridge_rectifier_coeff_smoke(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.5673423236456


def test_additional_pressure_calc_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure > 0


def test_pressure_inside_cuff_calc_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure - additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_cuff_connection_negative_calc_smoke(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Inflatable Cuff is not connected"


def test_pressure_in_cuff_more_then_additional_calc_smoke(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement > tenv.pump.pumping()


def test_power_adapter_efficiency_calc_smoke(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 0.2  # 0.8 was to demonstrate failure


def test_cuff_thickness_calc_smoke(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness > 0


def test_minimum_power_pump_calc_smoke(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power < 0.2


def test_blood_pressure_md_connected_power_class_title_smoke(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("DCAdapter")


def test_power_source_current_limit_calc_smoke(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [6.0, 6.1, 6.2]


def test_connected_power_supply_class_title_smoke(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSupply"


def test_power_source_voltage_limit_calc_smoke(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [240.0, 240.1, 241.2]


def test_bridge_rectifier_coefficient_calc_smoke(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.5673423236456


def test_bridge_rectifier_coef_smoke(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.5673423236456


def test_additional_pressure_calculation_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure > 0


def test_pressure_inside_cuff_calculation_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure - additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_cuff_connection_negative_calculation_smoke(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Inflatable Cuff is not connected"


def test_pressure_in_cuff_more_then_additional_calculation_smoke(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement > tenv.pump.pumping()


def test_power_adapter_efficiency_calculation_smoke(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 0.2  # 0.8 was to demonstrate failure


def test_cuff_thickness_calculation_smoke(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness > 0


def test_minimum_power_pump_calculation_smoke(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power < 0.2


def test_blood_pressure_md_connected_power_class_val_smoke(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("DCAdapter")


def test_power_source_current_limit_calculation_smoke(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [6.0, 6.1, 6.2]


def test_connected_power_supply_class_val_smoke(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSupply"


def test_power_source_voltage_limit_calculation_smoke(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [240.0, 240.1, 241.2]


def test_bridge_rectifier_coefficient_calculation_smoke(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.5673423236456


def test_additional_pressure_of_pump_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure > 0


def test_pressure_in_cuff_smoke(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure - additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_for_cuff_connection_negative_smoke(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Inflatable Cuff is not connected"


def test_pressure_inside_cuff_more_then_additional_smoke(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement > tenv.pump.pumping()


def test_adapter_efficiency_smoke(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 0.2  # 0.8 was to demonstrate failure


def test_for_cuff_thickness_regression(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness > 0


def test_min_power_pump_calculation_regression(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power < 0.2


def test_blood_pressure_md_connected_power_val_regression(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("DCAdapter")


def test_source_current_limit_calculation_regression(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [6.0, 6.1, 6.2]


def test_power_supply_class_val_regression(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSupply"


def test_source_voltage_limit_calculation_regression(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [240.0, 240.1, 241.2]


def test_bridge_rect_coefficient_calculation_regression(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.5673423236456


def test_additional_pressure_in_pump_regression(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    assert additional_pump_pressure > 0


def test_pressure_of_cuff_regression(tenv: TEnv) -> None:
    additional_pump_pressure = tenv.pump.pumping()
    rand_pause()
    print(f"Additional pump pressure is {additional_pump_pressure}")
    result_pressure = tenv.pump.pressure.measurement
    rand_pause()
    print(f"Pressure inside the cuff is {result_pressure}")
    assert (result_pressure - additional_pump_pressure) == tenv.blood_pressure_md.target_pressure


def test_device_cuff_connection_negative_regression(tenv: TEnv) -> None:
    tenv.pump._cuff = None
    rand_pause()
    with pytest.raises(ValueError) as exc_info:
        # noinspection PyCallingNonCallable
        tenv.pump.connected_cuff()
    assert str(exc_info.value) == "Inflatable Cuff is not connected"


def test_pressure_in_cuff_device_more_then_additional_regression(tenv: TEnv):
    rand_pause()
    print(f"Pressure measurement: {tenv.pump.pressure.measurement}")
    assert tenv.pump.pressure.measurement > tenv.pump.pumping()


def test_power_adapter_device_efficiency_val_regression(tenv: TEnv):
    efficiency = tenv.power_adapter.efficiency
    print(f"Power adapter efficiency: {efficiency}")
    rand_pause()
    # Expected efficiency is 80% or more
    assert efficiency >= 0.2  # 0.8 was to demonstrate failure


def test_for_cuff_device_thickness_regression(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness > 0


def test_min_power_pump_device_calculation_regression(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power < 0.2


def test_blood_pressure_md_device_connected_power_val_regression(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("DCAdapter")


def test_power_source_device_current_limit_calculation_regression(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [6.0, 6.1, 6.2]


def test_power_supply_device_class_val_regression(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSupply"


def test_power_source_device_voltage_limit_calculation_regression(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [240.0, 240.1, 241.2]


def test_power_adapter_bridge_rect_coefficient_calculation_regression(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.5673423236456


def test_for_cuff_device_thickness_val_regression(tenv: TEnv):
    thickness = tenv.cuff.cuff_thickness
    print(f"Cuff thickness value: {thickness}")
    rand_pause()
    assert thickness > 0


def test_min_power_pump_device_calculation_info_regression(tenv: TEnv):
    min_power = tenv.pump.min_power  # 0.1
    rand_pause()
    print(f"Pump minimum power value: {min_power}")
    assert min_power < 0.2


def test_blood_pressure_md_device_connected_power_value_regression(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("DCAdapter")


def test_power_source_device_current_limit_calc_info(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit in [6.0, 6.1, 6.2]


def test_power_supply_device_class_value(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls == "DCPowerSupply"


def test_power_source_device_voltage_limit_calc(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit in [240.0, 240.1, 241.2]


def test_power_adapter_bridge_rect_coefficient_calc(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient != 1.5673423236456


def test_power_source_device_current_limit_calc_info_regression(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit not in [6.0, 6.1, 6.2]


def test_power_supply_device_class_value_regression(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls != "DCPowerSupply"


def test_power_source_device_voltage_limit_calc_regression(tenv: TEnv):
    voltage_limit = tenv.power_source.voltage_limit
    rand_pause()
    print(f"Power source current limit is: {voltage_limit}")
    assert voltage_limit not in [240.0, 240.1, 241.2]


def test_power_adapter_bridge_rect_coefficient_calc_regression(tenv: TEnv):
    bridge_rectifier_coefficient = tenv.power_adapter.bridge_rectifier_coefficient  # 1.4142135623730951
    print(f"Power adapter bridge rectifier coefficient is: {bridge_rectifier_coefficient}")
    rand_pause()
    assert bridge_rectifier_coefficient == 1.5673423236456


def test_blood_pressure_connected_power_val(tenv: TEnv):
    power_class = str(tenv.blood_pressure_md.connected_power)
    class_values = power_class.split(" ")
    rand_pause()
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls.startswith("DCAdapter")


def test_source_current_limit_calculation_result_in(tenv: TEnv):
    current_limit = tenv.power_source.current_limit
    rand_pause()
    print(f"Power source current limit is: {current_limit}")
    assert current_limit not in [6.0, 6.1, 6.2]


def test_power_supply_class_title_correct(tenv: TEnv):
    power_supply_class = str(tenv.power_adapter.connected_power_supply)
    rand_pause()
    class_values = power_supply_class.split(" ")
    items = class_values[0].split(".")
    cls = items[4]
    rand_pause()
    print(f"Connected power class is: {cls}")
    assert cls != "DCPowerSupply"
