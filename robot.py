from weapon import Weapon





class Robot:
    fleet1 = []
    
  
    
    
    def __init__(self, name, hp, weapon):
        self.name = ''
        self.hp = 10
        #self.atk = ()
        self.weapon = 0

    def name_robo1(self):
        name = input('Please name your first robot: ')
        #self.fleet1.append
        return name

    def name_robo2(self):
        name= input('Please name your second robot: ')
        #self.fleet1.append
        return name

    def name_robo3(self):
        name = input('Please name your third robot: ')
        #self.fleet1.append
        return name

    def robo1_weapon_select(self):
        robowep1 = Weapon
        robowep1.weapon_select1(self)
        return robowep1

    def robo2_weapon_select(self):
        robowep2 = Weapon
        robowep2.weapon_select2(self)
        return robowep2

    def robo3_weapon_select(self):
        robowep3 = Weapon
        robowep3.weapon_select3(self)
        return robowep3







    
    
    

        



