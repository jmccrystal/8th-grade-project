import math
from Screen import Screen

class Hit_Circle:
    def __init__(self, radius, entity):
        self.radius = radius
        self.entity = entity
    
    def is_intersecting(self, other_hit_circle):
        x1 = self.entity.get_x_pos()
        x2 = other_hit_circle.entity.get_x_pos()
        y1 = self.entity.get_y_pos()
        y2 = other_hit_circle.entity.get_y_pos()
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        return distance < self.radius + other_hit_circle.radius

    def is_outside_left_wall(self):
        if self.entity.get_x_pos() - self.radius < 0:
            return True
        return False

    def is_outside_top_wall(self):
        if self.entity.get_y_pos() - self.radius < 0:
            return True
        return False

    def is_outside_right_wall(self):
        if self.entity.get_x_pos() + self.radius > Screen.get_width():
            return True
        return False
    
    def is_outside_bottom_wall(self):
        if self.entity.get_y_pos() + self.radius > Screen.get_height():
            return True
        return False

    def get_radius(self):
        return self.radius