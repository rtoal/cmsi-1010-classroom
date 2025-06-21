"""A animation of a plane landing, controlled by the user.

The plan begins in a flying state. The user then presses the down arrow key
to start descending. When the plane is close to the ground, the user must
press the up arrow key to raise the nose. After the plane touches the ground,
then the user presses the down arrow key again to lower the nose. Then they
must press the return key to start braking. The plane will come to a stop
and the user can click to start over.
"""

import math
from dataclasses import dataclass
import pygame

WIDTH, HEIGHT = 1024, 600
GRASS_COLOR = (0, 128, 0)
GRASS_HEIGHT = 100
GRASS_TOP = HEIGHT - GRASS_HEIGHT
GRASS_RECTANGLE = (0, GRASS_TOP, WIDTH, GRASS_HEIGHT)
GROUND_LEVEL = HEIGHT - (GRASS_HEIGHT // 2)
TREE_SPACING = 173  # space between trees
MAX_PLANE_SPEED = 23

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Landing")
clock = pygame.time.Clock()


@dataclass
class Plane:
    x: int
    y: int
    state: str = "flying"  # "flying", "descending", "ground"
    speed: int = MAX_PLANE_SPEED
    rotation: int = 0  # rotation angle in radians

    def draw(self):
        plane_relatives = [
            (-16, 0), (-13, 2), (-15, 7), (-12, 7), (-8, 2), (-1, 2),
            (-6, 6), (-5, 6), (8, 2), (16, 2), (19, -2), (8, -2),
            (-5, -8), (-6, -8), (-1, -2), (-13, -2)]
        rotated = plane_relatives if self.rotation == 0 else [
            (x * math.cos(self.rotation) - y * math.sin(self.rotation),
             x * math.sin(self.rotation) + y * math.cos(self.rotation))
            for x, y in plane_relatives]
        plane = [(WIDTH//2 + 4*x, self.y - 4*y) for x, y in rotated]
        pygame.draw.polygon(screen, (255, 255, 255), plane)

    def move(self):
        if self.state != "stopped":
            self.x += self.speed % TREE_SPACING
        if self.state == "descending":
            self.y += self.speed * 0.1
            if self.y >= GROUND_LEVEL:
                self.state = "ground"
                self.y = GROUND_LEVEL
        elif self.state == "ground":
            self.y = GROUND_LEVEL
            self.speed -= 0.05
            if self.speed <= 0:
                self.speed = 0
                self.state = "stopped"


plane = Plane(0, y=50, rotation=0.1)


def draw_tree(x, y):
    pygame.draw.rect(screen, (139, 69, 19), (x - 5, y - 20, 10, 20))  # trunk
    pygame.draw.polygon(screen, (0, 128, 0), [
                        (x - 30, y - 20), (x + 30, y - 20), (x, y - 100)])  # leaves


def draw_scene():
    if plane.state != "stopped":
        screen.fill((0, 255, 255))  # clear screen
        pygame.draw.rect(screen, GRASS_COLOR, GRASS_RECTANGLE)
        x = -plane.x
        while x < WIDTH:
            draw_tree(x, GRASS_TOP)
            x += TREE_SPACING
        plane.draw()
        plane.move()

    clock.tick(60)  # limit to 60 FPS
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if plane.state == "flying":
                    plane.state = "descending"
                elif plane.state == "stopped":
                    plane.state = "flying"
                    plane.x = 0
                    plane.y = 50
                    plane.speed = MAX_PLANE_SPEED
    draw_scene()
