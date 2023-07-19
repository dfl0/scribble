import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
SCREEN.fill(WHITE)

color = BLACK
radius = 10

running = True
while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    MOUSE = pygame.mouse.get_pos()
    MOUSE_PRESSED = pygame.mouse.get_pressed()
    MOUSE_SPEED = pygame.mouse.get_rel()

    keys = pygame.key.get_pressed()

    if MOUSE_PRESSED[0] and MOUSE_SPEED != (0, 0):
        pygame.draw.circle(SCREEN, color, MOUSE, radius)
    else:
        pass

    pygame.display.flip()

pygame.quit()
sys.exit()
