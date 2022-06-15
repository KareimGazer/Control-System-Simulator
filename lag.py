class Lag():
    def __init__(self, sampling_time):
        self.Ts = sampling_time
        self.past_input = 0
        self.past_output = 0
        self.current_input = self.past_input
        self.current_output = self.past_output

    def input(self, data):
        y_est = self.past_output + self.Ts * \
            (self.past_input + self.past_output)
        self.current_input = data
        self.current_output = self.past_output + \
            (self.Ts/2) * ((self.current_input - y_est) +
                           (self.past_input - self.past_output))
        self.past_input = self.current_input
        self.past_output = self.current_output

    def output(self):
        return self.current_output
