from Screen import Screen
from Hit_Circle import Hit_Circle
import pygame

class Entity:
    def __init__(self, xpos, ypos, xvel, yvel, hit_radius, sprite_filename=None, sprite_scale=1):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        self.hit_circle = Hit_Circle(hit_radius, self)
        if sprite_filename is not None:
            self.sprite = pygame.image.load(sprite_filename)
            width = self.sprite.get_size()[0]
            height = self.sprite.get_size()[1]
            self.sprite = pygame.transform.scale(self.sprite, (int(width*sprite_scale), int(height*sprite_scale)))
        else:
            self.sprite = None
        
    def get_x_pos(self):
        return self.xpos

    def get_y_pos(self):
        return self.ypos

    def get_hit_circle(self):
        return self.hit_circle

    def tick(self):
        self.xpos+= self.xvel
        self.ypos+= self.yvel

    def draw(self):
        if self.sprite is not None:
            Screen.draw_image(self.sprite, int(self.xpos), int(self.ypos))