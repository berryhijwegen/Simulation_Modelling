import matplotlib.pyplot as plt

class System(object):
    def __init__(self):
        self.tanks = []

    def add_tank(self, tank):
        self.tanks.append(tank)
    
    def run(self, steps):
        for tank in self.tanks:
            for i in range(steps):
                tank.step()
            tank.plot()
        
        plt.legend()
        plt.show()