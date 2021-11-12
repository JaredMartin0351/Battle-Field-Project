from weapon import Weapon





class Robot:
    
    
    def __init__(self, name, hp, weapon):
        self.name = ''
        self.hp = 10
        #self.atk = ()
        self.weapon = 0

    def name_robo1(self):
        robo1 = input('Please name your first robot: ')
        return self.name

    def name_robo2(self):
        robo2 = input('Please name your second robot: ')
        return self.name

    def name_robo3(self):
        robo3 = input('Please name your third robot: ')
        return self.name

    def robo1_weapon_select(self):
        robowep1 = Weapon
        robowep1.weapon_select1()
        return robowep1

    def robo2_weapon_select(self):
        robowep2 = Weapon
        robowep2.weapon_select2()
        return robowep2

    def robo3_weapon_select(self):
        robowep3 = Weapon
        robowep3.weapon_select3()
        return robowep3


    
    
    

        



