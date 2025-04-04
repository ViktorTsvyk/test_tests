Feature: Test perform measurement functionality

  @BPMFR019
  @TC-000005
  @bpm_emulator_rpc
  Scenario: Test stop measurement
    Given Start bpm emulator rpc
    Then Verify button Enter menu is selected
    When Click button ok
    Then Verify button Perform a measurement is selected
    When Click button ok
    When Click button Down
    Then Verify button Start is selected
    When Click button ok
    When Click button ok
    Then Verify screen contains text Measurement was stopped
