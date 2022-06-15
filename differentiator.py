class Differentiator():
    def __init__(self, sampling_time):
        self.Ts = sampling_time
        self.past_input = 0
        self.past_output = 0
        self.current_input = self.past_input
        self.current_output = self.past_output

    def input(self, data):
        self.current_input = data
        self.current_output = (1/self.Ts) * \
            (self.current_input - self.past_input)
        self.past_input = self.current_input
        self.past_output = self.current_output

    def output(self):
        return self.current_output
