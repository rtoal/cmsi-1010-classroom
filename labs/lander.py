"""A animation of a plane landing, controlled by the user.

WORK IN PROGRESS
"""

import sys
from dataclasses import dataclass
import pygame

pygame.init()
WIDTH, HEIGHT = 1024, 600
GROUND_LEVEL = HEIGHT - 100  # y-coordinate of the ground
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Landing")

tree_spacing = 160
stripe_start, stripe_length = 0, 100
STRIPE_LEVEL = HEIGHT - 50  # y-coordinate of the stripes

MAX_PLANE_SPEED = 1


@dataclass
class Plane:
    x: int
    y: int
    width: int
    height: int
    state: str = "flying"  # "flying", "descending", "ground"
    speed: int = 8

    def draw(self):
        color = (128, 128, 128)
        # pygame.draw.ellipse(
        #     screen, color, (WIDTH//2-self.width, self.y, self.width, self.height))
        x, y = WIDTH // 2 - self.width, self.y
        plane_relatives = [
            (0, 0), (3, 2), (1, 7), (4, 7), (8, 2), (15, 2), (10, 6), (11, 6),
            (24, 2), (32, 2), (35, -2), (24, -2), (11, -8), (10, -8), (15, -2),
            (3, -2)
        ]
        plane = [(WIDTH//2 + 4*x, self.y - 4*y) for x, y in plane_relatives]
        pygame.draw.polygon(screen, (128, 128, 128), plane)

    def move(self):
        if self.state != "stopped":
            self.x += self.speed % (tree_spacing * 20)
        if self.state == "descending":
            self.y += self.speed * 0.1
            if self.y >= STRIPE_LEVEL:
                self.state = "ground"
                self.y = STRIPE_LEVEL
        elif self.state == "ground":
            self.y = STRIPE_LEVEL
            self.speed -= 0.005
            if self.speed <= 0:
                self.speed = 0
                self.state = "stopped"


plane = Plane(0, y=50, width=100, height=30)


def draw_scene():
    global stripe_start
    screen.fill((0, 255, 255))  # clear screen
    pygame.draw.rect(screen, (0, 128, 0), (0, HEIGHT - 100, WIDTH, 100))
    pygame.draw.rect(screen, (0, 0, 0), (0, HEIGHT-70, WIDTH, 50))
    x = stripe_start
    while x < WIDTH:
        pygame.draw.line(screen, (255, 255, 255), (x, HEIGHT - 50),
                         (x + stripe_length, HEIGHT - 50), 5)
        x += (stripe_length * 1.5)
    # draw_trees()
    plane.draw()
    plane.move()
    stripe_start -= plane.speed
    if stripe_start*1.5 < -stripe_length:
        stripe_start += stripe_length*1.5

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
                    plane.speed = MAX_PLANE_SPEED
    draw_scene()
