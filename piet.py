import pygame
import random
import sys

# Initialize PyGame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recursive Rectangles")

# Colors (pygame uses RGB tuples)
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


def split_rect(rect, depth, limit):
    pygame.draw.rect(screen, random.choice(COLORS), rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, LINE_WIDTH)

    if depth == limit:
        return
    if rect.width < 2 * x_pad or rect.height < 2 * y_pad:
        return

    if rect.width > rect.height:
        x = random.randint(rect.left + x_pad, rect.right - x_pad)
        r1 = pygame.Rect(rect.left, rect.top, x - rect.left, rect.height)
        r2 = pygame.Rect(x, rect.top, rect.right - x, rect.height)
    else:
        y = random.randint(rect.top + y_pad, rect.bottom - y_pad)
        r1 = pygame.Rect(rect.left, rect.top, rect.width, y - rect.top)
        r2 = pygame.Rect(rect.left, y, rect.width, rect.bottom - y)

    split_rect(r1, depth + 1, limit)
    split_rect(r2, depth + 1, limit)


def draw_scene():
    screen.fill((255, 255, 255))  # clear screen
    initial = pygame.Rect(0, 0, WIDTH, HEIGHT)
    split_rect(initial, 0, 5)
    pygame.display.flip()


# Draw the first scene
draw_scene()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            draw_scene()
