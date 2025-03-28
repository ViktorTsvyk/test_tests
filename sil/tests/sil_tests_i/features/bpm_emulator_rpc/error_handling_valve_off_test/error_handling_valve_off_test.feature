Feature: Test error handling valve off

  @BPMFR050
  @TC-000002
  @bpm_emulator_rpc
  Scenario: Test error handling with valve off
    Given Start bpm emulator rpc
    When Click button ok
    Then Verify button Perform a measurement is selected
    When Click button ok
    When Click button Down
    When Click button ok
    When Device waiting 5000 milliseconds
    When Turn off the valve
    Then Wait until perform measurement finished
    Then Verify screen contains text ERROR
    Then Verify screen contains text Pressure remains unchanged