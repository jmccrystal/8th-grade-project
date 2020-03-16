from Screen import Screen
import time, pygame

class World:
    @classmethod
    def init(cls, width, height, tickrate):
        cls.width = width
        cls.height = height
        size = width, height
        cls.entities = []
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            cls.tick()
            cls.draw()
            time.sleep(sleep_time)