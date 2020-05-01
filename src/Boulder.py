from Entity import Entity
from Direction import Direction
import pygame

class Boulder(Entity):
    def __init__(self, x, y, xvel, yvel, boulder_scale):
        super().__init__(x, y, xvel, yvel, 220 * boulder_scale, 'boulder.png', boulder_scale)