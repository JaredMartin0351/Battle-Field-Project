from robot import Robot



robo1 = Robot
robo2 = Robot
robo3 = Robot




class Fleet:
    def __init__(self):
        fleet1 = [robo1, robo2, robo3]



    def create_fleet(self):
        fleet1 = []
        robo1.name_robo1(robo1)
        fleet1.append(robo1)
        #robo1.robo1_weapon_select(self)
        robo2.name_robo2(robo2)
        fleet1.append(robo2)
        #robo2.robo2_weapon_select(self)
        robo3.name_robo3(robo3)
        fleet1.append(robo3)
        #robo3.robo3_weapon_select(self)
        #self.fleet1.append(robo1)
        #self.fleet1.append(robo2)
        #self.fleet1.append(robo3)
        print(fleet1)




