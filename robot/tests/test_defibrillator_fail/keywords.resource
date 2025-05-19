*** Settings ***
Library    devsure.robot

*** Keywords ***
PowerUnit Get Battery Level
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.battery_level}

PowerUnit Set Battery Level
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.battery_level}=    Set Variable  ${value}

PowerUnit Provide Power
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    provide_power    @{args}
    RETURN             ${result}

PowerUnit Recharge
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    recharge    @{args}
    RETURN             ${result}

Electrodes Get Material
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.material}

Electrodes Set Material
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.material}=    Set Variable  ${value}

Electrodes Get Thickness
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.thickness}

Electrodes Set Thickness
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.thickness}=    Set Variable  ${value}

Electrodes Get Contact Area
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.contact_area}

Electrodes Set Contact Area
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.contact_area}=    Set Variable  ${value}

Electrodes Get Rhythm Data
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.rhythm_data}

Electrodes Set Rhythm Data
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.rhythm_data}=    Set Variable  ${value}

Electrodes Get Charge Level
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.charge_level}

Electrodes Set Charge Level
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.charge_level}=    Set Variable  ${value}

Electrodes Get Efficiency
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.efficiency}

Electrodes Detect Heart Rhythm
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    detect_heart_rhythm    @{args}
    RETURN             ${result}

Electrodes Deliver Shock
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    deliver_shock    @{args}
    RETURN             ${result}

Electrodes Reset Charge
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    reset_charge    @{args}
    RETURN             ${result}

Switch Get State
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.state}

Switch Set State
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.state}=    Set Variable  ${value}

Speaker Get Instruction
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.instruction}

Speaker Set Instruction
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.instruction}=    Set Variable  ${value}

Microprocessor Get Connected Power Supply
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_power_supply}

Microprocessor Set Connected Power Supply
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_power_supply}=    Set Variable  ${value}

Microprocessor Get Connected Electrodes
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_electrodes}

Microprocessor Set Connected Electrodes
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_electrodes}=    Set Variable  ${value}

Microprocessor Get Connected Capacitor
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_capacitor}

Microprocessor Set Connected Capacitor
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_capacitor}=    Set Variable  ${value}

Microprocessor Get Connected Switch
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_switch}

Microprocessor Set Connected Switch
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_switch}=    Set Variable  ${value}

Microprocessor Get Connected Speaker
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_speaker}

Microprocessor Set Connected Speaker
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_speaker}=    Set Variable  ${value}

Microprocessor Analyze Rhythm
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    analyze_rhythm    @{args}
    RETURN             ${result}

Microprocessor Process Rhythm
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    process_rhythm    @{args}
    RETURN             ${result}

Capacitor Get Connected Power Supply
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_power_supply}

Capacitor Set Connected Power Supply
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_power_supply}=    Set Variable  ${value}

Capacitor Get Connected Electrodes
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_electrodes}

Capacitor Set Connected Electrodes
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_electrodes}=    Set Variable  ${value}

Capacitor Get Charge Voltage
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.charge_voltage}

Capacitor Set Charge Voltage
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.charge_voltage}=    Set Variable  ${value}

Capacitor Charge
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    charge    @{args}
    RETURN             ${result}

Capacitor Discharge
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    discharge    @{args}
    RETURN             ${result}

Defibrillator Get Connected Electrodes
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_electrodes}

Defibrillator Set Connected Electrodes
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_electrodes}=    Set Variable  ${value}

Defibrillator Get Connected Microprocessor
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.connected_microprocessor}

Defibrillator Set Connected Microprocessor
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.connected_microprocessor}=    Set Variable  ${value}

Defibrillator Defibrillate
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    defibrillate    @{args}
    RETURN             ${result}
