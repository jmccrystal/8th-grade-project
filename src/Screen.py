import pygame
from Score import Score

class Screen:
    @classmethod
    def init(cls, width, height):
        pygame.init()
        size = width, height
        cls.screen = pygame.display.set_mode(size)
        cls.font = pygame.font.SysFont('Comic Sans MS', 30)

    @classmethod
    def fill_screen(cls, color):
        cls.screen.fill(color)
    
    @classmethod
    def draw_image(cls, image, x, y, center = True):
        if center:
            cls.screen.blit(image, (x - image.get_width() // 2, y - image.get_height() // 2))
        else:
            cls.screen.blit(image, (x , y))

    @classmethod
    def draw_text(cls, text, x, y, color):
        rendered_text = cls.font.render(text, True, color) 
        cls.screen.blit(rendered_text, (x, y))

    @classmethod
    def screen_update(cls):
        pygame.display.flip()

    @classmethod
    def get_width(cls):
        return pygame.display.get_surface().get_size()[0]

    @classmethod
    def get_height(cls):
        return pygame.display.get_surface().get_size()[1]

    @classmethod
    def show_title_screen(cls):
        Screen.fill_screen(255,255,255)
        Screen.draw_text("Boulder Dodge!", Screen.get_width() // 2, Screen.get_height() // 2, (0, 0, 0))