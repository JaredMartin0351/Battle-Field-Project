from weapon import Weapon



class Robot:
    
    def __init__(self, name, hp, weapon):
        self.name = ('Juliana')
        self.hp = hp
        #self.atk = ()
        self.weapon = weapon
    
    def attack(self, enemy):
        if enemy.hp > self.weapon:
            enemy.hp = enemy.hp - self.weapon
        else:
            enemy.hp = 0

        




    robot_1 = ('Juliana', 10, 1)
    robot_2 = ('Benjamin', 10, 1)
    robot_3 = ('Alex', 10, 1)

    fleet1 = [robot_1, robot_2, robot_3]
