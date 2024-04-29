from gpiozero import PWMOutputDevice, DigitalOutputDevice


class LedStrip:
    def __init__(
        self,
        first_enable_pin: int,
        second_enable_pin: int,
        pwm_pin: int,
        max_pwm: float = 1.0,
    ) -> None:
        self.first_enable_pin = first_enable_pin
        self.second_enable_pin = second_enable_pin
        self.pwm_pin = pwm_pin
        self._pwm_output = PWMOutputDevice(pwm_pin)
        self._second_enable_output = DigitalOutputDevice(second_enable_pin)
        self._first_enable_output = DigitalOutputDevice(first_enable_pin)
        self.turn_off()
        self.max_pwm = max_pwm

    def turn_off(self):
        self._first_enable_output.off()
        self._second_enable_output.off()

    def set_brightness(self, brightness: float) -> None:
        if brightness <= 0:
            self.turn_off()
            return
        if brightness > 0:
            self._first_enable_output.on()
            self._second_enable_output.off()
        self._pwm_output.value = min(abs(brightness), self.max_pwm)
        print(self._pwm_output.value)


if __name__ == "__main__":
    led_strip = LedStrip(18, 14, 15)
    led_strip.set_brightness(0.8)
