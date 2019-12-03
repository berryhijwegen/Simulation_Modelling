import matplotlib.pyplot as plt

class System(object):
    def __init__(self):
        self.tanks = []

    def add_tank(self, tank):
        self.tanks.append(tank)
    
    def run(self, steps):
        for i in range(steps):
            self.step()
        self.plot()
        
        plt.legend()
        plt.savefig(f'plot_{steps}steps.png')
        plt.show()
    def step(self):
        for tank in self.tanks:
            tank.step()
    
    def plot(self):
        for tank in self.tanks:
            tank.plot()