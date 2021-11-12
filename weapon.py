






class Weapon:
    def __init__(self):
        self.BS = ''
        self.LG = ''
        self.BZ = ''

    def choose_weapon(self, wepch):
        print('Weapon choices are: [1: for Broad Sword]  [2: for Laser Gun]  [3: for Buzz Saw]')
        wepch = input('Please choose your weapon: ')
        return wepch
       
