from Screen import Screen
import pygame

class Entity:
    def __init__(self, xpos, ypos, xvel, yvel, sprite_filename=None, sprite_scale=1):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        if sprite_filename is not None:
            self.sprite = pygame.image.load(sprite_filename)
            width = self.sprite.get_size()[0]
            height = self.sprite.get_size()[1]
            self.sprite = pygame.transform.scale(self.sprite, (int(width*sprite_scale), int(height*sprite_scale)))
            print(sprite_scale)
        else:
            self.sprite = None
        


    def tick(self):
        self.xpos+= self.xvel
        self.ypos+= self.yvel

    def draw(self):
        if self.sprite is not None:
            Screen.draw_image(self.sprite, int(self.xpos), int(self.ypos))