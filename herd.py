from dino import Dino
#from dino import herd1



class Herd:
    def __init__(self, herd1):
        self.herd1 = []



    def create_herd(self):
        dino1 = Dino('Jared', 15, 2)
        dino2 = Dino('Casandra', 15, 2)
        dino3 = Dino('Torrence', 15, 2)

        self.herd1.append(dino1)
        self.herd1.append(dino2)
        self.herd1.append(dino3)
