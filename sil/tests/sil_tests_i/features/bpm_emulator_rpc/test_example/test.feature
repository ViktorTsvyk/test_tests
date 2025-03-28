Feature: Test debug issue


  @bpm_emulator_rpc
  Scenario: Test debug issue
    Given Start bpm emulator rpc
    Then Step 1 execution
    Then Verify button Enter menu is selected
    When Device waiting 1 milliseconds
    Then Step 2 execution
    Then Verify button Enter menu is selected
    When Device waiting 50 milliseconds
    Then Step 3 execution
    Then Verify button Enter menu is selected
    When Device waiting 100 milliseconds
    Then Step 4 execution
    Then Verify button Enter menu is selected
    When Device waiting 1000 milliseconds
    Then Step 5 execution
    Then Verify button Enter menu is selected
    When Device waiting 2000 milliseconds
    Then Step 6 execution
    When Click button ok
    Then Verify button Perform a measurement is selected
    When Click button ok
    When Click button Down
    When Click button ok
    When Device waiting 5000 milliseconds
    Then Verify screen contains text Please wait
    Then Verify screen contains text measurement in progress
    Then Verify pressure in the cuff displaying
    Then Step 8 execution
    When Turn off the valve
    Then Step 9 execution
    Then Wait until perform measurement finished
    Then Step 10 execution
