from World import World
from Direction import Direction
from Controls_Manager import Controls_Manager
from Game_State import Game_State
import pygame

class Actions:
    @classmethod
    def set_controls(cls):
        Controls_Manager.map_key(pygame.K_w, pygame.KEYDOWN, Game_State.GAME, cls.start_move_up)
        Controls_Manager.map_key(pygame.K_a, pygame.KEYDOWN, Game_State.GAME, cls.start_move_left)
        Controls_Manager.map_key(pygame.K_s, pygame.KEYDOWN, Game_State.GAME, cls.start_move_down)
        Controls_Manager.map_key(pygame.K_d, pygame.KEYDOWN, Game_State.GAME, cls.start_move_right)

        Controls_Manager.map_key(pygame.K_w, pygame.KEYUP, Game_State.GAME, cls.end_move_up)
        Controls_Manager.map_key(pygame.K_a, pygame.KEYUP, Game_State.GAME, cls.end_move_left)
        Controls_Manager.map_key(pygame.K_s, pygame.KEYUP, Game_State.GAME, cls.end_move_down)
        Controls_Manager.map_key(pygame.K_d, pygame.KEYUP, Game_State.GAME, cls.end_move_right)

        Controls_Manager.map_key(pygame.K_SPACE, pygame.KEYUP, Game_State.TITLE_SCREEN, cls.start_game)


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

    @classmethod
    def start_game(cls):
        World.reset_entities()
        World.change_game_state(Game_State.GAME)