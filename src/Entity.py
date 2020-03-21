from Screen import Screen
import pygame

class Entity:
    #figure out how to make sprite scale scale the sprites
    def __init__(self, xpos, ypos, xvel, yvel, sprite_filename=None, sprite_scale=1.0):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        if sprite_filename is not None:
            self.sprite = pygame.image.load(sprite_filename)
        else:
            self.sprite = None

    def tick(self):
        self.xpos+= self.xvel
        self.ypos+= self.yvel

    def draw(self):
        if self.sprite is not None:
            Screen.draw_image(self.sprite, int(self.xpos), int(self.ypos))