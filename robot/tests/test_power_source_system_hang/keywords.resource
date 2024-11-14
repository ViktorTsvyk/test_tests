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

DCMotor Get Nominal Voltage
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    nominal_voltage
    RETURN             ${result}

DCMotor Get Nominal Torque Nm
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    nominal_torque_nm
    RETURN             ${result}

DCMotor Get Nominal Omega
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    nominal_omega
    RETURN             ${result}

DCMotor Get Connected Power Supply
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_power_supply
    RETURN             ${result}

DCMotor Get Load Torque
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    load_torque
    RETURN             ${result}

DCMotor Get Nominal Power
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    nominal_power
    RETURN             ${result}

DCMotor Get Over Voltage Detected
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    over_voltage_detected
    RETURN             ${result}

DCMotor Get Over Current Detected
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    over_current_detected
    RETURN             ${result}

DCMotor Get Current
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    current
    RETURN             ${result}

DCMotor Get Omega Now
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    omega_now
    RETURN             ${result}

DCMotor Get Power
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    power
    RETURN             ${result}

DCMotor Set Connected Power Supply
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_power_supply    @{args}

DCMotor Set Load Torque
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    load_torque    @{args}

Ventilator Get Heat Coefficient
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    heat_coefficient
    RETURN             ${result}

Ventilator Get Pressure Coefficient
    [Documentation]    Attribute
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Attribute    ${instance}    pressure_coefficient
    RETURN             ${result}

Ventilator Get Connected Power
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_power
    RETURN             ${result}

Ventilator Get Heat Measurement
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${mid_result} =    EL.Get Property    ${instance}    heat
    ${result} =        Set Variable    ${mid_result.measurement}
    RETURN             ${result}

Ventilator Get Heat
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    heat
    RETURN             ${result}

Ventilator Get Pressure Measurement
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${mid_result} =    EL.Get Property    ${instance}    pressure
    ${result} =        Set Variable    ${mid_result.measurement}
    RETURN             ${result}

Ventilator Get Pressure
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    pressure
    RETURN             ${result}

Ventilator Set Connected Power
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_power    @{args}

ADCVoltage Get Connected Measurement
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_measurement
    RETURN             ${result}

ADCVoltage Set Connected Measurement
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_measurement    @{args}

ADCVoltage Voltage
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    voltage    @{args}
    RETURN             ${result}

ADCAmpere Get Connected Measurement
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_measurement
    RETURN             ${result}

ADCAmpere Set Connected Measurement
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_measurement    @{args}

ADCAmpere Current
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    current    @{args}
    RETURN             ${result}

TemperatureFromVolts Get Coefficient
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    coefficient
    RETURN             ${result}

TemperatureFromVolts Get Connected Voltage
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_voltage
    RETURN             ${result}

TemperatureFromVolts Get Measurement
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    measurement
    RETURN             ${result}

TemperatureFromVolts Set Connected Voltage
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_voltage    @{args}

PressureFromAmperes Get Coefficient
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    coefficient
    RETURN             ${result}

PressureFromAmperes Get Connected Ampere
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_ampere
    RETURN             ${result}

PressureFromAmperes Get Measurement
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    measurement
    RETURN             ${result}

PressureFromAmperes Set Connected Ampere
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_ampere    @{args}

