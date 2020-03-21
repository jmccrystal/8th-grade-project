from Entity import Entity
from Boulder import Boulder
import random

class Boulder_Spawner(Entity):

    def __init__(self, velocity, rate):
        super().__init__(0, 0, 0, 0)
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

    def draw(self):
        for boulder in self.boulders:
            boulder.draw()

    def spawn_boulder(self):
        #figure out how to make x random
        x = random.randint(0, 1001)
        boulder = Boulder(x, -400, 0, self.velocity)
        self.boulders.append(boulder)
