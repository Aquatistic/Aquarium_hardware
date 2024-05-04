from HardwareSensors.WaterLevelSensor import WaterLevelSensor
from SensorService import SensorService

from datetime import datetime


class WaterSensorService(WaterLevelSensor, SensorService):
    def __init__(
        self,
        echo_pin: int,
        trigger_pin: int,
        sensor_id: int = None,
        alarm_water_level: float = 0.1,
    ):
        super().__init__(echo_pin=echo_pin, trigger_pin=trigger_pin)
        self._sensor_id = sensor_id
        self._alarm_water_level = alarm_water_level

    def set_sensor_id(self, sensor_id: int) -> None:
        self._sensor_id = sensor_id

    def get_measurement_json(self) -> None:
        water_level = self.get_water_level()
        return f"\{userSensor: {self._sensor_id}, alarmStatus: {self._alarm_water_level > water_level}, measurementValue: {water_level}, measurementTimestamp: {datetime.now()}\}"
