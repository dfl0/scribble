import pygame
import sys
import math

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 150, 0)
YELLOW = (255, 225, 0)
GREEN = (0, 225, 25)
BLUE = (0, 0, 255)
PURPLE = (150, 0, 255)
GRAY = (125, 125, 125)
LIGHTRED = (255, 125, 125)
LIGHTORANGE = (255, 200, 100)
LIGHTYELLOW = (255, 250, 125)
LIGHTGREEN = (150, 255, 100)
LIGHTBLUE = (100, 175, 255)
LIGHTPURPLE = (200, 150, 255)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
SCREEN.fill(WHITE)


canvas = []


def drawCanvas():
    for i in range(len(canvas)):
        pygame.draw.circle(SCREEN, canvas[i][0], canvas[i][1], canvas[i][2])


def drawCursor():
    if MOUSE[1] > 60:
        pygame.draw.circle(SCREEN, (100, 100, 100), MOUSE, radius, 1)
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)


toolbarItems = []


class ToolbarItem:
    def __init__(self, color, origin, size, isCircle):
        self.color = color
        self.origin = origin
        self.size = size
        self.isCircle = isCircle
        self.isChosen = False
        self.outlineColor = (100, 100, 100)
        toolbarItems.append(self)

    def check(self):
        if self.isCircle:
            if (
                math.sqrt(
                    (MOUSE[0] - self.origin[0]) ** 2 + (MOUSE[1] - self.origin[1]) ** 2
                )
                < self.size
                and MOUSE_PRESSED[0]
            ):
                for i in toolbarItems:
                    if i != self and i.isChosen == True:
                        i.isChosen = False
                self.isChosen = True

        if self.isChosen:
            self.outlineColor = WHITE
        else:
            self.outlineColor = (100, 100, 100)


blackPalette = ToolbarItem(BLACK, (WINDOW_WIDTH - 200, 16), 10, True)
redPalette = ToolbarItem(RED, (WINDOW_WIDTH - 170, 16), 10, True)
orangePalette = ToolbarItem(ORANGE, (WINDOW_WIDTH - 140, 16), 10, True)
yellowPalette = ToolbarItem(YELLOW, (WINDOW_WIDTH - 110, 16), 10, True)
greenPalette = ToolbarItem(GREEN, (WINDOW_WIDTH - 80, 16), 10, True)
bluePalette = ToolbarItem(BLUE, (WINDOW_WIDTH - 50, 16), 10, True)
purplePalette = ToolbarItem(PURPLE, (WINDOW_WIDTH - 20, 16), 10, True)

grayPalette = ToolbarItem(GRAY, (WINDOW_WIDTH - 200, 44), 10, True)
lightredPalette = ToolbarItem(LIGHTRED, (WINDOW_WIDTH - 170, 44), 10, True)
lightorangePalette = ToolbarItem(LIGHTORANGE, (WINDOW_WIDTH - 140, 44), 10, True)
lightyellowPalette = ToolbarItem(LIGHTYELLOW, (WINDOW_WIDTH - 110, 44), 10, True)
lightgreenPalette = ToolbarItem(LIGHTGREEN, (WINDOW_WIDTH - 80, 44), 10, True)
lightbluePalette = ToolbarItem(LIGHTBLUE, (WINDOW_WIDTH - 50, 44), 10, True)
lightpurplePalette = ToolbarItem(LIGHTPURPLE, (WINDOW_WIDTH - 20, 44), 10, True)


def drawToolbar():
    pygame.draw.rect(SCREEN, (175, 175, 175), [0, 0, WINDOW_WIDTH, 60])

    for i in toolbarItems:
        pygame.draw.circle(SCREEN, i.color, i.origin, i.size)
        pygame.draw.circle(SCREEN, i.outlineColor, i.origin, i.size + 2, 2)


color = BLACK
blackPalette.isChosen = True
radius = 10

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

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFTBRACKET:
                radius -= 2
            if event.key == pygame.K_RIGHTBRACKET:
                radius += 2

    if MOUSE_PRESSED[0] and MOUSE_SPEED != (0, 0) and MOUSE[1] > 60:
        canvas.append((color, MOUSE, radius))
    else:
        pass

    for i in toolbarItems:
        i.check()
        if i.isChosen:
            color = i.color

    drawCanvas()
    drawCursor()
    drawToolbar()
    pygame.display.flip()

pygame.quit()
sys.exit()
