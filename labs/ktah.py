import math
from dataclasses import dataclass
import pygame

pygame.init()
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("K'tah")

FREEZE = pygame.USEREVENT + 1
SCARECROW = pygame.USEREVENT + 2

scarecrow = None  # Placeholder for the scarecrow position


@dataclass
class Agent:
    x: int
    y: int
    radius: int
    speed: int
    color: tuple

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move_towards(self, target):
        dx = target[0] - self.x
        dy = target[1] - self.y
        distance = math.hypot(dx, dy)
        if distance > 0:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed

    def is_collided_with(self, other):
        distance = math.hypot(self.x - other.x, self.y - other.y)
        return distance < (self.radius + other.radius)


@dataclass
class Player(Agent):
    x: int = WIDTH // 2
    y: int = HEIGHT // 2
    radius: int = 20
    speed: int = 5
    color: tuple = (200, 200, 255)

    def teleport(self, pos):
        self.x, self.y = pos


@dataclass
class Zombie(Agent):
    speed: int = 2
    radius: int = 20
    color: tuple = (80, 255, 0)


player = Player()
zombies = [
    Zombie(x=20, y=20, speed=1.8),
    Zombie(x=WIDTH-20, y=20),
    Zombie(x=20, y=HEIGHT-20, speed=2.5),
    Zombie(x=WIDTH-20, y=HEIGHT-20, speed=0.9)]


def player_is_caught(player, zombies):
    for zombie in zombies:
        if player.is_collided_with(zombie):
            return True
    return False


frozen = False


def freeze_zombies():
    global frozen
    if frozen:
        return
    frozen = True
    pygame.time.set_timer(FREEZE, 5000)


def draw_scene():
    if player_is_caught(player, zombies):
        return

    player.move_towards(pygame.mouse.get_pos())
    for zombie in zombies:
        if not frozen:
            target = scarecrow or (player.x, player.y)
            zombie.move_towards(target)

    screen.fill((0, 100, 0))
    player.draw()
    for zombie in zombies:
        zombie.draw()
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.teleport(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                freeze_zombies()
            elif event.key == pygame.K_s:
                scarecrow = (player.x, player.y)
                pygame.time.set_timer(SCARECROW, 5000)
        if event.type == FREEZE:
            frozen = False
            pygame.time.set_timer(FREEZE, 0)
        if event.type == SCARECROW:
            scarecrow = None
            pygame.time.set_timer(SCARECROW, 0)
    draw_scene()
