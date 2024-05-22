from typing import List

import numpy as np


class PID:
    def __init__(self, Kp: float, Ti: float, Td: float, Tp: float = 0.5) -> None:
        self.Kp = Kp
        self.Ti = Ti
        self.Td = Td
        self.Tp = Tp
        self.e = [0.0, 0.0, 0.0]
        self.r0, self.r1, self.r2 = self.calculate_pid_variables()

    def __call__(self, u, y, y_zad):
        return self.main_loop(u, y, y_zad)

    def calculate_pid_variables(self) -> tuple:
        r0 = self.Kp * (1 + (self.Tp / (2 * self.Ti)) + (self.Td / self.Tp))
        r1 = self.Kp * ((self.Tp / (2 * self.Ti)) - 2 * (self.Td / self.Tp) - 1)
        r2 = self.Kp * self.Td / self.Tp
        return r0, r1, r2

    @staticmethod
    def calculate_error(y, y_zad) -> float:
        return y_zad - y

    def calculate_control_signal(self, u) -> float:
        return self.r2 * self.e[-3] + self.r1 * self.e[-2] + self.r0 * self.e[-1] + u

    def set_e(self, y, y_zad) -> None:
        current_e = self.calculate_error(y, y_zad)
        self.e.append(current_e)
        self.e = self.e[-3:]

    def main_loop(self, u, y, y_zad) -> float:
        self.set_e(y, y_zad)
        return self.calculate_control_signal(u)


def main():
    pid = PID(1, 1, 1)


if __name__ == "__main__":
    main()
