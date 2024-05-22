from effectors.HardwareEffectors.SwitchModule import SwitchModule
from effectors.EffectorService import EffectorService
from typing import Dict


class SwitchModuleService(EffectorService):
    def __init__(self, control_pin: int, effector_id: int) -> None:
        self._switch_module = SwitchModule(control_pin)
        self._effector_id = effector_id
        
    def activate_effector(self, input_dict: Dict[str, str]) -> None:
        if bool(input_dict["value"]):
            self._switch_module.on()
        else:
            self._switch_module.off()