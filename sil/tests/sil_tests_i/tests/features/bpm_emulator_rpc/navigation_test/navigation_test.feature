Feature: Test menu navigation

  @BPMFR011, @BPMFR012, @BPMFR013, @BPMFR014, @BPMFR015
  @TC-000003
  @bpm_emulator_rpc
  Scenario: Test menu navigation
    Given Start bpm emulator rpc
    Then Verify button Enter menu is selected
    When Click button ok
    Then Verify button Perform a measurement is selected
    When Click button ok
    Then Verify screen contains text Measurement
    When Click button ok

    When Click button down
    Then Verify button Measurement history is selected
    When Click button ok
    Then Verify screen contains text History
    When Click button ok

    When Click button down
    When Click button down
    Then Verify button Visit our site is selected
    When Click button ok
    Then Verify screen contains text Visit our site
    When Click button ok

    When Click button down
    When Click button down
    When Click button down
    Then Verify button Exit is selected
    When Click button ok
    Then Verify button Enter menu is selected
