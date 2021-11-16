import time
import random
import sys
from dino import Dino
from herd import Herd
from fleet import Fleet
from robot import Robot
from weapon import Weapon

dino1 = Dino('Dino: Jared', 10, 5)
dino2 = Dino('Dino: Casandra', 10, 5)
dino3 = Dino('Dino: Torrence', 10, 5)

robo1 = Robot('Robot: Benjamin', 10, 5)
robo2 = Robot('Robot: Juliana', 10, 5)
robo3 = Robot('Robot: Alex', 10, 5)

wep1 = Weapon('Sword', 3)
wep2 = Weapon('Laser', 3)

herd = [dino1, dino2, dino3]
fleet = [robo1, robo2, robo3]  

counter = 1   

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
                
                
        def fight_robo_atk(self):
                counter = 1
                while counter == 1:
                        if (robo1) and (robo2) and (robo3) .hp <= 0:
                                print('Dinos win')
                                sys.exit()
                        else:
                                self = int(input('Please choose your attacker: [1] for Benjamin, [2] for Juliana, [3] for Alex: '))
                                if self == 1:
                                        self = robo1
                                        if robo1.hp <=0:
                                                print('you are dead')
                                                fight.fight_robo_atk()
                                elif self == 2:
                                        self = robo2
                                        if robo2.hp <= 0:
                                                print('you are dead')
                                                fight.fight_robo_atk()
                                else: 
                                        self = robo3
                                        if robo3.hp <= 0:
                                                print('you are dead')
                                                fight.fight_robo_atk()
                                attack = int(input('Type [1] to attack Jared, [2] to attack Cassandra or [3] to attack Torrence: '))
                                if attack == 1:
                                        if dino1.hp <= 0:
                                                print('that dino is already dead')
                                                fight.fight_dino_atk()
                                        dino1.hp = dino1.hp - self.wepatk
                                        counter = counter - 1
                                        print(('Jared has') + str(dino1.hp) + ('hp remaining'))
                                        fight.fight_dino_atk()
                                elif attack == 2:
                                        if dino2.hp <= 0:
                                                print('that dino is already dead')
                                                fight.fight_dino_atk()
                                        dino2.hp = dino2.hp - self.wepatk
                                        counter = counter - 1
                                        print(('Cassandra has') + str(dino2.hp) + ('hp remaining'))
                                        fight.fight_dino_atk()
                                elif attack == 3:
                                        if dino3.hp <= 0:
                                                print('this dino is already dead')
                                                fight.fight_dino_atk()
                                        dino3.hp = dino3.hp - self.wepatk
                                        counter = counter - 1
                                        print(('Torrence has') + str(dino3.hp) + ('hp remaining'))
                                        fight.fight_dino_atk()
                                else:
                                        print('You missed!!')
                                        fight.fight_dino_atk()
                                
                
        def fight_dino_atk(self):
                counter = 0
                while counter == 0:
                        if (dino1.hp) and (dino2.hp) and (dino3.hp) <=0:
                                end = True
                                print('Robots win')
                                sys.exit()
                                
                        else:
                                self = int(input('Please choose your attacker: [1] for Jared, [2] for Casandra, [3] for Torrence: '))
                                if self == 1:
                                        self = dino1
                                        if dino1.hp <= 0:
                                                print('you are dead')
                                                fight.fight_dino_atk()
                                elif self == 2:
                                        self = dino2
                                        if dino2.hp <= 0:
                                                print('you are dead')
                                                fight.fight_dino_atk()
                                else: 
                                        self = dino3
                                        if dino3.hp <= 0:
                                                print('you are dead')
                                                fight.fight_dino_atk()
                                attack = int(input('Type 1 to attack Benjamin, 2 to attack Juliana or 3 to attack Alex: '))
                                if attack == 1:
                                        if robo1.hp <= 0:
                                                print('that robot is already dead')
                                                fight.fight_robo_atk()
                                        robo1.hp = robo1.hp - self.atk
                                        counter = counter + 1
                                        print(('Benjamin') + str(robo1.hp) + ('hp remaining'))
                                        fight.fight_robo_atk()
                                elif attack == 2:
                                        if robo2.hp <= 0:
                                                print('that robot is already dead')
                                                fight.fight_robo_atk
                                        robo2.hp = robo2.hp - self.atk
                                        counter = counter + 1
                                        print(('Juliana has') + str(robo2.hp) + ('hp remaining'))
                                        fight.fight_robo_atk()
                                elif attack == 3:
                                        if robo3.hp <= 0:
                                                print('that robot is already dead')
                                                fight.fight_robo_atk()
                                        robo3.hp = robo3.hp - self.atk
                                        counter = counter + 1
                                        print(('Alex has') + str(robo3.hp) + ('hp remaining'))
                                        fight.fight_robo_atk()
                                else:
                                        print('You missed!!')
                                        fight.fight_robo_atk()
                                
        
                        
         
                                    
fight=Fight()
fight.enter()
robofight = fight.fight_robo_atk()
dinofight = fight.fight_dino_atk()









      








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