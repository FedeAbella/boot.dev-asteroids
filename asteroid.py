import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(*self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        deviation_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_plus = Asteroid(
            self.position.x, self.position.y, new_radius)
        new_asteroid_plus.velocity = self.velocity.rotate(
            deviation_angle) * 1.2

        new_asteroid_minus = Asteroid(
            self.position.x, self.position.y, new_radius)
        new_asteroid_minus.velocity = self.velocity.rotate(
            -deviation_angle) * 1.0
