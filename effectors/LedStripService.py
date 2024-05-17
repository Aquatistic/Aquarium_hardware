from effectors.HardwareEffectors.LedStrip import LedStrip
from effectors.EffectorService import EffectorService
from typing import Dict


class LedStripService(LedStrip, EffectorService):
    def __init__(self, effector_id: int,first_enable_pin: int,
        second_enable_pin: int,
        pwm_pin: int,
        max_pwm: float = 1.0):
        super().__init__(first_enable_pin, second_enable_pin, pwm_pin, max_pwm)
        self._effector_id = effector_id
        
    def activate_effector(self, input_dict: Dict[str, str]) -> None:
        self.set_brightness(float(input_dict["value"])/100.0)
