from abc import ABC, abstractmethod


class EffectorService(ABC):
    @abstractmethod
    def activate_effector(self) -> None:
        pass
    
    def set_effector_id(self, effector_id: int) -> None:
        self._effector_id = effector_id

    def get_effector_id(self) -> int:
        return self._effector_id