import pygame,sys

class Controls_Manager:

    keys_down = {}
    key_up_controls = {}
    key_down_controls = {}

    @classmethod
    def handle_events(cls, state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                cls.keys_down[event.key] = False
                if (event.key, state) in cls.key_up_controls:
                    action = cls.key_up_controls[(event.key, state)]
                    action()
            if event.type == pygame.KEYDOWN:
                cls.keys_down[event.key] = True
                if (event.key, state) in cls.key_down_controls:
                    action = cls.key_down_controls[(event.key, state)]
                    action()

    @classmethod
    def is_key_down(cls, key):
        if key not in cls.keys_down:
            return False
        else:
            return cls.keys_down[key]

    @classmethod
    def map_key(cls, key, event_type, state, action):
        if event_type == pygame.KEYUP:
            cls.key_up_controls[(key, state)] = action
        if event_type == pygame.KEYDOWN:
            cls.key_down_controls[(key, state)] = action
