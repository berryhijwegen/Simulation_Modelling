import matplotlib.pyplot as plt
class Tank(object):
    def __init__(self, name, start_water=100, start_salt=0, line_color="-r"):
        self.name = name

        self.streams_in = []
        self.streams_out = []

        self.total_water = start_water
        self.concentration_over_time = [start_salt / self.total_water] 
        self.times = [0]
        self.total_salt = start_salt

        self.line_color = line_color

    def add_stream_in(self, stream):
        self.streams_in.append(stream)

    def add_stream_out(self, stream):
        self.streams_out.append(stream)

    def step(self):
        curr_step = self.times[-1]

        salt_concentration = self.concentration_over_time[-1]

        # Flow in
        for stream in self.streams_in:
            self.total_water += stream.speed
            self.total_salt += stream.salt_concentration * stream.speed
        
        # Flow out
        for stream in self.streams_out:
            self.total_water -= stream.speed
            self.total_salt -= stream.salt_concentration * stream.speed

        salt_concentration = self.total_salt / self.total_water

        # Set new time
        curr_step += 1

        # Add values to results
        self.times.append(curr_step)
        self.concentration_over_time.append(salt_concentration)

        # Update streams
        for stream in [*self.streams_in,*self.streams_out]:
            stream.update()
    

    def get_salt_concentration(self):
        return self.concentration_over_time[-1]

    def plot(self):
        plt.plot(self.times, self.concentration_over_time, self.line_color, label=self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()