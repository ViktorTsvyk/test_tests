""" Describe PRC interface for the Emulator """

import unittest
import os

from .tenv import TEnv
from devsure.rpc.test.rpc_to_bpm_emu.bpm_emulator_rpc import PinState

from devsure.time_simulator import time_runner
from devsure.time_simulator.simulation import SimulatedTimeScope, simulated_sleep_ms

from datetime import datetime


class TestConnectionEstablished(unittest.TestCase):
    def setUp(self) -> None:
        """ Setup execution environment """
        # Simulation must restart before Emulators will use it
        time_runner.reset_to_initial_state()

        # Emulators also init here
        self.tenv = TEnv.setUpUnittest(self)

        self.start_emulation_statuses = (
            self.tenv.emulator.emulator_start_emulation(),
            self.tenv.emulator_second.emulator_start_emulation(),
        )

    def test_emulator_loaded(self):
        self.assertEqual(self.start_emulation_statuses, (0, 0), msg="Emulators shall start normally")

        emu_first = self.tenv.emulator
        emu_second = self.tenv.emulator_second

        self.enterContext(SimulatedTimeScope("test_emulator_loaded"))

        print(f"Test started at {time_runner.current_time_ms}")

        # let display bytes to arrive for sure
        simulated_sleep_ms(200)

        print(f"Checking for display at {time_runner.current_time_ms}")

        remember_refreshes_1 = emu_first.display_refreshes
        remember_refreshes_2 = emu_second.display_refreshes
        self.assertGreater(remember_refreshes_1, 0, msg="There shall be display refreshes since start")
        self.assertGreater(remember_refreshes_2, 0, msg="There shall be display refreshes since start")

        simulated_sleep_ms(1000)

        new_refreshes_1 = emu_first.display_refreshes
        new_refreshes_2 = emu_second.display_refreshes
        self.assertEqual(
            new_refreshes_1, remember_refreshes_1, "There shall be no display refreshes while no buttons were pressed"
        )
        self.assertEqual(
            new_refreshes_2, remember_refreshes_2, "There shall be no display refreshes while no buttons were pressed"
        )

        emu_first.click_pin(PinState.ButtonOk)
        emu_second.click_pin(PinState.ButtonOk)
        print(f"After first click ")

        new_refreshes_1 = emu_first.display_refreshes
        new_refreshes_2 = emu_second.display_refreshes
        print(f"{new_refreshes_1=}, {remember_refreshes_1=}")
        print(f"{new_refreshes_2=}, {remember_refreshes_2=}")
        self.assertGreater(new_refreshes_1, remember_refreshes_1, msg="There shall be display refreshes after ButtonOk")
        self.assertGreater(new_refreshes_2, remember_refreshes_2, msg="There shall be display refreshes after ButtonOk")
        remember_refreshes_1 = new_refreshes_1
        remember_refreshes_2 = new_refreshes_2

        # Where to store captured images
        report_folder = os.environ.get("DEVSURE_REPORT_FOLDER", os.getcwd())

        start_real_time = datetime.now()
        start_virtual_time = time_runner.current_time_ms

        # Code to measure
        for i in range(100):
            emu_first.click_pin(PinState.ButtonDown)
            emu_second.click_pin(PinState.ButtonUp)

            # Save captured image
            emu_first.screen_image.save(f"{report_folder}/Emu1_Image{i}.png")
            emu_second.screen_image.save(f"{report_folder}/Emu2_Image{i}.png")

            new_refreshes_1 = emu_first.display_refreshes
            new_refreshes_2 = emu_second.display_refreshes
            if i % 30 == 0:
                print(f"{new_refreshes_1=}, {remember_refreshes_1=}")
                print(f"{new_refreshes_2=}, {remember_refreshes_2=}")

            self.assertGreater(
                new_refreshes_1, remember_refreshes_1, msg="There shall be display refreshes while buttons were pressed"
            )
            self.assertGreater(
                new_refreshes_2, remember_refreshes_2, msg="There shall be display refreshes while buttons were pressed"
            )
            remember_refreshes_1 = new_refreshes_1
            remember_refreshes_2 = new_refreshes_2

            simulated_sleep_ms(200)

        end_real_time = datetime.now()
        end_virtual_time = time_runner.current_time_ms

        print(
            f"{new_refreshes_1=}\n"
            f"{new_refreshes_2=}\n"
            f"Elapsed time: {(end_real_time - start_real_time).total_seconds()} seconds\n"
            f"Virtual time: {(end_virtual_time - start_virtual_time)/1000} seconds"
        )
