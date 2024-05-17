from effectors.HardwareEffectors.SwitchModule import SwitchModule
from effectors.EffectorService import EffectorService


class SwitchModuleService(SwitchModule, EffectorService):
    def __init__(self, control_pin: int, effector_id: int) -> None:
        super().__init__(control_pin)
        self._effector_id = effector_id
        
    def activate_effector(self, input_dict: Dict[str]) -> None:
        if bool(input_dict["value"]):
            self.on()
        else:
            self.off()