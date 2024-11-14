*** Settings ***
Library    %{VIRTUAL_ENV}/../devsure/robot_tools/EnvironmentLibrary.py      AS      EL
Library    %{VIRTUAL_ENV}/../devsure/robot_tools/DynamicDeviceLibrary.py    AS      DEVICES

*** Keywords ***
DCPowerSupply Get Voltage Limit
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    voltage_limit
    RETURN             ${result}

DCPowerSupply Get Current Limit
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    current_limit
    RETURN             ${result}

DCPowerSupply Get Voltage
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    voltage
    RETURN             ${result}

DCPowerSupply Get Current
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    current
    RETURN             ${result}

DCPowerSupply Set Voltage Limit
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    voltage_limit    @{args}

DCPowerSupply Set Current Limit
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    current_limit    @{args}

DCAdapter Get Input Voltage
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    input_voltage
    RETURN             ${result}

DCAdapter Get Input Current
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    input_current
    RETURN             ${result}

DCAdapter Get Output Voltage
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    output_voltage
    RETURN             ${result}

DCAdapter Get Output Current
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    output_current
    RETURN             ${result}

DCAdapter Get Connected Power Supply
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_power_supply
    RETURN             ${result}

DCAdapter Get Bridge Rectifier Coefficient
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    bridge_rectifier_coefficient
    RETURN             ${result}

DCAdapter Get Efficiency
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    efficiency
    RETURN             ${result}

DCAdapter Get Power
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    power
    RETURN             ${result}

DCAdapter Set Connected Power Supply
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_power_supply    @{args}

InflatableCuff Get Cuff Thickness
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    cuff_thickness
    RETURN             ${result}

InflatableCuff Get Cuff Area
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    cuff_area
    RETURN             ${result}

Pump Get Min Power
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    min_power
    RETURN             ${result}

Pump Get Connected Controller
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_controller
    RETURN             ${result}

Pump Get Connected Cuff
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_cuff
    RETURN             ${result}

Pump Get Pressure Measurement
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${mid_result} =    EL.Get Property    ${instance}    pressure
    ${result} =        Set Variable    ${mid_result.measurement}
    RETURN             ${result}

Pump Get Pressure
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    pressure
    RETURN             ${result}

Pump Set Connected Controller
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_controller    @{args}

Pump Set Connected Cuff
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_cuff    @{args}

Pump Pumping
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    pumping    @{args}
    RETURN             ${result}

BloodPressureMD Get Target Pressure
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    target_pressure
    RETURN             ${result}

BloodPressureMD Get Connected Power
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_power
    RETURN             ${result}

BloodPressureMD Set Connected Power
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_power    @{args}

BloodPressureMD Provide Power
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    provide_power    @{args}
    RETURN             ${result}

