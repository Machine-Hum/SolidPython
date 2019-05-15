from solid import *
from solid.utils import *
import pdb

# SolidPart
class sprt():
    def __init__(self, x, y, z):
        self.size = [x,y,z]
        self.part = cube(size=self.size)
        self.part = color([0,1,0,0.8])(self.part)

# SolidHole
class shole:
    def __init__(self, part, loc, rot, r, hType):
        self.loc = loc
        self.rot = rot
        self.r = r
        self.hType = hType

        h = cylinder(r=r, h=part.size[2]+0.001, center=True)
        h = translate([loc[0], loc[1], part.size[2]/2])(h)
        part.part = part.part - hole()(h)
