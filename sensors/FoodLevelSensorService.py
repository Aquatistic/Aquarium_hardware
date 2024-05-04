from sensors.HardwareSensors.FoodLevelSensor import FoodLevelSensor
from sensors.SensorService import SensorService

from datetime import datetime


class FoodLevelSensorService(FoodLevelSensor, SensorService):
    def __init__(self, sensor_pin: int, sensor_id: int = None, measurement_period: float = 5.0):
        super().__init__(sensor_pin=sensor_pin)
        self._sensor_id = sensor_id
        self._measurement_period = measurement_period

    def get_measurement_json(self) -> None:
        return f"\{userSensor: {self._sensor_id}, alarmStatus: {self.senses_food()}, measurementValue: {self.senses_food()}, measurementTimestamp: {datetime.now()}\}"
    
    def _run_measurements(self) -> None:
        while True:
            loop_start = time()
            if self._backend_interactor:
                self._backend_interactor.send_measurement(self.get_measurement_json())
            while time() - loop_start < self._readings_period:
                pass
