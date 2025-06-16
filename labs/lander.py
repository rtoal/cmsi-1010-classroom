"""A animation of a plane landing, controlled by the user.

WORK IN PROGRESS
"""

import sys
from dataclasses import dataclass
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
GROUND_LEVEL = HEIGHT - 100  # y-coordinate of the ground
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Landing")

tree_spacing = 160


@dataclass
class Plane:
    x: int
    y: int
    width: int
    height: int
    state: str = "flying"  # "flying", "descending", "ground"
    speed: int = 5

    def draw(self):
        color = (128, 128, 128)
        pygame.draw.ellipse(
            screen, color, (WIDTH//2-self.width, self.y, self.width, self.height))

    def move(self):
        if self.state != "stopped":
            self.x += self.speed % (tree_spacing * 20)
        if self.state == "descending":
            self.y += self.speed * 0.1
            if self.y >= GROUND_LEVEL:
                self.state = "ground"
                self.y = GROUND_LEVEL
        elif self.state == "ground":
            self.y = HEIGHT - 50
            self.speed -= 0.01
            if self.speed <= 0:
                self.speed = 0
                self.state = "stopped"


plane = Plane(0, y=50, width=100, height=30)


def draw_trees():
    x = tree_spacing - (plane.x % WIDTH)
    while x < WIDTH:
        pygame.draw.rect(screen, (139, 69, 19),
                         (x, GROUND_LEVEL - 50, 20, 50))  # trunk
        pygame.draw.polygon(screen, (0, 128, 0), [(x - 30, GROUND_LEVEL - 50),
                                                  (x + 10, GROUND_LEVEL - 100),
                                                  # leaves
                                                  (x + 50, GROUND_LEVEL - 50)])
        pygame.draw.polygon(screen, (0, 128, 0), [(x - 20, GROUND_LEVEL - 70),
                                                  (x + 10, GROUND_LEVEL - 120),
                                                  # leaves
                                                  (x + 40, GROUND_LEVEL - 70)])
        x += tree_spacing


def draw_scene():
    screen.fill((0, 255, 255))  # clear screen
    pygame.draw.rect(screen, (0, 128, 0), (0, HEIGHT - 100, WIDTH, 100))
    draw_trees()
    plane.draw()
    plane.move()
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if plane.state == "flying":
                    plane.state = "descending"
                elif plane.state == "descending":
                    plane.state = "ground"
                elif plane.state == "ground":
                    plane.state = "stopped"
                elif plane.state == "stopped":
                    plane.state = "flying"
                    plane.x = 0
                    plane.y = 50
                    plane.speed = 5
    draw_scene()
