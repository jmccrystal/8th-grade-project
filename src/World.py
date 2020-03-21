from Screen import Screen
from Controls_Manager import Controls_Manager
from Player import Player
from Boulder_Spawner import Boulder_Spawner
import time, pygame

class World:
    @classmethod
    def init(cls, width, height, tickrate):
        cls.width = width
        cls.height = height
        size = width, height
        cls.player = Player(width/2, height/2)
        cls.boulder_spawner = Boulder_Spawner(5, 1)
        cls.entities = [cls.player, cls.boulder_spawner]
        cls.tickrate = tickrate

    @classmethod
    def add_entity(cls, entity):
        cls.entities.append(entity)

    @classmethod
    def tick(cls):
        for entity in cls.entities:
            entity.tick()

    @classmethod
    def draw(cls):
        Screen.fill_screen((0, 0, 0))
        for entity in cls.entities:
            entity.draw()
        Screen.screen_update()

    @classmethod
    def run(cls):
        sleep_time = 1/cls.tickrate
        while True:
            Controls_Manager.handle_events()
            cls.tick()
            cls.draw()
            time.sleep(sleep_time)