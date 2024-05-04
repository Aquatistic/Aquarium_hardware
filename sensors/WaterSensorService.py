from sensors.HardwareSensors.WaterLevelSensor import WaterLevelSensor
from sensors.SensorService import SensorService

from datetime import datetime


class WaterSensorService(WaterLevelSensor, SensorService):
    def __init__(
        self,
        echo_pin: int,
        trigger_pin: int,
        sensor_id: int = None,
        alarm_water_level: float = 0.1,
        measurement_period: float = 5.0
    ):
        super().__init__(echo_pin=echo_pin, trigger_pin=trigger_pin)
        self._sensor_id = sensor_id
        self._alarm_water_level = alarm_water_level
        self._measurement_period = measurement_period

    def get_measurement_json(self) -> None:
        water_level = self.get_water_level()
        return f"\{userSensor: {self._sensor_id}, alarmStatus: {self._alarm_water_level > water_level}, measurementValue: {water_level}, measurementTimestamp: {datetime.now()}\}"
    
    def _run_measurements(self) -> None:
        while True:
            loop_start = time()
            if self._backend_interactor:
                self._backend_interactor.send_measurement(self.get_measurement_json())
            while time() - loop_start < self._readings_period:
                pass
