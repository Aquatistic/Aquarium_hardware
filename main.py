from backend_interactors.SensorsBackendInteractors import SensorsBackendInteractors
from sensors.WaterSensorService import WaterSensorService


if __name__ == "__main__":
    sensors = [WaterSensorService(23, 22, 1)]
    backend = SensorsBackendInteractors("http://192.168.0.190:6868/api/v1/measurements/add", 10.0)
    for sensor in sensors:
        sensor.set_backend_interactor(backend)
        sensor.run()
    backend.run()
    