*** Settings ***
Library    devsure/robot_tools/ListenerLibrary.py         AS      _
Library    devsure/robot_tools/EnvironmentLibrary.py      AS      EL
Library    devsure/robot_tools/DynamicDeviceLibrary.py    AS      DEVICES

*** Keywords ***
PowerUnit Get Battery Level
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    battery_level
    RETURN             ${result}

PowerUnit Set Battery Level
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    battery_level    @{args}

PowerUnit Provide Power
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    provide_power    @{args}
    RETURN             ${result}

PowerUnit Recharge
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    recharge    @{args}
    RETURN             ${result}

Electrodes Get Material
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    material
    RETURN             ${result}

Electrodes Set Material
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    material    @{args}

Electrodes Get Thickness
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    thickness
    RETURN             ${result}

Electrodes Set Thickness
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    thickness    @{args}

Electrodes Get Contact Area
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    contact_area
    RETURN             ${result}

Electrodes Set Contact Area
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    contact_area    @{args}

Electrodes Get Rhythm Data
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    rhythm_data
    RETURN             ${result}

Electrodes Set Rhythm Data
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    rhythm_data    @{args}

Electrodes Get Charge Level
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    charge_level
    RETURN             ${result}

Electrodes Set Charge Level
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    charge_level    @{args}

Electrodes Get Efficiency
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    efficiency
    RETURN             ${result}

Electrodes Detect Heart Rhythm
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    detect_heart_rhythm    @{args}
    RETURN             ${result}

Electrodes Deliver Shock
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    deliver_shock    @{args}
    RETURN             ${result}

Electrodes Reset Charge
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    reset_charge    @{args}
    RETURN             ${result}

Switch Get State
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    state
    RETURN             ${result}

Switch Set State
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    state    @{args}

Speaker Get Instruction
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    instruction
    RETURN             ${result}

Speaker Set Instruction
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    instruction    @{args}

Microprocessor Get Connected Power Supply
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_power_supply
    RETURN             ${result}

Microprocessor Set Connected Power Supply
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_power_supply    @{args}

Microprocessor Get Connected Electrodes
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_electrodes
    RETURN             ${result}

Microprocessor Set Connected Electrodes
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_electrodes    @{args}

Microprocessor Get Connected Capacitor
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_capacitor
    RETURN             ${result}

Microprocessor Set Connected Capacitor
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_capacitor    @{args}

Microprocessor Get Connected Switch
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_switch
    RETURN             ${result}

Microprocessor Set Connected Switch
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_switch    @{args}

Microprocessor Get Connected Speaker
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_speaker
    RETURN             ${result}

Microprocessor Set Connected Speaker
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_speaker    @{args}

Microprocessor Analyze Rhythm
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    analyze_rhythm    @{args}
    RETURN             ${result}

Microprocessor Process Rhythm
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    process_rhythm    @{args}
    RETURN             ${result}

Capacitor Get Connected Power Supply
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_power_supply
    RETURN             ${result}

Capacitor Set Connected Power Supply
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_power_supply    @{args}

Capacitor Get Connected Electrodes
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_electrodes
    RETURN             ${result}

Capacitor Set Connected Electrodes
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_electrodes    @{args}

Capacitor Get Charge Voltage
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    charge_voltage
    RETURN             ${result}

Capacitor Set Charge Voltage
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    charge_voltage    @{args}

Capacitor Charge
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    charge    @{args}
    RETURN             ${result}

Capacitor Discharge
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    discharge    @{args}
    RETURN             ${result}

Defibrillator Get Connected Electrodes
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_electrodes
    RETURN             ${result}

Defibrillator Set Connected Electrodes
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_electrodes    @{args}

Defibrillator Get Connected Microprocessor
    [Documentation]    Getter
    [Arguments]        ${device_name}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Get Property    ${instance}    connected_microprocessor
    RETURN             ${result}

Defibrillator Set Connected Microprocessor
    [Documentation]    Setter
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    EL.Set Property    ${instance}    connected_microprocessor    @{args}

Defibrillator Defibrillate
    [Documentation]    Method
    [Arguments]        ${device_name}    @{args}
    ${instance} =      DEVICES.Get Device    ${device_name}
    ${result} =        EL.Call Method    ${instance}    defibrillate    @{args}
    RETURN             ${result}
