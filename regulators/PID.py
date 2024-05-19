import numpy as np


class PID:
    def __init__(self, Kp: float, Ti: float, Td: float) -> None:
        self.Kp = Kp
        self.Ti = Ti
        self.Td = Td

    @staticmethod
    def get_current_control_signal(self):
        """ This method is used at the beginning or when there is a change between manual and auto.
            Current Implementation is temporary. Used only in constructor  """
        return 0

    def get_current_y(self, k: int, x1_prev, x2_prev) -> np.ndarray:
        """This should be loaded from raspberry pi - temporary implementation
            In my case it would be function that will make it easy to test PID"""
        alpha1 = -1.489028;
        alpha2 = 0.535261;
        beta1 = 0.012757;
        beta2 = 0.010360;
        g1 = np.exp(7.5 * self.u(max(k - 5)) - 1) / np.exp(7.5 * self.u(max(k - 5)) + 1)
        x1 = -alpha1 * x1_prev + x2_prev + beta1 * g1;
        x2 = -alpha2 * x1_prev + beta2 * g1
        return 1.2 * (1 - np.exp(-1.5 * x1))


def main():
    pid = PID(1, 1, 1)


if __name__ == "__main__":
    main()
