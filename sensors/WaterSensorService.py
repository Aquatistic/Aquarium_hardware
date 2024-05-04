from sensors.HardwareSensors.WaterLevelSensor import WaterLevelSensor
from sensors.SensorService import SensorService

from time import time
from datetime import datetime


class WaterSensorService(WaterLevelSensor, SensorService):
    def __init__(
        self,
        echo_pin: int,
        trigger_pin: int,
        sensor_id: int = None,
        alarm_water_level: float = 0.1,
        measurement_period: float = 30.0
    ):
        super().__init__(echo_pin=echo_pin, trigger_pin=trigger_pin)
        self._sensor_id = sensor_id
        self._alarm_water_level = alarm_water_level
        self._measurement_period = measurement_period

    def get_measurement_json(self) -> None:
        water_level = self.get_water_level()
        return {"userSensorId": self._sensor_id, "alarmStatus": self._alarm_water_level > water_level, "measurementValue": water_level, "measurementTimestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

