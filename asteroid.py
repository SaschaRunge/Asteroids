import pygame
import random

from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2
        radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, radius)

        new_asteroid1.velocity = velocity1
        new_asteroid2.velocity = velocity2
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

