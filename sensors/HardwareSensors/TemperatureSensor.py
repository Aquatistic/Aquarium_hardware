from w1thermsensor import W1ThermSensor

TEMPERATURE_OFFSET = -10.0


class TemperatureSensor:
    def __init__(self):
        self._probe = W1ThermSensor()

    def get_temperature(self) -> float:
        return self._probe.get_temperature() + TEMPERATURE_OFFSET


if __name__ == "__main__":
    sensor = TemperatureSensor()
    print(sensor.get_temperature())
