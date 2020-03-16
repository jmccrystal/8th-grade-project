from World import World
from Direction import Direction
from Controls_Manager import Controls_Manager
import pygame

class Actions:
    @classmethod
    def set_controls(cls):
        Controls_Manager.map_key(pygame.K_w, pygame.KEYDOWN, cls.start_move_up)
        Controls_Manager.map_key(pygame.K_a, pygame.KEYDOWN, cls.start_move_left)
        Controls_Manager.map_key(pygame.K_s, pygame.KEYDOWN, cls.start_move_down)
        Controls_Manager.map_key(pygame.K_d, pygame.KEYDOWN, cls.start_move_right)

        Controls_Manager.map_key(pygame.K_w, pygame.KEYUP, cls.end_move_up)
        Controls_Manager.map_key(pygame.K_a, pygame.KEYUP, cls.end_move_left)
        Controls_Manager.map_key(pygame.K_s, pygame.KEYUP, cls.end_move_down)
        Controls_Manager.map_key(pygame.K_d, pygame.KEYUP, cls.end_move_right)


    @classmethod
    def start_move_up(cls):
        World.player.start_move(Direction.UP)

    @classmethod
    def end_move_up(cls):
        World.player.end_move(Direction.UP)

    @classmethod
    def start_move_right(cls):
        World.player.start_move(Direction.RIGHT)

    @classmethod
    def end_move_right(cls):
        World.player.end_move(Direction.RIGHT)

    @classmethod
    def start_move_down(cls):
        World.player.start_move(Direction.DOWN)

    @classmethod
    def end_move_down(cls):
        World.player.end_move(Direction.DOWN)

    @classmethod
    def start_move_left(cls):
        World.player.start_move(Direction.LEFT)

    @classmethod
    def end_move_left(cls):
        World.player.end_move(Direction.LEFT)