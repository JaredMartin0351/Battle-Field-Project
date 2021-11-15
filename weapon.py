




class Weapon:
    def __init__(self, name, wepatk):
        self.name = name
        self.wepatk = wepatk
        
    def weapon_choice(self):
        wep1 = Weapon('Sword', 3)
        wep2 = Weapon('Laser', 3)
        weapon_choice = input('Please choose your weapon: [1] for Sword or [2] for Laser: ')
        if weapon_choice == '1':
            return wep1
        elif weapon_choice == '2':
            return wep2
        else:
            print('Fine, I guess I will choose')
            return wep1
 

        
        
    
    
 


       
