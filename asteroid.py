import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, width= 2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        spawned_velocity = (
                [
                    self.velocity.rotate(angle) * SPAWN_VELOCITY_FACTOR,
                    self.velocity.rotate(-angle) * SPAWN_VELOCITY_FACTOR,
                ]
        )
        spawned_radius = self.radius - ASTEROID_MIN_RADIUS
        
        spawned_asteroid1 = Asteroid(self.position.x, self.position.y, spawned_radius)
        spawned_asteroid1.velocity = spawned_velocity[0]
        spawned_asteroid2 = Asteroid(self.position.x, self.position.y, spawned_radius)
        spawned_asteroid2.velocity = spawned_velocity[1]
