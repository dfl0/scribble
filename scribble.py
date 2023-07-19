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

canvas = []


def drawCanvas():
    for i in range(len(canvas)):
        pygame.draw.circle(SCREEN, canvas[i][0], canvas[i][1], canvas[i][2])


def drawMenu():
    pygame.draw.rect(SCREEN, (175, 175, 175), [0, 0, WINDOW_WIDTH, 50])


running = True
while running:
    SCREEN.fill(WHITE)

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    MOUSE = pygame.mouse.get_pos()
    MOUSE_PRESSED = pygame.mouse.get_pressed()
    MOUSE_SPEED = pygame.mouse.get_rel()

    keys = pygame.key.get_pressed()

    if MOUSE[1] > 50:
        pygame.draw.circle(SCREEN, (100, 100, 100), MOUSE, radius, 1)
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)

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

    if MOUSE_PRESSED[0] and MOUSE_SPEED != (0, 0) and MOUSE[1] > 50:
        canvas.append((color, MOUSE, radius))
    else:
        pass

    drawCanvas()
    drawMenu()
    pygame.display.flip()

pygame.quit()
sys.exit()
