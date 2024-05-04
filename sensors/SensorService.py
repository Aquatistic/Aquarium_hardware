from abc import ABC, abstractmethod


class SensorService(ABC):
    @abstractmethod
    def get_measurement_json(self) -> str:
        pass

    @abstractmethod
    def set_sensor_id(self, sensor_id: int) -> None:
        pass
    
    def get_sensor_id(self) -> int"
    return self._sensor_id