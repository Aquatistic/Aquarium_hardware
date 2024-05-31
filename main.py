from backend_interactors.SensorsBackendInteractors import SensorsBackendInteractors
from sensors.WaterSensorService import WaterSensorService
from sensors.TemperatureSensorService import TemperatureSensorService
from effectors.LedStripService import LedStripService
from effectors.SwitchModuleService import SwitchModuleService
from backend_interactors.EffectorBackendInteractor import EffectorBackendInteractors
from threading import Thread


if __name__ == "__main__":
    sensors = [TemperatureSensorService(35, 1), WaterSensorService(23, 22, 2)]
    backend = SensorsBackendInteractors(
        "http://192.168.0.190:6868/api/v1/measurements/add", 10.0
    )
    for sensor in sensors:
        sensor.set_backend_interactor(backend)
        sensor.run()
    backend_thread = Thread(target= backend.run)
    backend_thread.start()

    effectors = [SwitchModuleService(26, 2), LedStripService(1, 18, 14, 15)]
    backend = EffectorBackendInteractors("http://192.168.0.190:6868/api/v1/userEffector/connect/1", effectors)
    backend.run()
