from solid.utils import *

class assembly():
    trans = [0,0,0]
    rot = [0,0,0]

    def __init__(self):
        self.trans = [0,0,0]
        self.rot = [0,0,0]
    
    # Mate obj1 feature to obj2
    def concentricMate(self, obj1, obj2):
        for i in range(0,3):
            self.trans[i] += obj1.loc[i] - obj2.loc[i]

    def assembly(self):
        self.part.part = translate(self.trans)(self.part.part)
        self.part.part = rotate(self.rot)(self.part.part)
        return self.part.part
