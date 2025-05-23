*** Settings ***
Library    devsure.robot

*** Keywords ***
DCPowerSupply Get Voltage Limit
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.voltage_limit}

DCPowerSupply Set Voltage Limit
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.voltage_limit}=    Set Variable  ${value}

DCPowerSupply Get Current Limit
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.current_limit}

DCPowerSupply Set Current Limit
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.current_limit}=    Set Variable  ${value}

DCPowerSupply Get Voltage
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.voltage}

DCPowerSupply Get Current
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.current}

DCAdapter Get Input Voltage
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.input_voltage}

DCAdapter Get Input Current
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.input_current}

DCAdapter Get Output Voltage
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.output_voltage}

DCAdapter Get Output Current
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.output_current}

DCAdapter Get Connected Power Supply
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_power_supply}

DCAdapter Set Connected Power Supply
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_power_supply}=    Set Variable  ${value}

DCAdapter Get Bridge Rectifier Coefficient
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.bridge_rectifier_coefficient}

DCAdapter Get Efficiency
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.efficiency}

DCAdapter Get Power
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.power}

InflatableCuff Get Cuff Thickness
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.cuff_thickness}

InflatableCuff Get Cuff Area
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.cuff_area}

Pump Get Min Power
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.min_power}

Pump Get Connected Controller
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_controller}

Pump Set Connected Controller
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_controller}=    Set Variable  ${value}

Pump Get Connected Cuff
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_cuff}

Pump Set Connected Cuff
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_cuff}=    Set Variable  ${value}

Pump Pumping
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    pumping    @{args}
    RETURN             ${result}

Pump Get Pressure
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.pressure}

Pump Get Pressure Measurement
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.pressure_measurement}

BloodPressureMD Get Target Pressure
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.target_pressure}

BloodPressureMD Get Connected Power
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_power}

BloodPressureMD Set Connected Power
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_power}=    Set Variable  ${value}

BloodPressureMD Provide Power
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    provide_power    @{args}
    RETURN             ${result}
