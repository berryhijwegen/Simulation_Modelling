from tank import Tank
class Stream(object):
    def __init__(self, speed, from_tank):
        self.speed = speed
        
        if type(from_tank) == Tank:
            self.from_tank = from_tank
        else:
            self.from_tank = False
            self.salt_concentration = from_tank
        self.update()

    def update(self):
        if self.from_tank:
            self.salt_concentration = self.from_tank.get_salt_concentration()