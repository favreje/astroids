import pygame
from circleshape import CircleShape
from constants import * 
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius= PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), width= 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Ship movement
        if keys[pygame.K_j]: # Rotate left
            self.rotate(-dt) 
        if keys[pygame.K_l]: # Rotate right
            self.rotate(dt) 
        if keys[pygame.K_f]: # Move forward
            self.move(dt)
        if keys[pygame.K_d]: # Move backwards
            self.move(-dt)
        if keys[pygame.K_k]: # Shoot
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        Shot(self.position, pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED)
