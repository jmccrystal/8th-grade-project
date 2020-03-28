from Entity import Entity
from Boulder import Boulder
from Screen import Screen
from Score import Score
import random, pygame

class Boulder_Spawner(Entity):
    def __init__(self, velocity, rate):
        super().__init__(0, 0, 0, 0, 0)
        self.velocity = velocity
        #rate is the number of ticks between the spawning of boulders
        self.rate = rate
        #tick_counter is how many ticks have passed since the game starts
        self.tick_counter = 0
        self.boulders = []


    def tick(self):
        self.tick_counter += 1
        if self.tick_counter % self.rate == 0:
            self.spawn_boulder()
        for boulder in self.boulders:
            boulder.tick()
            self.despawn_boulder()

    def draw(self):
        for boulder in self.boulders:
            boulder.draw()

    def spawn_boulder(self):
        x = random.randint(0, Screen.get_width())
        boulder = Boulder(x, -150, 0, self.velocity)
        self.boulders.append(boulder)
        Score.increment_score()

    def is_intersecting_boulder(self, entity):
        for boulder in self.boulders:
            if boulder.get_hit_circle().is_intersecting(entity.get_hit_circle()):
                return True
        return False

    def despawn_boulder(self):
        for boulder in self.boulders:
            if boulder.hit_circle.should_despawn_boulder():
                self.boulders.remove(boulder)