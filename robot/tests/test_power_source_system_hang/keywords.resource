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

DCMotor Get Nominal Voltage
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.nominal_voltage}

DCMotor Get Nominal Torque Nm
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.nominal_torque_nm}

DCMotor Get Nominal Omega
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.nominal_omega}

DCMotor Get Connected Power Supply
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_power_supply}

DCMotor Set Connected Power Supply
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_power_supply}=    Set Variable  ${value}

DCMotor Get Load Torque
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.load_torque}

DCMotor Set Load Torque
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.load_torque}=    Set Variable  ${value}

DCMotor Get Nominal Power
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.nominal_power}

DCMotor Get Over Voltage Detected
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.over_voltage_detected}

DCMotor Get Over Current Detected
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.over_current_detected}

DCMotor Get Current
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.current}

DCMotor Get Omega Now
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.omega_now}

DCMotor Get Power
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.power}

Ventilator Get Heat Coefficient
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.heat_coefficient}

Ventilator Get Pressure Coefficient
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.pressure_coefficient}

Ventilator Get Connected Power
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_power}

Ventilator Set Connected Power
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_power}=    Set Variable  ${value}

Ventilator Get Heat
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.heat}

Ventilator Get Heat Measurement
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.heat_measurement}

Ventilator Get Pressure
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.pressure}

Ventilator Get Pressure Measurement
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.pressure_measurement}

ADCVoltage Get Connected Measurement
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_measurement}

ADCVoltage Set Connected Measurement
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_measurement}=    Set Variable  ${value}

ADCVoltage Voltage
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    voltage    @{args}
    RETURN             ${result}

ADCAmpere Get Connected Measurement
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_measurement}

ADCAmpere Set Connected Measurement
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_measurement}=    Set Variable  ${value}

ADCAmpere Current
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    current    @{args}
    RETURN             ${result}

TemperatureFromVolts Get Coefficient
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.coefficient}

TemperatureFromVolts Get Connected Voltage
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_voltage}

TemperatureFromVolts Set Connected Voltage
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_voltage}=    Set Variable  ${value}

TemperatureFromVolts Get Measurement
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.measurement}

PressureFromAmperes Get Coefficient
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.coefficient}

PressureFromAmperes Get Connected Ampere
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_ampere}

PressureFromAmperes Set Connected Ampere
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_ampere}=    Set Variable  ${value}

PressureFromAmperes Get Measurement
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.measurement}
