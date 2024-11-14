""" Setups the environment for the test case """
from typing import Annotated
from devsure.tenv_setup import *
from devsure.tenv_setup.test import fake_devices as fd


class TEnv(TEnvSetup):
    """ All the items of test environment are listed here """

    power_source: Annotated[
        fd.DCPowerSupply,
        Find(
            comment="Power the schematics",
            kwargs={"voltage_limit": 120.1, "current_limit": 5.1}
        )
    ]
    # Find with special requirement
    motor: Annotated[
        fd.DCMotor,
        Find(
            need={
                "is_brushless": True,
                "real_physics": False
            }
        )]

    # Just find whatever is available
    ventilator: Annotated[fd.Ventilator, Find()]
    adc_temperature: Annotated[fd.ADCVoltage, Find()]
    adc_pressure: Annotated[fd.ADCAmpere, Find()]

    # Just create a new instances
    temperature: Annotated[fd.TemperatureFromVolts, Create(kwargs={"coefficient": 100})]
    pressure: Annotated[fd.PressureFromAmperes, Create(kwargs={"coefficient": 200})]

    def __init__(self):
        """ Setup the environment for the test case.
        Just skip that if not needed (then do not add constructor at all!)
        Real devices are usually connected physically,
        here we just create fake devices for demo purposes,
        so we need to connect them in code """

        # return  #UNCOMMENT ONCE CREATION IS FIXED!

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

    def tear_down(self):
        """ Demo for some useful cleanup, if needed,
        just skip that if not needed

        NOTE: this method is not called automatically,
        you should call it manually in the test case, if needed
        (Call that from those places in your test case
         that correspond to right cleanup location)

        This is just a demo with fake devices, so no real cleanup is needed,
        but in real life you may need to do some cleanup here
        depending on kind of devices you are using
        (or create TEnv instance ONLY ONCE PER PROCESS
         and reuse it for all tests)"""
        pass
