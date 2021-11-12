from robot import Robot



robo1 = Robot
robo2 = Robot
robo3 = Robot




class Fleet:
    def __init__(self):
        self.fleet1 = []



    def create_fleet(self):
        robo1.name_robo1(robo1)
        robo1.robo1_weapon_select()
        robo2.name_robo2(robo2)
        robo2.robo2_weapon_select()
        robo3.name_robo3(robo3)
        robo3.robo3_weapon_select()
        self.fleet1.append(robo1)
        self.fleet1.append(robo2)
        self.fleet1.append(robo3)




