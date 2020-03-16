from World import World
from Entity import Entity

def init_game(width, height, tickrate):
    Screen.init(width, height)
    World.init(width, height, tickrate)

init_game(500, 500, 60)
ball = Entity(250, 250, 1, 1, 'intro_ball.gif')
World.add_entity(ball)
World.run()
