import pygame
from circleshape import CircleShape
from constants import *
  

class Shot(CircleShape):
    # Need to store the velocity here
    # substitute x, y with position
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, radius= SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, width= 2)

    def update(self, dt):
        self.position += (self.velocity * dt)


