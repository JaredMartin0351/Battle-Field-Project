from weapon import Weapon



# These methods will name the robots and assign the name to each one and then should create weapons and assign them as well.

class Robot:
    fleet1 = []
    wep = Weapon
    ro1wep = Weapon
    ro2wep = Weapon
    ro3wep = Weapon
    
    
  
    
    
    def __init__(self, name, hp, weapon):
        self.name = name
        self.hp = hp
        #self.atk = ()
        self.weapon = weapon

    def name_robo1(self, name, hp, weapon):
        name = 'Jared'
        hp = 10
        print(name)
        weapon = input('Please select your weapon  of choice: ''' '[1 for Broad Sword], [2 for Laser Gun] or [3 for Buzz Saw]')
        if weapon == '1':
            print('Broad Sword, you must be feeling brave')
        elif weapon == '2':
            print('Laser Gun, someone is feeling a little scared to get close today huh?')
        else:
            weapon == '3'
            print('Buzz Saw.... now you are just crazy!!')
        return weapon

    def name_robo2(self, name, hp, weapon):
        name= 'Casandra'
        hp = 10
        print(name)
        weapon = input('Please select your weapon  of choice: ''' '[1 for Broad Sword], [2 for Laser Gun] or [3 for Buzz Saw]')
        if weapon == '1':
            print('Broad Sword, you must be feeling brave')
        elif weapon == '2':
            print('Laser Gun, someone is feeling a little scared to get close today huh?')
        else:
            weapon == '3'
            print('Buzz Saw.... now you are just crazy!!')
        return weapon

    def name_robo3(self, name, hp, weapon):
        name = 'Juliana'
        hp = 10
        print(name)
        weapon = input('Please select your weapon  of choice: ''' '[1 for Broad Sword], [2 for Laser Gun] or [3 for Buzz Saw]')
        if weapon == '1':
            print('Broad Sword, you must be feeling brave')
        elif weapon == '2':
            print('Laser Gun, someone is feeling a little scared to get close today huh?')
        else:
            weapon == '3'
            print('Buzz Saw.... now you are just crazy!!')
        return weapon
    


        #self.fleet1.append
        print(name)
        return self

  







    
    
    

        



