from HardwareSensors.FoodLevelSensor import FoodLevelSensor
from SensorService import SensorService

from datetime import datetime


class FoodLevelSensorService(FoodLevelSensor, SensorService):
    def __init__(self, sensor_pin: int, sensor_id: int = None):
        super().__init__(sensor_pin=sensor_pin)
        self._sensor_id = sensor_id

    def set_sensor_id(self, sensor_id: int) -> None:
        self._sensor_id = sensor_id

    def get_measurement_json(self) -> None:
        return f"\{userSensor: {self._sensor_id}, alarmStatus: {self.senses_food()}, measurementValue: {self.senses_food()}, measurementTimestamp: {datetime.now()}\}"
