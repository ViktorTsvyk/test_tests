Feature: Test perform measurement functionality

  @BPMFR017, @BPMFR020
  @TC-000004
  @bpm_emulator_rpc
  Scenario: Test
    Given Start bpm emulator rpc
    Then Verify button Enter menu is selected
    When Click button ok
    Then Verify button Perform a measurement is selected
    When Click button ok
    When Click button Down
    Then Verify button Start is selected
    When Click button ok
    When Device waiting 2000 milliseconds
    Then Verify button Stop is selected
    Then Verify screen contains text Please wait
    Then Verify screen contains text measurement in progress
    Then Verify pressure in the cuff displaying
    Then Wait until perform measurement finished
    Then Verify measurement result: SYS equal to 120, DIA equal to 80; With deviation uf 5 units