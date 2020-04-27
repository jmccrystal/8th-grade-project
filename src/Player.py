from Entity import Entity
from Direction import Direction
from Controls_Manager import Controls_Manager
from Screen import Screen
import pygame

class Player(Entity):
    speed = 5

    def __init__(self, x, y):
        super().__init__(x, y, 0, 0, 50, 'intro_ball.gif', 0.25)


    def hit_wall(self):
        if self.hit_circle.is_outside_top_wall():
            self.ypos = self.hit_circle.get_radius()
        if self.hit_circle.is_outside_bottom_wall():
            self.ypos = Screen.get_height() - self.hit_circle.get_radius()
        if self.hit_circle.is_outside_right_wall():
            self.xpos = Screen.get_width() - self.hit_circle.get_radius()
        if self.hit_circle.is_outside_left_wall():
            self.xpos = self.hit_circle.get_radius()

    def tick(self):
        super().tick()
        self.hit_wall()

    def start_move(self, direction):
        if direction == Direction.UP:
            self.yvel = -Player.speed
        elif direction == Direction.RIGHT:
            self.xvel = Player.speed
        elif direction == Direction.DOWN:
            self.yvel = Player.speed
        elif direction == Direction.LEFT:
            self.xvel = -Player.speed

    def end_move(self, direction):
        if direction == Direction.UP:
            self.yvel = 0
            if Controls_Manager.is_key_down(pygame.K_s):
                self.start_move(Direction.DOWN)
        elif direction == Direction.RIGHT:
            self.xvel = 0
            if Controls_Manager.is_key_down(pygame.K_a):
                self.start_move(Direction.LEFT)
        elif direction == Direction.DOWN:
            self.yvel = 0
            if Controls_Manager.is_key_down(pygame.K_w):
                self.start_move(Direction.UP)
        elif direction == Direction.LEFT:
            self.xvel = 0
            if Controls_Manager.is_key_down(pygame.K_d):
                self.start_move(Direction.RIGHT)