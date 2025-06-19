"""A animation of a plane landing, controlled by the user.

WORK IN PROGRESS
"""

from dataclasses import dataclass
import pygame

pygame.init()
WIDTH, HEIGHT = 1024, 600
GROUND_LEVEL = HEIGHT - 100  # y-coordinate of the ground
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Landing")
clock = pygame.time.Clock()

tree_spacing = 160
stripe_start, stripe_length = 0, 100
STRIPE_LEVEL = HEIGHT - 50  # y-coordinate of the stripes

MAX_PLANE_SPEED = 20


@dataclass
class Plane:
    x: int
    y: int
    state: str = "flying"  # "flying", "descending", "ground"
    speed: int = MAX_PLANE_SPEED

    def draw(self):
        plane_relatives = [
            (-16, 0), (-13, 2), (-15, 7), (-12, 7), (-8, 2), (-1, 2),
            (-6, 6), (-5, 6), (8, 2), (16, 2), (19, -2), (8, -2),
            (-5, -8), (-6, -8), (-1, -2), (-13, -2)]
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
            self.speed -= 0.05
            if self.speed <= 0:
                self.speed = 0
                self.state = "stopped"


plane = Plane(0, y=50)


def draw_scene():
    global stripe_start
    if plane.state != "stopped":
        screen.fill((0, 255, 255))  # clear screen
        pygame.draw.rect(screen, (0, 128, 0), (0, HEIGHT - 100, WIDTH, 100))
        pygame.draw.rect(screen, (0, 0, 0), (0, HEIGHT-70, WIDTH, 50))
        x = stripe_start
        while x < WIDTH:
            pygame.draw.line(screen, (255, 255, 255), (x, HEIGHT - 50),
                             (x + stripe_length, HEIGHT - 50), 5)
            x += (stripe_length * 1.5)
        plane.draw()
        plane.move()
        stripe_start -= plane.speed
        if stripe_start*1.5 < -stripe_length:
            stripe_start += stripe_length*1.5

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
