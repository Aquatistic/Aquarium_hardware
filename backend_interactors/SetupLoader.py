import json
from typing import Dict, List
from sensors.WaterSensorService import WaterSensorService
from sensors.TemperatureSensorService import TemperatureSensorService
from sensors.FoodLevelSensorService import FoodLevelSensorService
from effectors.LedStripService import LedStripService
from effectors.SwitchModuleService import SwitchModuleService
from effectors.FeederService import FeederService


def generate_sensors_from_list(sensor_description_list: List[Dict[str, str]]):
    sensors = []
    for sensor_description in sensor_description_list:
        try:
            match sensor_description["type"]:
                case "temperature":
                    sensors.append(TemperatureSensorService(35, sensor_description["sensor_id"]))
                    continue
                case "water_level":
                    sensors.append(WaterSensorService(23, 22, sensor_description["sensor_id"]))
                    continue
                case "food_level":
                    sensors.append(FoodLevelSensorService(21, sensor_description["sensor_id"]))
                    continue
        except:
            pass
    return sensors
            

def generate_effectors_from_list(effector_description_list: List[Dict[str, str]]):
    effectors = []
    for effector_description in effector_description_list:
        try:
            match effector_description["type"]:
                case "led_strip":
                    effectors.append(LedStripService(effector_description["effector_id"], 18, 14, 15))
                    continue
                case "switch":
                    effectors.append(SwitchModuleService(26, effector_description["effector_id"]))
                    continue
                case "feeder":
                    effectors.append(FeederService(effector_description["effector_id"], [12, 5, 6, 13]))
                    continue
        except :
            pass
    return effectors


def load_setup_from_dict(input_data: Dict[str, str]):
    return generate_effectors_from_list(data["effectors"]), generate_sensors_from_list(data["sensors"])


if __name__ == "__main__":
    with open('start_config.json') as f:
        data = json.load(f)
    print(data)
    print(type(data))
    print(load_setup_from_dict(data))