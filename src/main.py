from World import World
from Screen import Screen
from Entity import Entity
from Actions import Actions
from Boulder import Boulder

def init_game(width, height, tickrate):
    Screen.init(width, height)
    World.init(width, height, tickrate)
    Actions.set_controls()

init_game(1000, 1000, 60)
World.run()
