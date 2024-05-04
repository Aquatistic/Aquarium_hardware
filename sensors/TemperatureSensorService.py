from HardwareSensors.TemperatureSensor import TemperatureSensor
from SensorService import SensorService

from datetime import datetime


class TemperatureSensorService(TemperatureSensor, SensorService):
    def __init__(self, danger_value: float, sensor_id: int = None) -> None:
        super().__init__()
        self._sensor_id = sensor_id
        self._danger_value = danger_value

    def set_sensor_id(self, sensor_id: int) -> None:
        self._sensor_id = sensor_id

    def get_measurement_json(self) -> None:
        temp_reading = self.get_temperature()
        return f"\{userSensor: {self._sensor_id}, alarmStatus: {self._danger_value > temp_reading}, measurementValue: {temp_reading}, measurementTimestamp: {datetime.now()}\}"
