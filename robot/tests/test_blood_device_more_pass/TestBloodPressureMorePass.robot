# 75 tests pass, 8 tests fail

*** Settings ***
Documentation    Blood Pressure Measurement Device testing suite
Resource         keywords.resource

*** Keywords ***
Random Pause
    ${pause_sec}=    Evaluate    __import__('random').randint(1, 3)
    Evaluate    __import__('time').sleep(${pause_sec})

*** Test Cases ***
Test Pressure In Cuff
    [Documentation]                    Test the difference between the resultant pressure and the additional pressure
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    ${additional_pump_pressure}=       Pump Pumping     pump
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Random Pause
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    Random Pause
    ${result}=                         Evaluate    ${result_pressure} - ${additional_pump_pressure}
    Should Be Equal As Numbers         ${target_pressure}    ${result}    User did not get the target pressure value

Test Additional Pressure
    [Documentation]                    Test that the pressure inside the pump is present after pumping
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${additional_pump_pressure} > 0    There is no additional pump pressure

Test Pressure In Cuff More Than Additional
    [Documentation]                    Test that the pressure in cuff is more then additional
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Random Pause
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${result_pressure} > ${additional_pump_pressure}

Test Power Adapter Efficiency
    [Documentation]                    Test that the expected efficiency is 80% or more
    ${efficiency}=                     DCAdapter Get Efficiency    power_adapter
    Random Pause
    Log To Console                     Power adapter efficiency is - ${efficiency}
    Should Be True                     ${efficiency} >= 0.2

Test Connected Cuff Class
    [Documentation]                    Test the connected cuff class is InflatableCuff
    ${cuff}=                           Pump Get Connected Cuff    pump
    Random Pause
    ${cuff_txt}=                       Convert To String    ${cuff}
    Random Pause
    Log To Console                     Connected cuff is - ${cuff_txt}
    Should Contain                     ${cuff_txt}    InflatableCuff

Test Power Source Voltage Limit
    [Documentation]                    Test that power source voltage limit is 240.1
    ${voltage_limit}=                  DCPowerSupply Get Voltage Limit    power_source
    Random Pause
    Log To Console                     Power source voltage limit is - ${voltage_limit}
    Random Pause
    Should Be Equal As Numbers         ${voltage_limit}    240.1

Test Power Source Current Limit
    [Documentation]                    Test that power source current limit is 6.1
    ${current_limit}=                  DCPowerSupply Get Current Limit    power_source
    Random Pause
    Log To Console                     Power source current limit is - ${current_limit}
    Random Pause
    Should Be Equal As Numbers         ${current_limit}    6.1

Test Target Pressure Value
    [Documentation]                    Test that target pressure is more then 200
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Random Pause
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    Should Be True                     ${target_pressure} > 200

Test Minimum Pump Power
    [Documentation]                    Test the minimum required pump power level
    ${min_power}=                      Pump Get Min Power    pump
    Random Pause
    Log To Console                     Minimum required power level for the pump is - ${min_power}
    Random Pause
    Should Be True                     ${min_power} > 0

Test Pump Connected Controller
    [Documentation]                    Test the connected controller
    ${connected_controller}=           Pump Get Connected Controller    pump
    ${connected_controller_txt}=       Convert To String    ${connected_controller}
    Random Pause
    Log To Console                     Connected controller to pump is - ${connected_controller_txt}
    Random Pause
    Should Contain                     ${connected_controller_txt}    BloodPressureMD

Test Pressure Inside Cuff
    [Documentation]                    Test the difference between the resultant pressure and the additional pressure
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    ${additional_pump_pressure}=       Pump Pumping     pump
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Random Pause
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    Random Pause
    ${result}=                         Evaluate    ${result_pressure} - ${additional_pump_pressure}
    Should Be Equal As Numbers         ${target_pressure}    ${result}    User did not get the target pressure value

Test Additional Pressure Inside Cuff
    [Documentation]                    Test that the pressure inside the pump is present after pumping
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${additional_pump_pressure} > 0    There is no additional pump pressure

Test Pressure Inside Cuff More Than Additional
    [Documentation]                    Test that the pressure in cuff is more then additional
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Random Pause
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${result_pressure} > ${additional_pump_pressure}

Test Power Adapter Efficiency Level
    [Documentation]                    Test that the expected efficiency is 80% or more
    ${efficiency}=                     DCAdapter Get Efficiency    power_adapter
    Random Pause
    Log To Console                     Power adapter efficiency is - ${efficiency}
    Should Be True                     ${efficiency} >= 0.2

Test Connected Cuff Class Value
    [Documentation]                    Test the connected cuff class is InflatableCuff
    ${cuff}=                           Pump Get Connected Cuff    pump
    Random Pause
    ${cuff_txt}=                       Convert To String    ${cuff}
    Random Pause
    Log To Console                     Connected cuff is - ${cuff_txt}
    Should Contain                     ${cuff_txt}    InflatableCuff

Test Power Source Voltage Limit Value
    [Documentation]                    Test that power source voltage limit is 240.1
    ${voltage_limit}=                  DCPowerSupply Get Voltage Limit    power_source
    Random Pause
    Log To Console                     Power source voltage limit is - ${voltage_limit}
    Random Pause
    Should Be Equal As Numbers         ${voltage_limit}    240.1

Test Power Source Current Limit Value
    [Documentation]                    Test that power source current limit is 6.1
    ${current_limit}=                  DCPowerSupply Get Current Limit    power_source
    Random Pause
    Log To Console                     Power source current limit is - ${current_limit}
    Random Pause
    Should Be Equal As Numbers         ${current_limit}    6.1

Test Target Pressure Level
    [Documentation]                    Test that target pressure is more then 200
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Random Pause
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    Should Be True                     ${target_pressure} > 200

Test Min Pump Power
    [Documentation]                    Test the minimum required pump power level
    ${min_power}=                      Pump Get Min Power    pump
    Random Pause
    Log To Console                     Minimum required power level for the pump is - ${min_power}
    Random Pause
    Should Be True                     ${min_power} > 0

Test Pump Connected Controller Class
    [Documentation]                    Test the connected controller
    ${connected_controller}=           Pump Get Connected Controller    pump
    ${connected_controller_txt}=       Convert To String    ${connected_controller}
    Random Pause
    Log To Console                     Connected controller to pump is - ${connected_controller_txt}
    Random Pause
    Should Contain                     ${connected_controller_txt}    BloodPressureMD

Test The Pressure In The Cuff
    [Documentation]                    Test the difference between the resultant pressure and the additional pressure
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    ${additional_pump_pressure}=       Pump Pumping     pump
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Random Pause
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    Random Pause
    ${result}=                         Evaluate    ${result_pressure} - ${additional_pump_pressure}
    Should Be Equal As Numbers         ${target_pressure}    ${result}    User did not get the target pressure value

Test The Additional Pressure
    [Documentation]                    Test that the pressure inside the pump is present after pumping
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${additional_pump_pressure} > 0    There is no additional pump pressure

Test The Pressure In Cuff More Than Additional
    [Documentation]                    Test that the pressure in cuff is more then additional
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Random Pause
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${result_pressure} > ${additional_pump_pressure}

Test The Power Adapter Efficiency
    [Documentation]                    Test that the expected efficiency is 80% or more
    ${efficiency}=                     DCAdapter Get Efficiency    power_adapter
    Random Pause
    Log To Console                     Power adapter efficiency is - ${efficiency}
    Should Be True                     ${efficiency} >= 0.2

Test The Connected Cuff Class
    [Documentation]                    Test the connected cuff class is InflatableCuff
    ${cuff}=                           Pump Get Connected Cuff    pump
    Random Pause
    ${cuff_txt}=                       Convert To String    ${cuff}
    Random Pause
    Log To Console                     Connected cuff is - ${cuff_txt}
    Should Contain                     ${cuff_txt}    InflatableCuff

Test The Power Source Voltage Limit
    [Documentation]                    Test that power source voltage limit is 240.1
    ${voltage_limit}=                  DCPowerSupply Get Voltage Limit    power_source
    Random Pause
    Log To Console                     Power source voltage limit is - ${voltage_limit}
    Random Pause
    Should Be Equal As Numbers         ${voltage_limit}    240.1

Test The Power Source Current Limit
    [Documentation]                    Test that power source current limit is 6.1
    ${current_limit}=                  DCPowerSupply Get Current Limit    power_source
    Random Pause
    Log To Console                     Power source current limit is - ${current_limit}
    Random Pause
    Should Be Equal As Numbers         ${current_limit}    6.1

Test The Target Pressure Value
    [Documentation]                    Test that target pressure is more then 200
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Random Pause
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    Should Be True                     ${target_pressure} > 200

Test The Minimum Pump Power
    [Documentation]                    Test the minimum required pump power level
    ${min_power}=                      Pump Get Min Power    pump
    Random Pause
    Log To Console                     Minimum required power level for the pump is - ${min_power}
    Random Pause
    Should Be True                     ${min_power} > 0

Test The Pump Connected Controller
    [Documentation]                    Test the connected controller
    ${connected_controller}=           Pump Get Connected Controller    pump
    ${connected_controller_txt}=       Convert To String    ${connected_controller}
    Random Pause
    Log To Console                     Connected controller to pump is - ${connected_controller_txt}
    Random Pause
    Should Contain                     ${connected_controller_txt}    BloodPressureMD

Test Cuff Pressure Inside
    [Documentation]                    Test the difference between the resultant pressure and the additional pressure
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    ${additional_pump_pressure}=       Pump Pumping     pump
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Random Pause
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    Random Pause
    ${result}=                         Evaluate    ${result_pressure} + ${additional_pump_pressure}
    Should Be Equal As Numbers         ${target_pressure}    ${result}    User did not get the target pressure value

Test Value Of Additional Pressure
    [Documentation]                    Test that the pressure inside the pump is present after pumping
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${additional_pump_pressure} > 0    There is no additional pump pressure

Test Pressure In Cuff More Additional Pressure
    [Documentation]                    Test that the pressure in cuff is more then additional
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Random Pause
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${result_pressure} > ${additional_pump_pressure}

Test Power Adapter Efficiency Is As Expected
    [Documentation]                    Test that the expected efficiency is 80% or more
    ${efficiency}=                     DCAdapter Get Efficiency    power_adapter
    Random Pause
    Log To Console                     Power adapter efficiency is - ${efficiency}
    Should Be True                     ${efficiency} >= 0.2

Test Connected Cuff Class Title
    [Documentation]                    Test the connected cuff class is InflatableCuff
    ${cuff}=                           Pump Get Connected Cuff    pump
    Random Pause
    ${cuff_txt}=                       Convert To String    ${cuff}
    Random Pause
    Log To Console                     Connected cuff is - ${cuff_txt}
    Should Contain                     ${cuff_txt}    InflatableCuff

Test Power Source Voltage Level
    [Documentation]                    Test that power source voltage limit is 240.1
    ${voltage_limit}=                  DCPowerSupply Get Voltage Limit    power_source
    Random Pause
    Log To Console                     Power source voltage limit is - ${voltage_limit}
    Random Pause
    Should Be Equal As Numbers         ${voltage_limit}    240.1

Test Power Source Current Level
    [Documentation]                    Test that power source current limit is 6.1
    ${current_limit}=                  DCPowerSupply Get Current Limit    power_source
    Random Pause
    Log To Console                     Power source current limit is - ${current_limit}
    Random Pause
    Should Be Equal As Numbers         ${current_limit}    6.1

Test Pump Target Pressure Value
    [Documentation]                    Test that target pressure is more then 200
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Random Pause
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    Should Be True                     ${target_pressure} > 200

Test Pump Power Min Value
    [Documentation]                    Test the minimum required pump power level
    ${min_power}=                      Pump Get Min Power    pump
    Random Pause
    Log To Console                     Minimum required power level for the pump is - ${min_power}
    Random Pause
    Should Be True                     ${min_power} > 0

Test Connected Controller To Pump
    [Documentation]                    Test the connected controller
    ${connected_controller}=           Pump Get Connected Controller    pump
    ${connected_controller_txt}=       Convert To String    ${connected_controller}
    Random Pause
    Log To Console                     Connected controller to pump is - ${connected_controller_txt}
    Random Pause
    Should Contain                     ${connected_controller_txt}    BloodPressureMD

Test Pressure Inside The Cuff
    [Documentation]                    Test the difference between the resultant pressure and the additional pressure
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    ${additional_pump_pressure}=       Pump Pumping     pump
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Random Pause
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    Random Pause
    ${result}=                         Evaluate    ${result_pressure} - ${additional_pump_pressure}
    Should Be Equal As Numbers         ${target_pressure}    ${result}    User did not get the target pressure value

Test Additional Pressure For The Pump
    [Documentation]                    Test that the pressure inside the pump is present after pumping
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${additional_pump_pressure} > 0    There is no additional pump pressure

Test The Pressure Level In Cuff More Than Additional
    [Documentation]                    Test that the pressure in cuff is more then additional
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Random Pause
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${result_pressure} > ${additional_pump_pressure}

Test The Level Of Power Adapter Efficiency
    [Documentation]                    Test that the expected efficiency is 80% or more
    ${efficiency}=                     DCAdapter Get Efficiency    power_adapter
    Random Pause
    Log To Console                     Power adapter efficiency is - ${efficiency}
    Should Be True                     ${efficiency} >= 0.2

Test The Connected Cuff Class Text
    [Documentation]                    Test the connected cuff class is InflatableCuff
    ${cuff}=                           Pump Get Connected Cuff    pump
    Random Pause
    ${cuff_txt}=                       Convert To String    ${cuff}
    Random Pause
    Log To Console                     Connected cuff is - ${cuff_txt}
    Should Contain                     ${cuff_txt}    InflatableCuff

Test The Power Source Voltage Limit Level
    [Documentation]                    Test that power source voltage limit is 240.1
    ${voltage_limit}=                  DCPowerSupply Get Voltage Limit    power_source
    Random Pause
    Log To Console                     Power source voltage limit is - ${voltage_limit}
    Random Pause
    Should Be Equal As Numbers         ${voltage_limit}    240.1

Test The Power Source Current Limit Level
    [Documentation]                    Test that power source current limit is 6.1
    ${current_limit}=                  DCPowerSupply Get Current Limit    power_source
    Random Pause
    Log To Console                     Power source current limit is - ${current_limit}
    Random Pause
    Should Be Equal As Numbers         ${current_limit}    6.1

Test The Target Pressure Of Pump
    [Documentation]                    Test that target pressure is more then 200
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Random Pause
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    Should Be True                     ${target_pressure} < 200

Test The Minimum Power Level Of Pump
    [Documentation]                    Test the minimum required pump power level
    ${min_power}=                      Pump Get Min Power    pump
    Random Pause
    Log To Console                     Minimum required power level for the pump is - ${min_power}
    Random Pause
    Should Be True                     ${min_power} > 0

Test The Connected Controller Class Connected To Pump
    [Documentation]                    Test the connected controller
    ${connected_controller}=           Pump Get Connected Controller    pump
    ${connected_controller_txt}=       Convert To String    ${connected_controller}
    Random Pause
    Log To Console                     Connected controller to pump is - ${connected_controller_txt}
    Random Pause
    Should Contain                     ${connected_controller_txt}    BloodPressureMD

Test Smoke - Pressure In Cuff
    [Documentation]                    Test the difference between the resultant pressure and the additional pressure
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    ${additional_pump_pressure}=       Pump Pumping     pump
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Random Pause
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    Random Pause
    ${result}=                         Evaluate    ${result_pressure} - ${additional_pump_pressure}
    Should Be Equal As Numbers         ${target_pressure}    ${result}    User did not get the target pressure value

Test Smoke - Additional Pressure
    [Documentation]                    Test that the pressure inside the pump is present after pumping
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${additional_pump_pressure} > 0    There is no additional pump pressure

Test Smoke - Pressure In Cuff More Than Additional
    [Documentation]                    Test that the pressure in cuff is more then additional
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Random Pause
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${result_pressure} > ${additional_pump_pressure}

Test Smoke - Power Adapter Efficiency
    [Documentation]                    Test that the expected efficiency is 80% or more
    ${efficiency}=                     DCAdapter Get Efficiency    power_adapter
    Random Pause
    Log To Console                     Power adapter efficiency is - ${efficiency}
    Should Be True                     ${efficiency} >= 0.2

Test Smoke - Connected Cuff Class
    [Documentation]                    Test the connected cuff class is InflatableCuff
    ${cuff}=                           Pump Get Connected Cuff    pump
    Random Pause
    ${cuff_txt}=                       Convert To String    ${cuff}
    Random Pause
    Log To Console                     Connected cuff is - ${cuff_txt}
    Should Contain                     ${cuff_txt}    InfCuff

Test Smoke - Power Source Voltage Limit
    [Documentation]                    Test that power source voltage limit is 240.1
    ${voltage_limit}=                  DCPowerSupply Get Voltage Limit    power_source
    Random Pause
    Log To Console                     Power source voltage limit is - ${voltage_limit}
    Random Pause
    Should Be Equal As Numbers         ${voltage_limit}    240.1

Test Smoke - Power Source Current Limit
    [Documentation]                    Test that power source current limit is 6.1
    ${current_limit}=                  DCPowerSupply Get Current Limit    power_source
    Random Pause
    Log To Console                     Power source current limit is - ${current_limit}
    Random Pause
    Should Be Equal As Numbers         ${current_limit}    6.1

Test Smoke - Target Pressure Value
    [Documentation]                    Test that target pressure is more then 200
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Random Pause
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    Should Be True                     ${target_pressure} > 900

Test Smoke - Minimum Pump Power
    [Documentation]                    Test the minimum required pump power level
    ${min_power}=                      Pump Get Min Power    pump
    Random Pause
    Log To Console                     Minimum required power level for the pump is - ${min_power}
    Random Pause
    Should Be True                     ${min_power} > 0

Test Smoke - Pump Connected Controller
    [Documentation]                    Test the connected controller
    ${connected_controller}=           Pump Get Connected Controller    pump
    ${connected_controller_txt}=       Convert To String    ${connected_controller}
    Random Pause
    Log To Console                     Connected controller to pump is - ${connected_controller_txt}
    Random Pause
    Should Contain                     ${connected_controller_txt}    BloodMD

Test Regression - Pressure In Cuff
    [Documentation]                    Test the difference between the resultant pressure and the additional pressure
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    ${additional_pump_pressure}=       Pump Pumping     pump
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Random Pause
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    Random Pause
    ${result}=                         Evaluate    ${result_pressure} - ${additional_pump_pressure}
    Should Be Equal As Numbers         ${target_pressure}    ${result}    User did not get the target pressure value

Test Regression - Additional Pressure
    [Documentation]                    Test that the pressure inside the pump is present after pumping
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${additional_pump_pressure} > 0    There is no additional pump pressure

Test Regression - Pressure In Cuff More Than Additional
    [Documentation]                    Test that the pressure in cuff is more then additional
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Random Pause
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${result_pressure} > ${additional_pump_pressure}

Test Regression - Power Adapter Efficiency
    [Documentation]                    Test that the expected efficiency is 80% or more
    ${efficiency}=                     DCAdapter Get Efficiency    power_adapter
    Random Pause
    Log To Console                     Power adapter efficiency is - ${efficiency}
    Should Be True                     ${efficiency} >= 0.2

Test Regression - Connected Cuff Class
    [Documentation]                    Test the connected cuff class is InflatableCuff
    ${cuff}=                           Pump Get Connected Cuff    pump
    Random Pause
    ${cuff_txt}=                       Convert To String    ${cuff}
    Random Pause
    Log To Console                     Connected cuff is - ${cuff_txt}
    Should Contain                     ${cuff_txt}    InflatableCuff

Test Regression - Power Source Voltage Limit
    [Documentation]                    Test that power source voltage limit is 240.1
    ${voltage_limit}=                  DCPowerSupply Get Voltage Limit    power_source
    Random Pause
    Log To Console                     Power source voltage limit is - ${voltage_limit}
    Random Pause
    Should Be Equal As Numbers         ${voltage_limit}    240.1

Test Regression - Power Source Current Limit
    [Documentation]                    Test that power source current limit is 6.1
    ${current_limit}=                  DCPowerSupply Get Current Limit    power_source
    Random Pause
    Log To Console                     Power source current limit is - ${current_limit}
    Random Pause
    Should Be Equal As Numbers         ${current_limit}    6.1

Test Regression - Target Pressure Value
    [Documentation]                    Test that target pressure is more then 200
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Random Pause
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    Should Be True                     ${target_pressure} > 200

Test Regression - Minimum Pump Power
    [Documentation]                    Test the minimum required pump power level
    ${min_power}=                      Pump Get Min Power    pump
    Random Pause
    Log To Console                     Minimum required power level for the pump is - ${min_power}
    Random Pause
    Should Be True                     ${min_power} > 0

Test Regression - Pump Connected Controller
    [Documentation]                    Test the connected controller
    ${connected_controller}=           Pump Get Connected Controller    pump
    ${connected_controller_txt}=       Convert To String    ${connected_controller}
    Random Pause
    Log To Console                     Connected controller to pump is - ${connected_controller_txt}
    Random Pause
    Should Contain                     ${connected_controller_txt}    BloodPressureMD

Test Regression - Pressure Inside Cuff
    [Documentation]                    Test the difference between the resultant pressure and the additional pressure
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    ${additional_pump_pressure}=       Pump Pumping     pump
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Random Pause
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    Random Pause
    ${result}=                         Evaluate    ${result_pressure} - ${additional_pump_pressure}
    Should Be Equal As Numbers         ${target_pressure}    ${result}    User did not get the target pressure value

Test Regression - Additional Pressure Inside Cuff
    [Documentation]                    Test that the pressure inside the pump is present after pumping
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${additional_pump_pressure} < 0    There is no additional pump pressure

Test Regression - Pressure Inside Cuff More Than Additional
    [Documentation]                    Test that the pressure in cuff is more then additional
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Random Pause
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${result_pressure} > ${additional_pump_pressure}

Test Regression - Power Adapter Efficiency Level
    [Documentation]                    Test that the expected efficiency is 80% or more
    ${efficiency}=                     DCAdapter Get Efficiency    power_adapter
    Random Pause
    Log To Console                     Power adapter efficiency is - ${efficiency}
    Should Be True                     ${efficiency} >= 0.2

Test Regression - Connected Cuff Class Value
    [Documentation]                    Test the connected cuff class is InflatableCuff
    ${cuff}=                           Pump Get Connected Cuff    pump
    Random Pause
    ${cuff_txt}=                       Convert To String    ${cuff}
    Random Pause
    Log To Console                     Connected cuff is - ${cuff_txt}
    Should Contain                     ${cuff_txt}    InflatableCuff

Test Regression - Power Source Voltage Limit Value
    [Documentation]                    Test that power source voltage limit is 240.1
    ${voltage_limit}=                  DCPowerSupply Get Voltage Limit    power_source
    Random Pause
    Log To Console                     Power source voltage limit is - ${voltage_limit}
    Random Pause
    Should Be Equal As Numbers         ${voltage_limit}    240.1

Test Regression - Power Source Current Limit Value
    [Documentation]                    Test that power source current limit is 6.1
    ${current_limit}=                  DCPowerSupply Get Current Limit    power_source
    Random Pause
    Log To Console                     Power source current limit is - ${current_limit}
    Random Pause
    Should Be Equal As Numbers         ${current_limit}    9.1

Test Regression - Target Pressure Level
    [Documentation]                    Test that target pressure is more then 200
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Random Pause
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    Should Be True                     ${target_pressure} > 200

Test Regression - Min Pump Power
    [Documentation]                    Test the minimum required pump power level
    ${min_power}=                      Pump Get Min Power    pump
    Random Pause
    Log To Console                     Minimum required power level for the pump is - ${min_power}
    Random Pause
    Should Be True                     ${min_power} > 0

Test Regression - Pump Connected Controller Class
    [Documentation]                    Test the connected controller
    ${connected_controller}=           Pump Get Connected Controller    pump
    ${connected_controller_txt}=       Convert To String    ${connected_controller}
    Random Pause
    Log To Console                     Connected controller to pump is - ${connected_controller_txt}
    Random Pause
    Should Contain                     ${connected_controller_txt}    BloodPressureMD

Test Regression - The Pressure In The Cuff
    [Documentation]                    Test the difference between the resultant pressure and the additional pressure
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    ${additional_pump_pressure}=       Pump Pumping     pump
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Random Pause
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    Random Pause
    ${result}=                         Evaluate    ${result_pressure} - ${additional_pump_pressure}
    Should Be Equal As Numbers         ${target_pressure}    ${result}    User did not get the target pressure value

Test Alpha - Pressure In Cuff
    [Documentation]                    Test the difference between the resultant pressure and the additional pressure
    ${target_pressure}=                BloodPressureMD Get Target Pressure    blood_pressure_md
    Log To Console                     Target pressure is - ${target_pressure}
    Random Pause
    ${additional_pump_pressure}=       Pump Pumping     pump
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Random Pause
    ${result_pressure}=                Pump Get Pressure Measurement    pump
    Log To Console                     Pressure inside the cuff is - ${result_pressure}
    Random Pause
    ${result}=                         Evaluate    ${result_pressure} - ${additional_pump_pressure}
    Should Be Equal As Numbers         ${target_pressure}    ${result}    User did not get the target pressure value

Test Alpha - Additional Pressure
    [Documentation]                    Test that the pressure inside the pump is present after pumping
    ${additional_pump_pressure}=       Pump Pumping     pump
    Random Pause
    Log To Console                     Additional pump pressure is - ${additional_pump_pressure}
    Should Be True                     ${additional_pump_pressure} < 0    There is no additional pump pressure
