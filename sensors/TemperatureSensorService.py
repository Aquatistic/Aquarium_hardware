from sensors.HardwareSensors.TemperatureSensor import TemperatureSensor
from sensors.SensorService import SensorService

from datetime import datetime


class TemperatureSensorService(TemperatureSensor, SensorService):
    def __init__(
        self,
        danger_value: float,
        sensor_id: int = None,
        measurement_period: float = 10.0,
    ) -> None:
        super().__init__()
        self._sensor_id = sensor_id
        self._danger_value = danger_value
        self._measurement_period = measurement_period

    def get_measurement_json(self) -> None:
        temp_reading = self.get_temperature()
        return {
            "userSensor": self._sensor_id,
            "alarmStatus": self._danger_value > temp_reading,
            "measurementValue": temp_reading,
            "measurementTimestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
