# (177, 52, 235) purple

import pygame, random
from p5 import *

class Rain:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.yspeed = 0.5

    def draw_rain(self):
        Line(self.screen, (177, 52, 235), (self.x, self.y), (self.x, self.y + 10), 2)

    def fall(self):
        self.y += self.yspeed
        if self.y > 300:
            self.y = random.randint(-300, 0)
