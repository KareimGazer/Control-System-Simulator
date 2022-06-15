import numpy as np


class DeadTime():
    def __init__(self, sampling_time, delay_time):
        self.size = delay_time // sampling_time
        self.buffer = np.zeros(self.size)
        self.p_in = 0
        self.p_out = 0

    def input(self, data):
        self.buffer[self.p_in] = data
        self.p_in = (self.p_in + 1) % self.size
        self.p_out = (self.p_out + 1) % self.size

    def outpt(self):
        return self.buffer[self.p_out]
