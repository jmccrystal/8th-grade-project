import pygame,sys

class Controls_Manager:

    keys_down = {}

    @classmethod
    def handle_events(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                cls.keys_down[event.key] = False
            if event.type == pygame.KEYDOWN:
                cls.keys_down[event.key] = True

    @classmethod
    def is_key_down(cls, key):
        if key not in cls.keys_down:
            return False
        else:
            return cls.keys_down[key]