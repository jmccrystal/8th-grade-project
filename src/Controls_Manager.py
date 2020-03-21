import pygame,sys

class Controls_Manager:

    keys_down = {}
    key_up_controls = {}
    key_down_controls = {}

    @classmethod
    def handle_events(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                cls.keys_down[event.key] = False
                if event.key in cls.key_up_controls:
                    action = cls.key_up_controls[event.key]
                    action()
            if event.type == pygame.KEYDOWN:
                cls.keys_down[event.key] = True
                if event.key in cls.key_down_controls:
                    action = cls.key_down_controls[event.key]
                    action()

    @classmethod
    def is_key_down(cls, key):
        if key not in cls.keys_down:
            return False
        else:
            return cls.keys_down[key]

    @classmethod
    def map_key(cls, key, event_type, action):
        if event_type == pygame.KEYUP:
            cls.key_up_controls[key] = action
        if event_type == pygame.KEYDOWN:
            cls.key_down_controls[key] = action
