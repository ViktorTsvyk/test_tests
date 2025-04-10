*** Settings ***
Documentation    The simple demo of testing our model with the Robot Framework - Blood Pressure Measurement Device
Variables        variables.py
Resource         keywords.resource

*** Test Cases ***
Test Emulator Loaded
    [Documentation]                    Example testcase, that uses BPM Emulator

    Utils.Sleep  200
    ${remember_display_refreshes}=     BpmEmulatorRpc Get Display Refreshes    emulator
    Should Be True                     ${remember_display_refreshes}>0  There shall be display refreshes since start

    Utils.Sleep  1000
    ${new_refreshes}=                  BpmEmulatorRpc Get Display Refreshes    emulator
    Should Be Equal As Integers        ${new_refreshes}  ${remember_display_refreshes}  There shall be no display refreshes while no buttons were pressed

    BpmEmulatorRpc Click Pin           emulator  ${PinState.ButtonOk}
    ${new_refreshes}=                  BpmEmulatorRpc Get Display Refreshes    emulator
    Log To Console                     new_refreshes=${new_refreshes}, remember_display_refreshes=${remember_display_refreshes}
    Should Be True                     ${new_refreshes}>${remember_display_refreshes}  There shall be display refreshes after ButtonOk
    ${remember_display_refreshes}=     Set Variable  ${new_refreshes}


    FOR  ${i}  IN RANGE  1  11
        Log To Console                 ------------------
        Log To Console                 Pressing button BUTTON1 ${i} of 10
        BpmEmulatorRpc Click Pin       emulator  ${PinState.ButtonDown}

        ${save_at}=                    Set Variable  %{DEVSURE_REPORT_FOLDER}/Image${i}.png
        Log To Console                 !!!!!!!!!!!!!!! Saving image to ${save_at}
        ${screen_image}=               BpmEmulatorRpc Get Screen Image  emulator
        Call Method                    ${screen_image}  save  ${save_at}

        ${new_refreshes}=              BpmEmulatorRpc Get Display Refreshes    emulator
        Log To Console                 new_refreshes=${new_refreshes}, remember_display_refreshes=${remember_display_refreshes}
        Should Be True                 ${new_refreshes}>${remember_display_refreshes}  There shall be display refreshes after ButtonOk
        ${remember_display_refreshes}=  Set Variable  ${new_refreshes}
        Utils.Sleep  1000
    END
