from Screen import Screen
import pygame

class Entity:
    def __init__(self, xpos, ypos, xvel, yvel, sprite_filename):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        self.sprite = pygame.image.load(sprite_filename)


    def tick(self):
        self.xpos+= self.xvel
        self.ypos+= self.yvel

    def draw(self):
        Screen.draw_image(self.sprite, int(self.xpos), int(self.ypos))

