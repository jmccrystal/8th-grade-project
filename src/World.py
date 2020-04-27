from Screen import Screen
from Controls_Manager import Controls_Manager
from Player import Player
from Boulder_Spawner import Boulder_Spawner
from Score import Score
from Game_State import Game_State
import time, pygame

class World:
    @classmethod
    def init(cls, width, height, tickrate):
        cls.width = width
        cls.height = height
        size = width, height
        cls.tickrate = tickrate
        cls.state = Game_State.TITLE_SCREEN

    @classmethod
    def add_entity(cls, entity):
        cls.entities.append(entity)

    @classmethod
    def tick(cls):
        for entity in cls.entities:
            entity.tick()
        if cls.boulder_spawner.is_intersecting_boulder(cls.player):
            cls.on_player_intersect_boulder()

    @classmethod
    def draw(cls):
        Screen.fill_screen((0, 0, 0))
        for entity in cls.entities:
            entity.draw()
        cls.display_score()
        Screen.screen_update()
        

    @classmethod
    def run(cls):
        sleep_time = 1/cls.tickrate
        while True:
            Controls_Manager.handle_events(cls.state)
            if cls.state == Game_State.GAME:
                cls.tick()
                cls.draw()
            elif cls.state == Game_State.TITLE_SCREEN:
                cls.show_title_screen()
            elif cls.state == Game_State.DEATH_SCREEN:
                cls.show_death_screen()
            time.sleep(sleep_time)

    @classmethod
    def on_player_intersect_boulder(cls):
        Score.reset_score()
        World.change_game_state(Game_State.DEATH_SCREEN)

    @classmethod
    def display_score(cls):
        Screen.draw_text(str(Score.get_score()), 10, 10, (255,255,255))

    @classmethod
    def change_game_state(cls, new_game_state):
        if cls.state == new_game_state:
            raise Error()
        if new_game_state == Game_State.TITLE_SCREEN:
            if cls.state is not Game_State.DEATH_SCREEN:
                raise Error()
        elif new_game_state == Game_State.GAME:
            pass
        elif new_game_state == Game_State.DEATH_SCREEN:
            if cls.state is not Game_State.GAME:
                raise Error()
        cls.state = new_game_state

    @classmethod
    def reset_entities(cls):
        cls.player = Player(cls.width/2, cls.height/2)
        cls.boulder_spawner = Boulder_Spawner(5, 25)
        cls.entities = [cls.player, cls.boulder_spawner]

    @classmethod
    def show_title_screen(cls):
        Screen.fill_screen((0,100,100))
        Screen.draw_text("Dodge the Space Garbage!", Screen.get_width() // 2 - 250, Screen.get_height() // 2 - 10, (255,255,255))
        Screen.draw_text("Press the spacebar to begin.", Screen.get_width() // 2 - 250, Screen.get_height() // 2 + 40, (255,255,255))
        Screen.screen_update()

    @classmethod
    def show_death_screen(self):
        Screen.fill_screen((150, 0, 0))
        Screen.draw_text("You Died! Press spacebar to play again, or T to go to the title screen.", Screen.get_width() // 2 - 470, Screen.get_height() // 2 - 10, (255,255,255))
        Screen.screen_update()
