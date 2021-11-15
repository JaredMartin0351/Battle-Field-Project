import time
import random
from dino import Dino
from herd import Herd
from fleet import Fleet
from robot import Robot
from weapon import Weapon

dino1 = Dino('Dino: Jared', 12, 2)
dino2 = Dino('Dino: Casandra', 12, 2)
dino3 = Dino('Dino: Torrence', 12, 2)

robo1 = Robot('Robot: Benjamin', 10, 3)
robo2 = Robot('Robot: Juliana', 10, 3)
robo3 = Robot('Robot: Alex', 10, 3)

wep1 = Weapon('Sword', 3)
wep2 = Weapon('Laser', 3)

herd = [dino1, dino2, dino3]
fleet = [robo1, robo2, robo3]     

class Battlefield:
        def __init__(self, fleet, herd, wep1, wep2):
                self.fleet = Fleet.create_fleet(fleet)
                self.herd = Herd.create_herd(herd)
                self.wep1 = Weapon.weapon_choice(self)
                self.wep2 = Weapon.weapon_choice(self)
                
                
class Fight:
        def enter(self):
                print('Three robots and 3 Dinos enter the dome... only one team may leave')
                temp = vars(dino1)
                for item in temp:
                        print(item, ':',temp[item]), #time.sleep(.5)
        
                temp = vars(dino2)
                for item in temp:
                        print(item, ':',temp[item]), #time.sleep(.5)
        
                temp = vars(dino3)
                for item in temp:
                        print(item, ':',temp[item]), #time.sleep(.5)
        
                temp = vars(robo1)
                for item in temp:
                        print(item, ':',temp[item]), #time.sleep(.5)
        
                temp = vars(robo2)
                for item in temp:
                        print(item, ':',temp[item]), #time.sleep(.5)
        
                temp = vars(robo3)
                for item in temp:
                        print(item, ':',temp[item]), #time.sleep(.5)
                
                print('Due to rapid internal processors.... the robots attack first')
                
                
        def fight_robo_atk(self, dino):
                self = input('Please choose your attacker: [1] for Benjamin, [2] for Juliana, [3] for Alex: ') 
                if self == 1:
                        self = robo1
                elif self == 2:
                        self = robo2
                else: 
                        self = robo3
                attack = int(input('Type [1] to attack Jared, [2] to attack Cassandra or [3] to attack Torrence: '))
                while self.hp >= 1:
                        if attack == 1:
                                dino1.hp = dino1.hp - self.wepatk
                                print(('Jared has') + str(dino1.hp) + ('hp remaining'))
                                return dino
                        elif attack == 2:
                                dino2.hp = dino2.hp - self.wepatk
                                print(('Cassandra has') + str(dino2.hp) + ('hp remaining'))
                                return dino
                        elif attack == 3:
                                dino3.hp = dino3.hp - self.wepatk
                                print(('Torrence has') + str(dino3.hp) + ('hp remaining'))
                                return dino
                        else:
                                print('You missed!!')
                                return
                return dino      
        def fight_dino_atk(self, robo):
                self = int(input('Please choose your attacker: [1] for Jared, [2] for Casandra, [3] for Torrence: '))
                if self == 1:
                        self = dino1
                elif self == 2:
                        self = dino2
                else: 
                        self = dino3
                attack = int(input('Type 1 to attack Benjamin, 2 to attack Juliana or 3 to attack Alex: '))
                while self.hp >= 1:
                        if attack == 1:
                                robo1.hp = robo1.hp - self.atk
                                print(('Benjamin') + str(robo1.hp) + ('hp remaining'))
                                return robo
                        elif attack == 2:
                                robo2.hp = robo2.hp - self.atk
                                print(('Juliana has') + str(robo2.hp) + ('hp remaining'))
                                return robo
                        elif attack == 3:
                                robo3.hp = robo3.hp - self.atk
                                print(('Alex has') + str(robo3.hp) + ('hp remaining'))
                                return robo
                        else:
                                print('You missed!!')
                                return
                return robo
                        
         
                                    
fight=Fight()
fight.enter()
robofight = fight.fight_robo_atk(fleet)
dinofight = fight.fight_dino_atk(herd)









      








#for item in herd:
#        print (vars(item))
        
           
#for item in fleet:
#        print (vars(item))


      
                



































#temp = vars(dino1)
#for item in temp:
#        print(item, ':',temp[item])
        
#temp = vars(dino2)
#for item in temp:
#        print(item, ':',temp[item])
        
#temp = vars(dino3)
#for item in temp:
#        print(item, ':',temp[item])
        
#temp = vars(robo1)
#for item in temp:
#        print(item, ':',temp[item])
        
#temp = vars(robo2)
#for item in temp:
#        print(item, ':',temp[item])
        
#temp = vars(robo3)
#for item in temp:
#        print(item, ':',temp[item])