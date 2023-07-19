import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (200, 0, 255)

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

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = BLACK
            if event.key == pygame.K_2:
                color = WHITE
            if event.key == pygame.K_3:
                color = RED
            if event.key == pygame.K_4:
                color = GREEN
            if event.key == pygame.K_5:
                color = BLUE
            if event.key == pygame.K_6:
                color = PURPLE
            if event.key == pygame.K_LEFTBRACKET:
                radius -= 2
            if event.key == pygame.K_RIGHTBRACKET:
                radius += 2

    if MOUSE_PRESSED[0] and MOUSE_SPEED != (0, 0):
        pygame.draw.circle(SCREEN, color, MOUSE, radius)
    else:
        pass

    pygame.display.flip()

pygame.quit()
sys.exit()
