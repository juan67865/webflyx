import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        right_asteroid = self.velocity.rotate(split_angle)
        left_asteroid = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_right_split = Asteroid(self.position.x, self.position.y, new_radius)
        new_right_split.velocity =  right_asteroid * 1.2
        new_left_split = Asteroid(self.position.x, self.position.y, new_radius)
        new_left_split.velocity = left_asteroid * 1.2