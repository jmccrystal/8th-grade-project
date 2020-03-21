from Entity import Entity
from Direction import Direction
import pygame

class Boulder(Entity):
    def __init__(self, x, y, xvel, yvel):
        super().__init__(x, y, xvel, yvel, 'boulder.png')