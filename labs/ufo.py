"""A animation of multiple grey UFOs flying across the screen.
There is a grassy field at the bottom of the screen, and a large
yellowish orange sun in the upper right corner of a cyan sky.
"""

import sys
from dataclasses import dataclass
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion")


@dataclass
class UFO:
    x: int
    y: int
    width: int = 100
    height: int = 30
    speed: int = 1

    def draw(self):
        ufo_color = (128, 128, 128)
        pygame.draw.ellipse(
            screen, ufo_color, (self.x, self.y, self.width, self.height))
        pygame.draw.ellipse(
            screen, ufo_color,
            (self.x + self.width//4, self.y-self.height//3, self.width//2, self.height))

    def move(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = -self.width


ufos = [
    UFO(x=0, y=50),
    UFO(x=200, y=100, speed=3.5, width=80, height=20),
    UFO(x=400, y=150, width=120, speed=3),
    UFO(x=600, y=200, speed=4)]


def draw_scene():
    screen.fill((0, 255, 255))  # clear screen
    # draw the sun
    pygame.draw.circle(screen, (255, 200, 0), (WIDTH - 100, 100), 150)
    # draw the grass
    pygame.draw.rect(screen, (0, 128, 0), (0, HEIGHT - 100, WIDTH, 100))
    for ufo in ufos:
        ufo.draw()
        ufo.move()
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    draw_scene()
