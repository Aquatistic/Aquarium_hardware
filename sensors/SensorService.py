from abc import ABC, abstractmethod

class SensorService(ABC):
    @abstractmethod
    def get_measurement_json() -> str:
        pass
    
    @abstractmethod
    def set_sensor_id(sensor_id: int) -> None:
        pass
    