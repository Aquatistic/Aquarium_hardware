from typing import List

import numpy as np


class PID:
    def __init__(self, Kp: float, Ti: float, Td: float) -> None:
        self.Kp = Kp
        self.Ti = Ti
        self.Td = Td
        self.e = [0, 0, 0]
        self.x1 = 0  # to be removed
        self.x2 = 0  # to be removed
        self.u = self.get_current_control_signal()
        self.y = self.get_current_y()
        self.y = self.get_current_setpoint()
        self.Tp = 0.5  # to be calculated dynamically?
        self.r0, self.r1, self.r2 = self.calculate_pid_variables()

    @staticmethod
    def get_current_control_signal() -> List[float]:
        """This method is used at the beginning or when there is a change between manual and auto.
        Current Implementation is temporary. Used only in constructor"""
        return [0, 0, 0, 0, 0]

    def get_current_y(self) -> float:
        """This should be loaded from raspberry pi - temporary implementation
        In my case it would be function that will make it easy to test PID"""
        alpha1 = -1.489028
        alpha2 = 0.535261
        beta1 = 0.012757
        beta2 = 0.010360
        g1 = np.exp(7.5 * self.u[-5] - 1) / np.exp(7.5 * self.u[-5] + 1)
        x1 = -alpha1 * self.x1 + self.x2 + beta1 * g1
        x2 = -alpha2 * self.x1 + beta2 * g1
        self.x1 = x1
        self.x2 = x2
        return 1.2 * (1 - np.exp(-1.5 * self.x1)).item()

    def calculate_pid_variables(self) -> tuple[float]:
        r0 = self.Kp * (1 + (self.Tp / (2 * self.Ti)) + (self.Td / self.Tp))
        r1 = self.Kp * ((self.Tp / (2 * self.Ti)) - 2 * (self.Td / self.Tp) - 1)
        r2 = self.Kp * self.Td / self.Tp
        return r0, r1, r2

    @staticmethod
    def get_current_setpoint() -> float:
        """Fetched from user"""
        return 0.3

    def calculate_error(self) -> float:
        return self.y - self.y_zad

    def calculate_control_signal(self) -> float:
        return (
            self.r2 * self.e[-3] + self.r1 * self.e[-2] + self.r0 * self.e[-1] + self.u
        )

    def set_u(self) -> None:
        current_u = self.calculate_control_signal()
        new_u_list = self.u.append(current_u)
        self.u = new_u_list[-5:]

    def set_e(self) -> None:
        current_e = self.calculate_error()
        new_e_list = self.e.append(current_e)
        self.e = new_e_list[-3:]

    def main_loop(self) -> None:
        self.set_current_y()
        r0, r1, r2 = self.calculate_pid_variables()
        self.set_e()
        self.set_u()


def main():
    pid = PID(1, 1, 1)


if __name__ == "__main__":
    main()
