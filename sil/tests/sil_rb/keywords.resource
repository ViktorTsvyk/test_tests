*** Settings ***
Library    devsure/robot_tools/UtilsLibrary.py         AS      Utils
Variables  devsure/robot_tools/UtilsVariables.py

*** Keywords ***
BpmEmulatorRpc Get Id To Local Function
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.id_to_local_function}

BpmEmulatorRpc Get Rpc Api Checksum
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.rpc_api_checksum}

BpmEmulatorRpc Get Pending Interrupts
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.pending_interrupts}

BpmEmulatorRpc Get Screen W
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.SCREEN_W}

BpmEmulatorRpc Get Screen H
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.SCREEN_H}

BpmEmulatorRpc Get Bytes Per Color
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.BYTES_PER_COLOR}

BpmEmulatorRpc Add Interrupt
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    add_interrupt    @{args}
    RETURN             ${result}

BpmEmulatorRpc Get Pin State
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.pin_state}

BpmEmulatorRpc Set Pin State
    [Documentation]    Setter
    [Arguments]        ${name}    ${value}
    ${tenv.${name}.pin_state}=    Set Variable  ${value}

BpmEmulatorRpc Set Pin
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    set_pin    @{args}
    RETURN             ${result}

BpmEmulatorRpc Clear Pin
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    clear_pin    @{args}
    RETURN             ${result}

BpmEmulatorRpc Toggle Pin
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    toggle_pin    @{args}
    RETURN             ${result}

BpmEmulatorRpc Click Pin
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    click_pin    @{args}
    RETURN             ${result}

BpmEmulatorRpc Get Display Refreshes
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.display_refreshes}

BpmEmulatorRpc Get Screen Image
    [Documentation]    Attribute
    [Arguments]        ${name}
    RETURN             ${tenv.${name}.screen_image}

BpmEmulatorRpc Framework Wait In Idle State
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    framework_wait_in_idle_state    @{args}
    RETURN             ${result}

BpmEmulatorRpc Framework Display Screen
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    framework_display_screen    @{args}
    RETURN             ${result}

BpmEmulatorRpc Emulator Start Emulation
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    emulator_start_emulation    @{args}
    RETURN             ${result}

BpmEmulatorRpc Emulator Stop Emulation
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    emulator_stop_emulation    @{args}
    RETURN             ${result}

BpmEmulatorRpc Emulator Echo
    [Documentation]    Method
    [Arguments]        ${name}    @{args}
    ${result} =        Call Method    ${tenv.${name}}    emulator_echo    @{args}
    RETURN             ${result}
