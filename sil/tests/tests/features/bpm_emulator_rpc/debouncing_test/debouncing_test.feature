Feature: Test debouncing

  @BPMFR011
    @TC-000001
    @bpm_emulator_rpc
  Scenario Outline: Test debouncing time with different waiting durations
    Given Start bpm emulator rpc
    Then Verify button Enter menu is selected
    When Click button Ok
    When Press button Down
    When Device waiting <waitingTime> milliseconds
    When Release button Down
    When Device waiting <waitingTime> milliseconds
    Then Verify button <activeButton> is selected

    Examples:
      | waitingTime | activeButton          |
      | 39          | Perform a measurement |
      | 40          | Measurement history   |
      | 41          | Measurement history   |
