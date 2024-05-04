from typing import List
from time import time
import requests

class SensorsBackendInteractors:
    def __init__(self, backend_destination: str, send_period: float):
        self._backend_destination = backend_destination
        self._send_period = send_period
        self._measurements = []
        
    def send_measurement(self, measurement: dict, sensor_id: int):
        self._measurements.append({"first": measurement, "second": sensor_id })
        
    def run(self):
        while True:
            loop_start = time()
            requests.post(self._backend_destination, json=self._measurements)
            print(self._measurements)
            self._measurements = []
            while time() - loop_start < self._send_period:
                pass