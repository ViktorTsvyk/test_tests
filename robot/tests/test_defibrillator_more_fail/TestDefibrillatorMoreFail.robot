# PASS - 32, FAIL - 65

*** Settings ***
Documentation    The simple demo of testing our model with the Robot Framework - Power Source
Variables        HeartRhythm.py
Resource         keywords.resource

*** Keywords ***
Random Pause
    ${pause_sec}=    Evaluate    __import__('random').randint(1, 2)
    Evaluate    __import__('time').sleep(${pause_sec})

*** Test Cases ***
Test Normal Rhythm Battery
    [Documentation]               Test that battery charge level is full under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Random Pause
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be Equal As Numbers    ${battery_level}    101.0    The battery discharged with a normal heart rhythm

Test Normal Rhythm Microprocessor Status
    [Documentation]                   Test microprocessor status after analysis of normal heart rhythm
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Random Pause
    Should Be Equal                   ${rhythm_status}    Norm rhythm    Invalid status of microprocessor

Test Ventricular Fibrillation Battery
    [Documentation]               Test that battery is discharged with ventricular fibrillation heart rhythm
    Log To Console                Start defibrillator with ventricular fibrillation heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${ventricular_fibrillation}
    Random Pause
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 98.0
    ...     The battery does not discharged with a ventricular fibrillation rhythm

Test Ventricular Fibrillation Charge Level
    [Documentation]               Test that battery is discharged with ventricular fibrillation heart rhythm
    Log To Console                Start defibrillator with ventricular fibrillation heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${ventricular_fibrillation}
    Random Pause
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 98.0
    ...     The battery does not discharged with a ventricular fibrillation rhythm

Test Ventricular Fibrillation Capacitor Discharge
    [Documentation]               Test that capacitor voltage level is zero under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    Random Pause
    ${capacitor_charge}=          Capacitor Get Charge Voltage    capacitor
    Log To Console                Capacitor charge voltage level after defibrillation is - ${capacitor_charge}
    Should Not Be Equal As Numbers    ${capacitor_charge}    0.0
    ...    The capacitor is not discharged with a normal heart rhythm

Test Pulseless Ventricular Tachycardia Battery
    [Documentation]               Test that battery discharges under condition of a pulseless ventricular tachycardia
    Log To Console                Start defibrillator with pulseless ventricular tachycardia heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${pulseless_ventricular_tachycardia}
    Random Pause
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Random Pause
    Should Be True                ${battery_level} < 101.0
    ...     The battery does not discharged with a pulseless ventricular tachycardia heart rhythm

Test Pulseless Ventricular Tachycardia Microprocessor Status
    [Documentation]                   Test microprocessor status after analysis of a pulseless ventricular tachycardia
    Log To Console                    Start electrodes for rhythm detection...
    Random Pause
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Tachycardia without pulse    Invalid status of microprocessor

Test Speaker Initial State
    [Documentation]                   Test the speaker initial status
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Random Pause
    Log To Console                    Current speaker instruction is - ${initial_instruction}
    Random Pause
    Should Be Equal                   ${initial_instruction}    Awaiting instructions

Test Speaker Normal Rhythm Analyze
    [Documentation]                   Test the speaker status with a normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Random Pause
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Random Pause
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Be Equal                   ${new_instruction}    No shock needed. Monitoring...
    ...                               Speaker instruction is not valid after rhythm processing

Test Speaker Not Normal Rhythm Analyze
    [Documentation]                   Test the speaker status with not normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Random Pause
    Electrodes Detect Heart Rhythm    electrodes    ${ventricular_fibrillation}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Random Pause
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Be Equal                   ${new_instruction}    Preparing to deliver shock. Touch the body!
    ...                               Speaker instruction is not valid after rhythm processing

Test Switch Initial State
    [Documentation]                   Test charge not allowed initially - switch state is False
    ${switch_state}=                  Switch Get State    switch
    Random Pause
    Should Be True                ${switch_state}    Switch is set to True - charge is allowed

Test Switch Normal Rhythm State
    [Documentation]                   Test charge not allowed for normal heart rhythm - switch state is False
    ${init_switch_state}=             Switch Get State    switch
    Log To Console                    Initial switch state is - ${init_switch_state}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Random Pause
    Microprocessor Process Rhythm     microprocessor
    ${new_switch_state}=              Switch Get State    switch
    Should Be True                ${new_switch_state}    Switch is set to True - charge is allowed

Test Switch State Dropped After Shock
    [Documentation]                   Test switched is discharged after shock - switch state is False
    Log To Console                    Start electrodes for rhythm detection...
    Random Pause
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    Random Pause
    ${switch_state_after_shock}=      Switch Get State    switch
    Should Be True                ${switch_state_after_shock}    Switch is not discharged

Test Normal Rhythm Battery Value
    [Documentation]               Test that battery charge level is full under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    Random Pause
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be Equal As Numbers    ${battery_level}    99.0    The battery discharged with a normal heart rhythm

Test Normal Rhythm Microprocessor Status Text
    [Documentation]                   Test microprocessor status after analysis of normal heart rhythm
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Random Pause
    Should Be Equal                   ${rhythm_status}    Normal    Invalid status of microprocessor

Test Ventricular Fibrillation Battery Value
    [Documentation]               Test that battery is discharged with ventricular fibrillation heart rhythm
    Log To Console                Start defibrillator with ventricular fibrillation heart rhythm...
    Random Pause
    Defibrillator Defibrillate    defibrillator   ${ventricular_fibrillation}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 10.0
    ...     The battery does not discharged with a ventricular fibrillation rhythm

Test Ventricular Fibrillation Capacitor Discharge Value
    [Documentation]               Test that capacitor voltage level is zero under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Random Pause
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    ${capacitor_charge}=          Capacitor Get Charge Voltage    capacitor
    Random Pause
    Log To Console                Capacitor charge voltage level after defibrillation is - ${capacitor_charge}
    Should Be Equal As Numbers    ${capacitor_charge}    1.0
    ...    The capacitor is not discharged with a normal heart rhythm

Test Pulseless Ventricular Tachycardia Battery Value
    [Documentation]               Test that battery discharges under condition of a pulseless ventricular tachycardia
    Log To Console                Start defibrillator with pulseless ventricular tachycardia heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${pulseless_ventricular_tachycardia}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 10.0
    ...     The battery does not discharged with a pulseless ventricular tachycardia heart rhythm

Test Pulseless Ventricular Tachycardia Microprocessor Status Text
    [Documentation]                   Test microprocessor status after analysis of a pulseless ventricular tachycardia
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Tachycardia without a pulse    Invalid status of microprocessor

Test Speaker Initial State Text
    [Documentation]                   Test the speaker initial status
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Random Pause
    Log To Console                    Current speaker instruction is - ${initial_instruction}
    Should Be Equal                   ${initial_instruction}    Awaiting instructions

Test Speaker Normal Rhythm Analyze Text
    [Documentation]                   Test the speaker status with a normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Random Pause
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    Random Pause
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Be Equal                   ${new_instruction}    No shock needed. Monitoring...
    ...                               Speaker instruction is not valid after rhythm processing

Test Speaker Not Normal Rhythm Analyze Text
    [Documentation]                   Test the speaker status with not normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Random Pause
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${ventricular_fibrillation}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Be Equal                   ${new_instruction}    Preparing to deliver shock!
    ...                               Speaker instruction is not valid after rhythm processing

Test Switch Initial State Value
    [Documentation]                   Test charge not allowed initially - switch state is False
    ${switch_state}=                  Switch Get State    switch
    Random Pause
    Should Not Be True                ${switch_state}    Switch is set to True - charge is allowed

Test Switch Normal Rhythm State Value
    [Documentation]                   Test charge not allowed for normal heart rhythm - switch state is False
    ${init_switch_state}=             Switch Get State    switch
    Log To Console                    Initial switch state is - ${init_switch_state}
    Log To Console                    Start electrodes for rhythm detection...
    Random Pause
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Random Pause
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_switch_state}=              Switch Get State    switch
    Should Not Be True                ${new_switch_state}    Switch is set to True - charge is allowed

Test Switch State Dropped After Shock To Zero
    [Documentation]                   Test switched is discharged after shock - switch state is False
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Random Pause
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${switch_state_after_shock}=      Switch Get State    switch
    Should Not Be True                ${switch_state_after_shock}    Switch is not discharged

Test Normal Rhythm Battery Value
    [Documentation]               Test that battery charge level is full under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Random Pause
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be Equal As Numbers    ${battery_level}    103.0    The battery discharged with a normal heart rhythm

Test Normal Rhythm Microprocessor Status Text
    [Documentation]                   Test microprocessor status after analysis of normal heart rhythm
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Normal    Invalid status of microprocessor

Test Ventricular Fibrillation Battery Value
    [Documentation]               Test that battery is discharged with ventricular fibrillation heart rhythm
    Log To Console                Start defibrillator with ventricular fibrillation heart rhythm...
    Random Pause
    Defibrillator Defibrillate    defibrillator   ${ventricular_fibrillation}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Random Pause
    Should Be True                ${battery_level} > 100.0
    ...     The battery does not discharged with a ventricular fibrillation rhythm

Test Ventricular Fibrillation Capacitor Discharge Value
    [Documentation]               Test that capacitor voltage level is zero under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Random Pause
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    ${capacitor_charge}=          Capacitor Get Charge Voltage    capacitor
    Random Pause
    Log To Console                Capacitor charge voltage level after defibrillation is - ${capacitor_charge}
    Should Be Equal As Numbers    ${capacitor_charge}    44.0
    ...    The capacitor is not discharged with a normal heart rhythm

Test Pulseless Ventricular Tachycardia Battery Value
    [Documentation]               Test that battery discharges under condition of a pulseless ventricular tachycardia
    Log To Console                Start defibrillator with pulseless ventricular tachycardia heart rhythm...
    Random Pause
    Defibrillator Defibrillate    defibrillator   ${pulseless_ventricular_tachycardia}
    Random Pause
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 44.0
    ...     The battery does not discharged with a pulseless ventricular tachycardia heart rhythm

Test Pulseless Ventricular Tachycardia Microprocessor Status Text
    [Documentation]                   Test microprocessor status after analysis of a pulseless ventricular tachycardia
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Tachycardia   Invalid status of microprocessor

Test Speaker Initial State Text
    [Documentation]                   Test the speaker initial status
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Random Pause
    Log To Console                    Current speaker instruction is - ${initial_instruction}
    Should Be Equal                   ${initial_instruction}    Awaiting help...

Test Speaker Normal Rhythm Analyze Text
    [Documentation]                   Test the speaker status with a normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Random Pause
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Random Pause
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Be Equal                   ${new_instruction}    No shock! Continue monitoring...
    ...                               Speaker instruction is not valid after rhythm processing

Test Speaker Not Normal Rhythm Analyze Text
    [Documentation]                   Test the speaker status with not normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${ventricular_fibrillation}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Random Pause
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Random Pause
    Should Be Equal                   ${new_instruction}    Preparing deliver shock. Dont touch the body!
    ...                               Speaker instruction is not valid after rhythm processing

Test Switch Initial State Value
    [Documentation]                   Test charge not allowed initially - switch state is False
    ${switch_state}=                  Switch Get State    switch
    Random Pause
    Should Be True                ${switch_state}    Switch is set to True - charge is allowed

Test Switch Normal Rhythm State Value
    [Documentation]                   Test charge not allowed for normal heart rhythm - switch state is False
    ${init_switch_state}=             Switch Get State    switch
    Log To Console                    Initial switch state is - ${init_switch_state}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_switch_state}=              Switch Get State    switch
    Should Be True                ${new_switch_state}    Switch is set to True - charge is allowed

Test Switch State Dropped After Shock To Zero
    [Documentation]                   Test switched is discharged after shock - switch state is False
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${switch_state_after_shock}=      Switch Get State    switch
    Should Be True                ${switch_state_after_shock}    Switch is not discharged

Test Normal Rhythm Battery Level
    [Documentation]               Test that battery charge level is full under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be Equal As Numbers    ${battery_level}    102.0    The battery discharged with a normal heart rhythm

Test Normal Rhythm Microprocessor Status Instruction
    [Documentation]                   Test microprocessor status after analysis of normal heart rhythm
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Normal    Invalid status of microprocessor

Test Ventricular Fibrillation Battery Level
    [Documentation]               Test that battery is discharged with ventricular fibrillation heart rhythm
    Log To Console                Start defibrillator with ventricular fibrillation heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${ventricular_fibrillation}
    Random Pause
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 78.0
    ...     The battery does not discharged with a ventricular fibrillation rhythm

Test Ventricular Fibrillation Capacitor Discharge Level
    [Documentation]               Test that capacitor voltage level is zero under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    Random Pause
    ${capacitor_charge}=          Capacitor Get Charge Voltage    capacitor
    Log To Console                Capacitor charge voltage level after defibrillation is - ${capacitor_charge}
    Should Be Equal As Numbers    ${capacitor_charge}    2.0
    ...    The capacitor is not discharged with a normal heart rhythm

Test Pulseless Ventricular Tachycardia Battery Level
    [Documentation]               Test that battery discharges under condition of a pulseless ventricular tachycardia
    Log To Console                Start defibrillator with pulseless ventricular tachycardia heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${pulseless_ventricular_tachycardia}
    Random Pause
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 78.0
    ...     The battery does not discharged with a pulseless ventricular tachycardia heart rhythm

Test Pulseless Ventricular Tachycardia Microprocessor Status Instruction
    [Documentation]                   Test microprocessor status after analysis of a pulseless ventricular tachycardia
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Random Pause
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Tachycardia with a pulse    Invalid status of microprocessor

Test Speaker Initial State Instruction
    [Documentation]                   Test the speaker initial status
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Random Pause
    Log To Console                    Current speaker instruction is - ${initial_instruction}
    Should Be Equal                   ${initial_instruction}    Wait instructions...

Test Speaker Normal Rhythm Analyze Instruction
    [Documentation]                   Test the speaker status with a normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Random Pause
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Random Pause
    Should Be Equal                   ${new_instruction}    Continue monitoring...
    ...                               Speaker instruction is not valid after rhythm processing

Test Speaker Not Normal Rhythm Analyze Instruction
    [Documentation]                   Test the speaker status with not normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Random Pause
    Electrodes Detect Heart Rhythm    electrodes    ${ventricular_fibrillation}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Be Equal                   ${new_instruction}    Preparing to shock. Do not touch body!
    ...                               Speaker instruction is not valid after rhythm processing

Test Switch Initial Value
    [Documentation]                   Test charge not allowed initially - switch state is False
    ${switch_state}=                  Switch Get State    switch
    Random Pause
    Should Be True                ${switch_state}    Switch is set to True - charge is allowed

Test Switch Normal Rhythm Value
    [Documentation]                   Test charge not allowed for normal heart rhythm - switch state is False
    ${init_switch_state}=             Switch Get State    switch
    Log To Console                    Initial switch state is - ${init_switch_state}
    Log To Console                    Start electrodes for rhythm detection...
    Random Pause
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_switch_state}=              Switch Get State    switch
    Should Be True                ${new_switch_state}    Switch is set to True - charge is allowed

Test Switch State After Shock Is Zero
    [Documentation]                   Test switched is discharged after shock - switch state is False
    Log To Console                    Start electrodes for rhythm detection...
    Random Pause
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    Random Pause
    ${switch_state_after_shock}=      Switch Get State    switch
    Should Be True                ${switch_state_after_shock}    Switch is not discharged

Test Smoke Normal Rhythm Battery
    [Documentation]               Test that battery charge level is full under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be Equal As Numbers    ${battery_level}    101.0    The battery discharged with a normal heart rhythm

Test Smoke Normal Rhythm Microprocessor Status
    [Documentation]                   Test microprocessor status after analysis of normal heart rhythm
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Random Pause
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Normal    Invalid status of microprocessor

Test Smoke Ventricular Fibrillation Battery
    [Documentation]               Test that battery is discharged with ventricular fibrillation heart rhythm
    Log To Console                Start defibrillator with ventricular fibrillation heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${ventricular_fibrillation}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 99.0
    ...     The battery does not discharged with a ventricular fibrillation rhythm

Test Smoke Ventricular Fibrillation Capacitor Discharge
    [Documentation]               Test that capacitor voltage level is zero under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    Random Pause
    ${capacitor_charge}=          Capacitor Get Charge Voltage    capacitor
    Log To Console                Capacitor charge voltage level after defibrillation is - ${capacitor_charge}
    Should Be Equal As Numbers    ${capacitor_charge}    1.0
    ...    The capacitor is not discharged with a normal heart rhythm

Test Smoke Pulseless Ventricular Tachycardia Battery
    [Documentation]               Test that battery discharges under condition of a pulseless ventricular tachycardia
    Log To Console                Start defibrillator with pulseless ventricular tachycardia heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${pulseless_ventricular_tachycardia}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 67.0
    ...     The battery does not discharged with a pulseless ventricular tachycardia heart rhythm

Test Smoke Pulseless Ventricular Tachycardia Microprocessor Status
    [Documentation]                   Test microprocessor status after analysis of a pulseless ventricular tachycardia
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Tachycardia    Invalid status of microprocessor

Test Smoke Speaker Initial State
    [Documentation]                   Test the speaker initial status
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Current speaker instruction is - ${initial_instruction}
    Random Pause
    Should Be Equal                   ${initial_instruction}    Awaiting help...

Test Smoke Speaker Normal Rhythm Analyze
    [Documentation]                   Test the speaker status with a normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Random Pause
    Should Not Be Equal               ${new_instruction}    No shock needed. Continue monitoring...
    ...                               Speaker instruction is not valid after rhythm processing

Test Smoke Speaker Not Normal Rhythm Analyze
    [Documentation]                   Test the speaker status with not normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${ventricular_fibrillation}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Not Be Equal               ${new_instruction}    Preparing to deliver shock. Do not touch the body!
    ...                               Speaker instruction is not valid after rhythm processing

Test Smoke Switch Normal Rhythm State
    [Documentation]                   Test charge not allowed for normal heart rhythm - switch state is False
    ${init_switch_state}=             Switch Get State    switch
    Log To Console                    Initial switch state is - ${init_switch_state}
    Log To Console                    Start electrodes for rhythm detection...
    Random Pause
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_switch_state}=              Switch Get State    switch
    Should Not Be True                ${new_switch_state}    Switch is set to True - charge is allowed

Test Smoke Switch State Dropped After Shock
    [Documentation]                   Test switched is discharged after shock - switch state is False
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${switch_state_after_shock}=      Switch Get State    switch
    Should Not Be True                ${switch_state_after_shock}    Switch is not discharged

Test Smoke Normal Rhythm Battery Value
    [Documentation]               Test that battery charge level is full under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    Random Pause
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be Equal As Numbers    ${battery_level}    100.0    The battery discharged with a normal heart rhythm

Test Smoke Normal Rhythm Microprocessor Status Text
    [Documentation]                   Test microprocessor status after analysis of normal heart rhythm
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Random Pause
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Normal rhythm    Invalid status of microprocessor

Test Smoke Ventricular Fibrillation Battery Value
    [Documentation]               Test that battery is discharged with ventricular fibrillation heart rhythm
    Log To Console                Start defibrillator with ventricular fibrillation heart rhythm...
    Random Pause
    Defibrillator Defibrillate    defibrillator   ${ventricular_fibrillation}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 100.0
    ...     The battery does not discharged with a ventricular fibrillation rhythm

Test Smoke Ventricular Fibrillation Capacitor Discharge Value
    [Documentation]               Test that capacitor voltage level is zero under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    ${capacitor_charge}=          Capacitor Get Charge Voltage    capacitor
    Random Pause
    Log To Console                Capacitor charge voltage level after defibrillation is - ${capacitor_charge}
    Should Be Equal As Numbers    ${capacitor_charge}    0.0
    ...    The capacitor is not discharged with a normal heart rhythm

Test Smoke Pulseless Ventricular Tachycardia Battery Value
    [Documentation]               Test that battery discharges under condition of a pulseless ventricular tachycardia
    Log To Console                Start defibrillator with pulseless ventricular tachycardia heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${pulseless_ventricular_tachycardia}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 100.0
    ...     The battery does not discharged with a pulseless ventricular tachycardia heart rhythm

Test Smoke Pulseless Ventricular Tachycardia Microprocessor Status Text
    [Documentation]                   Test microprocessor status after analysis of a pulseless ventricular tachycardia
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Tachycardia without a pulse    Invalid status of microprocessor

Test Smoke Speaker Initial State Text
    [Documentation]                   Test the speaker initial status
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Current speaker instruction is - ${initial_instruction}
    Random Pause
    Should Be Equal                   ${initial_instruction}    Awaiting instructions...

Test Smoke Speaker Normal Rhythm Analyze Text
    [Documentation]                   Test the speaker status with a normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Random Pause
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Be Equal                   ${new_instruction}    No shock needed. Continue monitoring...
    ...                               Speaker instruction is not valid after rhythm processing

Test Alpha Speaker Not Normal Rhythm Analyze Text
    [Documentation]                   Test the speaker status with not normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${ventricular_fibrillation}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Be Equal                   ${new_instruction}    Preparing to deliver shock. Do not touch the body!
    ...                               Speaker instruction is not valid after rhythm processing

Test Alpha Switch Initial State Value
    [Documentation]                   Test charge not allowed initially - switch state is False
    ${switch_state}=                  Switch Get State    switch
    Random Pause
    Should Not Be True                ${switch_state}    Switch is set to True - charge is allowed

Test Alpha Switch Normal Rhythm State Value
    [Documentation]                   Test charge not allowed for normal heart rhythm - switch state is False
    ${init_switch_state}=             Switch Get State    switch
    Log To Console                    Initial switch state is - ${init_switch_state}
    Random Pause
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_switch_state}=              Switch Get State    switch
    Should Not Be True                ${new_switch_state}    Switch is set to True - charge is allowed

Test Alpha Switch State Dropped After Shock To Zero
    [Documentation]                   Test switched is discharged after shock - switch state is False
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Random Pause
    Microprocessor Process Rhythm     microprocessor
    ${switch_state_after_shock}=      Switch Get State    switch
    Should Not Be True                ${switch_state_after_shock}    Switch is not discharged

Test Alpha Normal Rhythm Battery Value
    [Documentation]               Test that battery charge level is full under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    Random Pause
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be Equal As Numbers    ${battery_level}    100.0    The battery discharged with a normal heart rhythm

Test Alpha Normal Rhythm Microprocessor Status Text
    [Documentation]                   Test microprocessor status after analysis of normal heart rhythm
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Normal rhythm    Invalid status of microprocessor

Test Alpha Ventricular Fibrillation Battery Value
    [Documentation]               Test that battery is discharged with ventricular fibrillation heart rhythm
    Log To Console                Start defibrillator with ventricular fibrillation heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${ventricular_fibrillation}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 100.0
    ...     The battery does not discharged with a ventricular fibrillation rhythm

Test Alpha Ventricular Fibrillation Capacitor Discharge Value
    [Documentation]               Test that capacitor voltage level is zero under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    ${capacitor_charge}=          Capacitor Get Charge Voltage    capacitor
    Random Pause
    Log To Console                Capacitor charge voltage level after defibrillation is - ${capacitor_charge}
    Should Be Equal As Numbers    ${capacitor_charge}    0.0
    ...    The capacitor is not discharged with a normal heart rhythm

Test Regression Pulseless Ventricular Tachycardia Battery Value
    [Documentation]               Test that battery discharges under condition of a pulseless ventricular tachycardia
    Log To Console                Start defibrillator with pulseless ventricular tachycardia heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${pulseless_ventricular_tachycardia}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} < 100.0
    ...     The battery does not discharged with a pulseless ventricular tachycardia heart rhythm

Test Regression Pulseless Ventricular Tachycardia Microprocessor Status Text
    [Documentation]                   Test microprocessor status after analysis of a pulseless ventricular tachycardia
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Random Pause
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Be Equal                   ${rhythm_status}    Tachycardia without a pulse    Invalid status of microprocessor

Test Regression Speaker Initial State Text
    [Documentation]                   Test the speaker initial status
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Random Pause
    Log To Console                    Current speaker instruction is - ${initial_instruction}
    Should Be Equal                   ${initial_instruction}    Awaiting instructions...

Test Regression Speaker Normal Rhythm Analyze Text
    [Documentation]                   Test the speaker status with a normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Random Pause
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Random Pause
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Be Equal                   ${new_instruction}    No shock needed. Continue monitoring...
    ...                               Speaker instruction is not valid after rhythm processing

Test Regression Speaker Not Normal Rhythm Analyze Text
    [Documentation]                   Test the speaker status with not normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${ventricular_fibrillation}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Random Pause
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Be Equal                   ${new_instruction}    Preparing to deliver shock. Do not touch the body!
    ...                               Speaker instruction is not valid after rhythm processing

Test Regression Switch Initial State Value
    [Documentation]                   Test charge not allowed initially - switch state is False
    ${switch_state}=                  Switch Get State    switch
    Random Pause
    Should Not Be True                ${switch_state}    Switch is set to True - charge is allowed

Test Regression Switch Normal Rhythm State Value
    [Documentation]                   Test charge not allowed for normal heart rhythm - switch state is False
    ${init_switch_state}=             Switch Get State    switch
    Random Pause
    Log To Console                    Initial switch state is - ${init_switch_state}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Random Pause
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_switch_state}=              Switch Get State    switch
    Should Not Be True                ${new_switch_state}    Switch is set to True - charge is allowed

Test Regression Switch State Dropped After Shock To Zero
    [Documentation]                   Test switched is discharged after shock - switch state is False
    Log To Console                    Start electrodes for rhythm detection...
    Random Pause
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${switch_state_after_shock}=      Switch Get State    switch
    Should Not Be True                ${switch_state_after_shock}    Switch is not discharged

Test Regression Normal Rhythm Battery Level
    [Documentation]               Test that battery charge level is full under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Random Pause
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be Equal As Numbers    ${battery_level}    100.0    The battery discharged with a normal heart rhythm

Test Regression Normal Rhythm Microprocessor Status Instruction
    [Documentation]                   Test microprocessor status after analysis of normal heart rhythm
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Not Be Equal               ${rhythm_status}    Normal rhythm    Invalid status of microprocessor

Test Regression Ventricular Fibrillation Battery Level
    [Documentation]               Test that battery is discharged with ventricular fibrillation heart rhythm
    Log To Console                Start defibrillator with ventricular fibrillation heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${ventricular_fibrillation}
    Random Pause
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Be True                ${battery_level} > 100.0
    ...     The battery does not discharged with a ventricular fibrillation rhythm

Test Regression Ventricular Fibrillation Capacitor Discharge Level
    [Documentation]               Test that capacitor voltage level is zero under condition of a normal heart rhythm
    Log To Console                Start defibrillator with normal heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${normal_rhythm}
    ${capacitor_charge}=          Capacitor Get Charge Voltage    capacitor
    Random Pause
    Log To Console                Capacitor charge voltage level after defibrillation is - ${capacitor_charge}
    Should Be Equal As Numbers    ${capacitor_charge}    3.0
    ...    The capacitor is not discharged with a normal heart rhythm

Test Regression Pulseless Ventricular Tachycardia Battery Level
    [Documentation]               Test that battery discharges under condition of a pulseless ventricular tachycardia
    Log To Console                Start defibrillator with pulseless ventricular tachycardia heart rhythm...
    Defibrillator Defibrillate    defibrillator   ${pulseless_ventricular_tachycardia}
    ${battery_level}=             PowerUnit Get Battery Level    power_source
    Log To Console                Battery level after defibrillation is - ${battery_level}
    Should Not Be True            ${battery_level} < 100.0
    ...     The battery does not discharged with a pulseless ventricular tachycardia heart rhythm

Test Beta Pulseless Ventricular Tachycardia Microprocessor Status Instruction
    [Documentation]                   Test microprocessor status after analysis of a pulseless ventricular tachycardia
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Random Pause
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Should Not Be Equal               ${rhythm_status}    Tachycardia without a pulse    Invalid status of microprocessor

Test Beta Speaker Initial State Instruction
    [Documentation]                   Test the speaker initial status
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Current speaker instruction is - ${initial_instruction}
    Should Not Be Equal               ${initial_instruction}    Awaiting instructions...

Test Beta Speaker Normal Rhythm Analyze Instruction
    [Documentation]                   Test the speaker status with a normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Not Be Equal               ${new_instruction}    No shock needed. Continue monitoring...
    ...                               Speaker instruction is not valid after rhythm processing

Test Beta Speaker Not Normal Rhythm Analyze Instruction
    [Documentation]                   Test the speaker status with not normal heart rhythm
    ${initial_instruction}=           Speaker Get Instruction    speaker
    Log To Console                    Initial speaker instruction is - ${initial_instruction}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${ventricular_fibrillation}
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Random Pause
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Random Pause
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_instruction}=               Speaker Get Instruction    speaker
    Log To Console                    New speaker instruction is - ${new_instruction}
    Should Not Be Equal               ${new_instruction}    Preparing to deliver shock. Do not touch the body!
    ...                               Speaker instruction is not valid after rhythm processing

Test Beta Switch Initial Value
    [Documentation]                   Test charge not allowed initially - switch state is False
    ${switch_state}=                  Switch Get State    switch
    Random Pause
    Should Be True                ${switch_state}    Switch is set to True - charge is allowed

Test Beta Switch Normal Rhythm Value
    [Documentation]                   Test charge not allowed for normal heart rhythm - switch state is False
    ${init_switch_state}=             Switch Get State    switch
    Log To Console                    Initial switch state is - ${init_switch_state}
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${normal_rhythm}
    Log To Console                    Start microprocessor for rhythm analysis...
    Random Pause
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${new_switch_state}=              Switch Get State    switch
    Should Be True                ${new_switch_state}    Switch is set to True - charge is allowed

Test Beta Switch State After Shock Is Zero
    [Documentation]                   Test switched is discharged after shock - switch state is False
    Log To Console                    Start electrodes for rhythm detection...
    Electrodes Detect Heart Rhythm    electrodes    ${pulseless_ventricular_tachycardia}
    Random Pause
    Log To Console                    Start microprocessor for rhythm analysis...
    ${rhythm_status}=                 Microprocessor Analyze Rhythm    microprocessor
    Log To Console                    Rhythm status after analysis is - ${rhythm_status}
    Log To Console                    Start microprocessor for rhythm processing...
    Microprocessor Process Rhythm     microprocessor
    ${switch_state_after_shock}=      Switch Get State    switch
    Should Be True                ${switch_state_after_shock}    Switch is not discharged

Test Reg Switch Initial Value
    [Documentation]                   Test charge not allowed initially - switch state is False
    ${switch_state}=                  Switch Get State    switch
    Random Pause
    Should Be True                ${switch_state}    Switch is set to True - charge is allowed