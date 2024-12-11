""" Setups the environment for the test case """
from typing import Annotated
from devsure.tenv_setup import *
from devsure.tenv_setup.test import fake_devices as fd


class TEnv(TEnvSetup):
    """ Test environment items:

        power_source: DCPowerSupply,
        power_adapter: DCAdapter,
        cuff: InflatableCuff,
        pump: Pump,
        blood_pressure_md: BloodPressureMD

    """
    title = "Test case that exists in three configurations"
    comment = "Demonstrate multiple configurations"
    test_config_default = "siglent"

    power_source: Annotated[
        fd.DCPowerSupply,
        Find(
            comment="Power",
            kwargs={"voltage_limit": 240.1, "current_limit": 6.1}
        )
    ]
    # Find with special requirement
    power_adapter: Annotated[
        fd.DCAdapter,
        Find(
            comment="Agilent DC Power Source",
            uses_config="agilent",
            target_class=fd.DCAdapterAgilent,
            kwargs={
                "input_voltage": 120.0,
                "input_current": 0.12,
                "output_voltage": 6,
                "output_current": 0.5
            },
            need={
                "real_physics": False
            }
        ),
        Find(
            comment="Siglent cool DC Power Source",
            uses_config="siglent",
            target_class=fd.DCAdapterSiglent,
            kwargs={
                "input_voltage": 120.0,
                "input_current": 0.12,
                "output_voltage": 6,
                "output_current": 0.5
            },
            need={
                "real_physics": False
            }
        ),
        Find(
            comment="Cheap default power adapter",
            target_class=fd.DCAdapter,
            kwargs={
                "input_voltage": 120.0,
                "input_current": 0.12,
                "output_voltage": 6,
                "output_current": 0.5
            },
            need={
                "real_physics": False
            }
        )
    ]

    pump: Annotated[
        fd.Pump, Find(
            need={"splitter": True}
        )
    ]

    # Just find whatever is available
    cuff: Annotated[fd.InflatableCuff, Find()]

    # Just create a new instances
    blood_pressure_md: Annotated[fd.BloodPressureMD, Create(kwargs={"target_pressure": 220})]

    def __init__(self) -> None:
        """ Set up the environment for the test case.
        Real devices are usually connected physically,
        here we just create fake devices for demo purposes,
        so we need to connect them in code """

        # ______________________________________________________________________
        # Connect fake devices to each other

        # DC power adapter is connected to electrical power source
        self.power_adapter.connected_power_supply = self.power_source

        # Blood Pressure Measurement Device is connected to the DC power adapter
        self.blood_pressure_md.connected_power = self.power_adapter

        # Pump is connected to the Blood Pressure Measurement Device
        self.pump.connected_controller = self.blood_pressure_md

        # Cuff is connected to the pump
        self.pump.connected_cuff = self.cuff

    def tear_down(self) -> None:
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
