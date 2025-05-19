""" Setups the environment for the test case """
from devsure.tenv_setup import Find, Create, TEnvSetup
from devsure.tenv_setup.test import fake_devices as fd


class TEnv(TEnvSetup):
    """ All the items of test environment are listed here """

    power_source: fd.DCPowerSupply = Find(
        comment="Power the schematics",
        kwargs={"voltage_limit": 120.1, "current_limit": 5.1}
    )
    # Find with special requirement
    motor: fd.DCMotor = Find(
        need={
            "is_brushless": True,
            "real_physics": False
        }
    )

    # Just find whatever is available
    ventilator: fd.Ventilator = Find()
    adc_temperature: fd.ADCVoltage = Find()
    adc_pressure: fd.ADCAmpere = Find()

    # Just create a new instances
    temperature: fd.TemperatureFromVolts = Create(kwargs={"coefficient": 100})
    pressure: fd.PressureFromAmperes = Create(kwargs={"coefficient": 200})

    def setup(self):
        """ Setup the environment for the test case.
        Just skip that if not needed (then do not add constructor at all!)
        Real devices are usually connected physically,
        here we just create fake devices for demo purposes,
        so we need to connect them in code """

        # ______________________________________________________________________
        # Connect fake devices to each other
        # (such "modeling" in NOT based on phycical laws,
        #  university professors will cry if they see that:))

        # motor is connected to electrical power source
        self.motor.connected_power_supply = self.power_source
        # Note: self.motor.load_torque is established by the test case itself

        # ventilator is rotated by the motor
        self.ventilator.connected_power = self.motor
        # adc for temperature is measuring the heat from the ventilator
        self.adc_temperature.connected_measurement = self.ventilator.heat
        # adc for pressure is measuring the pressure created by the ventilator
        self.adc_pressure.connected_measurement = self.ventilator.pressure

        # ______________________________________________________________________
        # two below are likely to be present in real life
        # just because one still needs to convert the measured values
        # (naturally there are no real "calibration tables" here, just imitation)

        # temperature is calculated from the measured voltage
        self.temperature.connected_voltage = self.adc_temperature
        # pressure is calculated from the measured amperage
        self.pressure.connected_amperage = self.adc_pressure
