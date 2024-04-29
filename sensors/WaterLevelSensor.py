from gpiozero import DistanceSensor
from time import sleep


class WaterLevelSensor:
    def __init__(self, echo_pin: int, trigger_pin: int) -> None:
        self._distance_sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin)
        self._base_level = self._distance_sensor.distance

    def get_water_level(self) -> float:
        return -(self._distance_sensor.distance - self._base_level) * 100

    def reset_sensor(self) -> None:
        self._base_level = self._distance_sensor.distance


if __name__ == "__main__":
    sensor = WaterLevelSensor(23, 22)
    while True:
        print("Distance: ", sensor.get_water_level())
        sleep(1)
