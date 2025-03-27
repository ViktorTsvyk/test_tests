""" Setups the environment for the test case """
from devsure.tenv_setup import Find, Create, TEnvSetup
from devsure.tenv_setup.test import fake_devices as fd


class TEnv(TEnvSetup):
    """ Test environment items:

        power_source: PowerUnit,
        electrodes: Electrodes,
        switch: Switch,
        speaker: Speaker,
        microprocessor: Microprocessor,
        capacitor: Capacitor,
        defibrillator: Defibrillator
    """

    power_source: fd.PowerUnit = Find(
        comment="Power supply for the Defibrillator",
        kwargs={"voltage_limit": 440.2, "current_limit": 30.2}
    )
    # Find with special requirement
    electrodes: fd.Electrodes = Find(
        comment="Electrodes for the Defibrillator",
        kwargs={"thickness": 1.2},
        need={
            "real_physics": False
        }
    )

    # Just find whatever is available
    switch: fd.Switch = Find()
    speaker: fd.Speaker = Find()
    microprocessor: fd.Microprocessor = Find()

    # Just create a new instances
    capacitor: fd.Capacitor = Create()
    defibrillator: fd.Defibrillator = Create()

    def __init__(self) -> None:
        """ Set up the environment for the test case.
        Real devices are usually connected physically,
        here we just create fake devices for demo purposes,
        so we need to connect them in code """

        # ______________________________________________________________________
        # Connect fake devices to each other

        # Capacitor is connected to the power unit (power source)
        self.capacitor.connected_power_supply = self.power_source

        # Capacitor is connected to the electrodes
        self.capacitor.connected_electrodes = self.electrodes

        # Microprocessor is connected to the power unit (power source)
        self.microprocessor.connected_power_supply = self.power_source

        # Microprocessor is connected to the electrodes
        self.microprocessor.connected_electrodes = self.electrodes

        # Microprocessor is connected to the capacitor
        self.microprocessor.connected_capacitor = self.capacitor

        # Microprocessor is connected to the switch
        self.microprocessor.connected_switch = self.switch

        # Microprocessor is connected to the speaker
        self.microprocessor.connected_speaker = self.speaker

        # Defibrillator is connected to the electrodes
        self.defibrillator.connected_electrodes = self.electrodes

        # Defibrillator is connected to the microprocessor
        self.defibrillator.connected_microprocessor = self.microprocessor
