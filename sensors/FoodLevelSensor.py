from gpiozero import DigitalInputDevice
from time import sleep


class FoodLevelSensor:
    def __init__(self, sensor_pin: int) -> None:
        self._sensor_input = DigitalInputDevice(sensor_pin)
        # in the future we can override when activated
    
    def senses_food(self) -> bool:
        return not bool(self._sensor_input.value)
    

if __name__ == "__main__":
    sensor = FoodLevelSensor(21)
    while(True):
        print(sensor.senses_food())
        sleep(1)
    
