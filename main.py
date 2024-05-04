from backend_interactors.SensorsBackendInteractors import SensorsBackendInteractors
from sensors.WaterSensorService import WaterSensorService
import threading

if __name__ == "__main__":
    backend = SensorsBackendInteractors([WaterSensorService(23, 22, 1)], "http://192.168.0.190:6868/api/v1/measurements/add", 2.0)
    thread = threading.Thread(backend.run)
    thread.start()
    