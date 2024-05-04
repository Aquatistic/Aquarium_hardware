from sensors.SensorService import SensorService
from typing import List
from time import time

class SensorsBackendInteractors:
    def __init__(self, sensors: List[SensorService], backend_destination: str, readings_period: float):
        self._sensors = sensors
        self._backend_destination = backend_destination
        self._readings_period = readings_period
        
    def send_measurement(self, measurement: str):
        pass
        
    def run(self):
        while True:
            loop_start = time()
            measurement_message = "["
            for sensor in self._sensors:
                measurement_message += sensor.get_measurement_json() + ", "
            measurement_message += "]"
            requests.post(self._backend_destination, json=measurement_message)
            while time() - loop_start < self._readings_period:
                pass