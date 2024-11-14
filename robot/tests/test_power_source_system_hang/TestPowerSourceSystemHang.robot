# Test to imitate the hanging of the system
# Add "Hang With Failing Condition" keyword call to any test to cause system hang

*** Settings ***
Documentation    The simple demo of testing our model with the Robot Framework - System Hang
Resource         keywords.resource

*** Keywords ***
Random Pause
    ${pause_sec}=    Evaluate    __import__('random').randint(4, 8)
    Evaluate    __import__('time').sleep(${pause_sec})

Hang With Failing Condition
    Wait Until Keyword Succeeds    1000000    1s    Should Be Equal    ${1}

*** Test Cases ***
Test Power Source Pass
    [Documentation]                    Pass test before system hang
    ${voltage_limit}=                  DCPowerSupply Get Voltage Limit        power_source
    Log To Console                     Voltage limit is - ${voltage_limit}
    Random Pause
    Should Be Equal As Numbers         ${voltage_limit}    120.1
    ${current_limit}                   DCPowerSupply Get Current Limit    power_source
    Log To Console                     Current limit is - ${current_limit}
    Should Be Equal As Numbers         ${voltage_limit}    120.1
    Should Be Equal As Numbers         ${current_limit}    5.1

Test System Hang
    [Documentation]                    Test to imitate the the hanging of the system - infinite loop
    ${voltage_limit}=                  DCPowerSupply Get Voltage Limit        power_source
    Log To Console                     Voltage limit is - ${voltage_limit}
    Random Pause
    Should Be Equal As Numbers         ${voltage_limit}    120.1
    ${current_limit}                   DCPowerSupply Get Current Limit    power_source
    Log To Console                     Current limit is - ${current_limit}
    Random Pause
    Log To Console                     Causing infinite loop...
    Random Pause
    Log To Console                     Test is going to hang for around 11 days...
    Should Be Equal As Numbers         ${current_limit}    5.1

Test Power Source After Hang Test
    [Documentation]                    Pass test after system hang
    ${voltage_limit}=                  DCPowerSupply Get Voltage Limit        power_source
    Log To Console                     Voltage limit is - ${voltage_limit}
    Random Pause
    Should Be Equal As Numbers         ${voltage_limit}    120.1
    ${current_limit}                   DCPowerSupply Get Current Limit    power_source
    Log To Console                     Current limit is - ${current_limit}
    Should Be Equal As Numbers         ${voltage_limit}    120.1
    Should Be Equal As Numbers         ${current_limit}    5.1