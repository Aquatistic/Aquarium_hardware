from abc import ABC, abstractmethod
from typing import Dict
from datetime import datetime
from threading import Thread


class EffectorService(ABC):
    @abstractmethod
    def activate_effector(self, input_dict: Dict[str, str]) -> None:
        pass
    
    def activate_effector_in_the_future(self, input_dict: Dict[str, str]) -> None:
        while datetime.strptime(input_dict['controllActivationMoment'], "%Y-%m-%d %H:%M:%S") >= datetime.now():
            pass
        self.activate_effector(input_dict)
    
    def send_controll_to_effector(self, input_dict: Dict[str, str]) -> None:
        if datetime.strptime(input_dict['controllActivationMoment'], "%Y-%m-%d %H:%M:%S") <= datetime.now():
            self.activate_effector(input_dict)
            return
        Thread(target=self.activate_effector_in_the_future, args=(input_dict,)).start()
        
    
    def set_effector_id(self, effector_id: int) -> None:
        self._effector_id = effector_id

    def get_effector_id(self) -> int:
        return self._effector_id