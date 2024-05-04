from abc import ABC, abstractmethod
from backend_interactors.SensorsBackendInteractors import SensorsBackendInteractors
from threading import Thread


class SensorService(ABC):
    @abstractmethod
    def get_measurement_json(self) -> str:
        pass

    def set_sensor_id(self, sensor_id: int) -> None:
        return self._sensor_id
    
    def get_sensor_id(self) -> int:
        return self._sensor_id
    
    def set_backend_interactor(self, backedn_interactor: SensorsBackendInteractors) -> None:
        self._backend_interactor = backedn_interactor
    
    def run(self) -> Thread:
        worker = Thread(self._run_measurements)
        worker.start()
        return worker
    
    @abstractmethod
    def _run_measurements(self):
        pass
    