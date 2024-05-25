from sensors.HardwareSensors.FoodLevelSensor import FoodLevelSensor
from sensors.SensorService import SensorService

from datetime import datetime


class FoodLevelSensorService(FoodLevelSensor, SensorService):
    def __init__(
        self, sensor_pin: int, sensor_id: int = None, measurement_period: float = 30.0
    ):
        super().__init__(sensor_pin=sensor_pin)
        self._sensor_id = sensor_id
        self._measurement_period = measurement_period

    def get_measurement_json(self) -> dict:
        return {
            "alarmStatus": self.senses_food(),
            "measurementValue": self.senses_food(),
            "measurementTimestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
