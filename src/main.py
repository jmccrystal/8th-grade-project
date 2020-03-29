from World import World
from Screen import Screen
from Entity import Entity
from Actions import Actions
from Boulder import Boulder
import pygame

def init_game(width, height, tickrate):
    Screen.init(width, height)
    World.init(width, height, tickrate)
    Actions.set_controls()



init_game(1000, 750, 60)
pygame.display.set_caption('Boulder Dodge!')
World.run()