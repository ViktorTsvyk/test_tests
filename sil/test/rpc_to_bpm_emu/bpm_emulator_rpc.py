""" Describe PRC interface for the Emulator
 Just run that file (Ctrl+Shift+F10 in PyCharm)
 And BpmEmulatorRpc.h, BpmEmulatorRpc.cpp will refresh))
 """
import os
from enum import IntFlag
from functools import partial
from typing import Annotated, Final
from devsure.rpc.rpc_to_emulator import RpcToEmulator, rpc_class, rpc_local, rpc_remote, serializable

from devsure.util.image_convertor import bytes_as_png, image_to_base64, Image
from devsure.webserver.web_interface import WebInterface

# TODO: use time_simulator instead!!!
from threading import Condition
import time


__all__ = [
    'PinState',  # Flags that correspond to the pins
    'BpmEmulatorRpc' 
]


# Control if web interface is allowed
DEVSURE_ALLOW_WEB_INTERFACE: Final[bool] = bool(os.environ.get("DEVSURE_ALLOW_WEB_INTERFACE", False))


class PinState(IntFlag):
    """ Set of digital pins """
    Default = 0
    # Pins that can be set (order according to FW behavior)
    ButtonDown = 1 << 0
    ButtonOk = 1 << 1
    ButtonUp = 1 << 2


@serializable
class InterruptInfo:
    """ Information about the interrupts,
    that arrives when we await in the idle state
    Each call to wait_in_idle_state returns:
    - "current time"
    - "interrupts triggered this time"
    - "current pin state"

    """

    # Remember when filling in the fields:
    # types must match python types declared in the annotations!

    # Current time in ticks (time arrives even if there is no "time interrupt")
    time_ticks: Annotated[int, 'uint64_t']

    # Mask with any interrupts triggered this time
    # 1 means interrupt triggered, "other side" will | (bitor) them to currently pending
    # (interrupt will happen "there" immediately as )
    pending_interrupts: Annotated[int, 'uint64_t']

    # Current "PIN state" (not all are used)
    pin_state: Annotated[int, 'uint64_t']


@rpc_class
class BpmEmulatorRpc(RpcToEmulator):
    """ Sample class to be generated as RPC API """

    pending_interrupts: int = 0

    # Pins as visible by device
    _pin_state: PinState = PinState.Default
    # number of times display was refreshed
    _display_refreshes: int = 0
    # _screen_bytes: bytes | None = None
    _screen_image: Image | None = None
    _condition: Condition = Condition()

    _web_interface: WebInterface | None = None

    def __init__(self, *, path_to_emulator: str, port_for_communication: int | None = None):
        """ Custom setup if any is needed """

        if DEVSURE_ALLOW_WEB_INTERFACE:
            self._init_web_interface()

        # Start Emulator only after web interface was shown!
        super().__init__(
            path_to_emulator=path_to_emulator,
            port_for_communication=port_for_communication
        )

        self.pending_interrupts = 0
        self._pin_state = PinState.Default
        self._display_refreshes = 0
        # self._screen_bytes = None
        self._screen_image = None  # No image at start

    if DEVSURE_ALLOW_WEB_INTERFACE:
        def _init_web_interface(self):
            self._web_interface = web = WebInterface()

            for button, pin in PinState.__members__.items():
                web.subscribe(
                    button,
                    partial(self._handle_web_button, pin=pin)
                )

            web.subscribe(
                "Refresh",
                self._handle_refresh
            )

            web.run_in_background()

        def _handle_web_button(self, ws, pin):
            self.click_pin(pin)

        def _handle_refresh(self, ws):
            print("########################### REFRESH ###########################")
            if self.screen_image:
                self._web_interface.display_image(
                    image_to_base64(self.screen_image)
                )

    def add_interrupt(self, interrupt: int):
        """ Add interrupt to the pending list """
        with self._condition:
            self.pending_interrupts |= 1 << interrupt
            self._condition.notify_all()

    @property
    def pin_state(self) -> PinState:
        """ Get pin state """
        with self._condition:
            return self._pin_state
        
    @pin_state.setter
    def pin_state(self, pin_state: PinState):
        """ Set pin state """
        print(f"### pin_state NEW requested {self._pin_state}")
        with self._condition:
            self._pin_state = pin_state
            self._condition.notify_all()
            print(f"### pin_state exit with self._pin_state = {self._pin_state}")

    def set_pin(self, pin: PinState):
        """ Set pin """
        with self._condition:
            self._pin_state |= pin
            self._condition.notify_all()

    def clear_pin(self, pin: PinState):
        """ Clear pin """
        with self._condition:
            self._pin_state &= ~pin
            self._condition.notify_all()

    def toggle_pin(self, pin: PinState):
        """ Toggle pin """
        print(f"Enter: toggle_pin for {pin}")
        with self._condition:
            self._pin_state ^= pin
            self._condition.notify_all()
            print(f"Exit: toggle_pin for {pin} self._pin_state = {self._pin_state}")

    def click_pin(self, pin: PinState):
        """ Simulate click sequence for button synchronously """
        self.set_pin(pin)
        time.sleep(1.5)
        self.clear_pin(pin)
        time.sleep(1)  # Wait for screen refresh

    @property
    def display_refreshes(self) -> int:
        """ Get number of times display was refreshed """
        with self._condition:
            return self._display_refreshes

    # @property
    # def screen_bytes(self) -> bytes | None:
    #     """ The last received screen image """
    #     with self._condition:
    #         return self._screen_bytes

    @property
    def screen_image(self) -> Image | None:
        """ The last received screen image """
        with self._condition:
            return self._screen_image

    # __________________________________________________________________________
    # API implemented on our (framework) side but called from C++

    @rpc_local
    def framework_wait_in_idle_state(self) -> InterruptInfo:
        """ Wait in idle state until interrupt arrives """
        with self._condition:
            # print("framework_wait_in_idle_state waning")
            self._condition.wait(0.010)
            # uncomment below to observe button states
            print(f"framework_wait_in_idle_state returning {repr(self.pin_state)}")
            return InterruptInfo(
                int(time.time()*1000),  # Must be integer to go through serialization!
                self.pending_interrupts,
                int(self.pin_state)  # Must be integer to go through serialization!
            )
    
    # Dimensions of the screen as being sent by the emulator
    SCREEN_W: Final[int] = 480
    SCREEN_H: Final[int] = 320
    BYTES_PER_COLOR: Final[int] = 3

    @rpc_local
    def framework_display_screen(
        self,
        screen_bytes: Annotated[bytes, 'char', SCREEN_W * SCREEN_H * BYTES_PER_COLOR],
    ):
        """ TODO: """
        print(
            "------------------\n"
            f"framework_display_screen Displaying screen... of {len(screen_bytes)} int")

        image = bytes_as_png(screen_bytes, self.SCREEN_W, self.SCREEN_H)

        if self._web_interface is not None:
            self._web_interface.display_image(
                image_to_base64(image)
            )
        print("------------------\n")

        with self._condition:
            self._display_refreshes += 1
            # self._screen_bytes = screen_bytes
            self._screen_image = image
            # self._condition.notify_all()

        print("framework_display_screen finished ------------------\n")

    # __________________________________________________________________________
    # API implemented on C++ side but is called from our side

    @rpc_remote
    def emulator_start_emulation(self) -> Annotated[int, 'uint32_t']:
        """ Start actual emulation in loaded emulator """

    @rpc_remote
    def emulator_stop_emulation(self) -> None:
        """ Stop actual emulation in loaded emulator """

    @rpc_remote
    def emulator_echo(self, value: int) -> int:
        """ Return the same value back
         NOTE: when not annotated for "just int" int32_t is assumed
               Use Annotated[int, '(u)int<8|16|32|64>_t'] to specify exact type
         """
