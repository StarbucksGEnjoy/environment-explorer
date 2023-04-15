from environment import Environment
from plant import Plant

import random
from math import pi, cos, sin


class Creature():
    def __init__(self, speed:float, size:float, x:int, y:int, detection_range:int, env:Environment=None) -> None:
        self.speed = speed
        self.size = size
        self.x = x
        self.y = y
        self.env = env
        self.detection_range = detection_range
        self.energy = 10
        self.hunger = 10
        self.alive = True
    
    def move(self):
        alpha:float = random.uniform(0, 2*pi)
        self.x = self.x + cos(alpha)*self.speed
        self.y = self.y + sin(alpha)*self.speed

        if self.x > (dim:=self.env.matrix.shape[1]) : self.x = dim
        elif self.x < 0 : self.x = 0

        if self.y > (dim:=self.env.matrix.shape[0]) : self.y = dim
        elif self.y < 0 : self.y = 0

    
    def die(self):
        self.alive=False

    def eat(self, plant:Plant):
        self.hunger = min(0, self.hunger-plant.size)


