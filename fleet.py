from robot import Robot
#from robot import fleet1



class Fleet:
    def __init__(self, fleet1):
        self.fleet1 = []



    def create_fleet(self):
        robot1 = Robot('Juliana', 10, 1)
        robot2 = Robot('Benjamin', 10, 1)
        robot3 = Robot('Alex', 10, 1)

        self.fleet1.append(robot1)
        self.fleet1.append(robot2)
        self.fleet1.append(robot3)