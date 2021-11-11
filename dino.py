from weapon import Weapon




class Dino:
    shape = 'Triangle'
    
    def __init__(self, name, hp, atk):
        self.name = ('Jared')
        self.hp = hp
        self.atk = atk
    
    def attack(self, enemy):
        if enemy.hp > self.atk:
            enemy.hp = enemy.hp - self.atk
        else:
            enemy.hp = 0





    dino_1 = ('Jared', 15, 2)
    dino_2 = ('Casandra', 15, 2)
    dino_3 = ('Torrence', 15, 2)

    herd1 = [dino_1, dino_2, dino_3]