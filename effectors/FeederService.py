from effectors.HardwareEffectors.Feeder import Feeder
from effectors.EffectorService import EffectorService
from typing import Dict, List


class FeederService(Feeder, EffectorService):
    def __init__(self, effector_id, control_pins: List[int], number_of_control_pins: int = 4):
        super().__init__(control_pins, number_of_control_pins)
        self._effector_id = effector_id
        
    def activate_effector(self, input_dict: Dict[str, str]) -> None:
        self.dispense(float(input_dict["value"]*250))
        
