from backend_interactors.SensorsBackendInteractors import SensorsBackendInteractors
from backend_interactors.EffectorBackendInteractor import EffectorBackendInteractors
from backend_interactors.SetupLoader import load_setup_from_dict
from threading import Thread
import json

def main():
    with open('start_config.json') as f:
        input_data = json.load(f)
    effectors, sensors = load_setup_from_dict(input_data)
    sensor_backend = SensorsBackendInteractors(
        input_data["host_url"] + "/api/v1/measurements/add", 10.0
    )
    for sensor in sensors:
        sensor.set_backend_interactor(sensor_backend)
        sensor.run()
    backend_thread = Thread(target= sensor_backend.run)
    backend_thread.start()
    
    effector_backend = EffectorBackendInteractors(input_data["host_url"] + f"/api/v1/userEffector/connect/{input_data['aquarium_id']}", effectors)
    effector_backend.run()


if __name__ == "__main__":
    main()
