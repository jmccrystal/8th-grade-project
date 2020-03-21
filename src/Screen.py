import pygame

class Screen:
    @classmethod
    def init(cls, width, height):
        pygame.init()
        size = width, height
        cls.screen = pygame.display.set_mode(size)

    @classmethod
    def fill_screen(cls, color):
        cls.screen.fill(color)
    
    @classmethod
    def draw_image(cls, image, x, y):
        cls.screen.blit(image, (x , y))

    @classmethod
    def draw_text(cls, text, x, y, color):
        cls.screen.blit(text, (x, y))

    @classmethod
    def screen_update(cls):
        pygame.display.flip()