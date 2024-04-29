from gpiozero import DigitalOutputDevice


class SwitchModule(DigitalOutputDevice):
    def __init__(self, control_pin) -> None:
        super().__init__(control_pin)
        

if __name__ == "__main__":
    from time import sleep
    module = SwitchModule(26)
    module.on()
    sleep(2)
    module.off()
        