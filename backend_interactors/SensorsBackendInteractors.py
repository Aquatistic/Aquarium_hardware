from sensors.SensorService import SensorService
from typing import List
from time import time

class SensorsBackendInteractors:
    def __init__(self, sensors: List[SensorService], backend_destination: str, send_period: float):
        self._sensors = sensors
        self._backend_destination = backend_destination
        self._send_period = send_period
        self._measurements = []
        
    def send_measurement(self, measurement: str):
        self._measurements.append(measurement)
        
    def run(self):
        while True:
            loop_start = time()
            requests.post(self._backend_destination, json=str(self._measurements))
            self._measurements = []
            while time() - loop_start < self._readings_period:
                pass