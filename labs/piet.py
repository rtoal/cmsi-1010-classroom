"""A simple generator of Mondrian-style colored rectangles.
Based on an original JavaScript implementation by Max Halford
at https://maxhalford.github.io/blog/mondrian/)
"""

import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mondrain")

COLORS = [
    (255, 255, 255),  # white
    (255, 255, 255),
    (255, 255, 255),
    (255, 255, 255),
    (0, 0, 0),        # black
    (255, 0, 0),      # red
    (0, 0, 255),      # blue
    (255, 255, 0),    # yellow
]

x_pad = int(WIDTH * 0.05)
y_pad = int(HEIGHT * 0.05)
LINE_WIDTH = 5


def draw_and_split(rect, depth):
    pygame.draw.rect(screen, random.choice(COLORS), rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, LINE_WIDTH)

    if depth == 0:
        # We've gone as deep as we want to go
        return
    if rect.width < 2 * x_pad or rect.height < 2 * y_pad:
        # Rectangle is too small to split
        return

    if rect.width > rect.height:
        x = random.randint(rect.left + x_pad, rect.right - x_pad)
        r1 = pygame.Rect(rect.left, rect.top, x - rect.left, rect.height)
        r2 = pygame.Rect(x, rect.top, rect.right - x, rect.height)
    else:
        y = random.randint(rect.top + y_pad, rect.bottom - y_pad)
        r1 = pygame.Rect(rect.left, rect.top, rect.width, y - rect.top)
        r2 = pygame.Rect(rect.left, y, rect.width, rect.bottom - y)

    draw_and_split(r1, depth - 1)
    draw_and_split(r2, depth - 1)


def draw_scene():
    screen.fill((255, 255, 255))  # clear screen
    outer_rectangle = pygame.Rect(0, 0, WIDTH, HEIGHT)
    draw_and_split(outer_rectangle, 5)
    pygame.display.flip()


draw_scene()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            draw_scene()
