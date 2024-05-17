from gpiozero import DigitalOutputDevice
from typing import List
from time import time, sleep

DEFAULT_STEP_SEQUENCE = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]
STEP_SLEEP = 0.001


class Feeder:
    def __init__(self, control_pins: List[int], number_of_control_pins: int = 4):
        self._control_pins = [
            DigitalOutputDevice(pin) for pin in control_pins[:number_of_control_pins]
        ]
        self.reset_state()

    def reset_state(self):
        for pin in self._control_pins:
            pin.off()

    def _wait_for_step_finish(self):
        step_start = time()
        while time() - step_start < STEP_SLEEP:
            pass

    def _rotate(self, number_of_steps: int, pins_list: List[DigitalOutputDevice]):
        for step in range(number_of_steps):
            for pin, pin_value in zip(
                pins_list, DEFAULT_STEP_SEQUENCE[step % len(DEFAULT_STEP_SEQUENCE)]
            ):
                pin.value = pin_value
            self._wait_for_step_finish()

    def dispense(self, number_of_steps: int):
        self._rotate(number_of_steps, self._control_pins)

    def reverse(self, number_of_steps: int):
        self._rotate(number_of_steps, list(reversed(self._control_pins)))


if __name__ == "__main__":
    feeder = Feeder([12, 5, 6, 13])
    feeder.dispense(4096)
    feeder.reverse(4096)
    feeder.reset_state()
