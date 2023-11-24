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


class ToolbarItem:
    def __init__(self, color, origin, size, type):
        self.color = color
        self.origin = origin
        self.size = size
        self.type = type
        self.isChosen = False
        self.outlineColor = (100, 100, 100)
        toolbarItems.append(self)

    def check(self):
        if self.type == "circle":
            if (
                math.sqrt((MOUSE[0] - self.origin[0]) ** 2 + (MOUSE[1] - self.origin[1]) ** 2) < self.size
                and MOUSE_PRESSED[0]
            ):
                for i in toolbarItems:
                    if i != self and i.type == self.type and i.isChosen is True:
                        i.isChosen = False
                self.isChosen = True
        elif self.type == "rect":
            if (
                MOUSE[0] > self.origin[0]
                and MOUSE[0] < self.origin[0] + self.size[0]
                and MOUSE[1] > self.origin[1]
                and MOUSE[1] < self.origin[1] + self.size[1]
                and MOUSE_PRESSED[0]
            ):
                for i in toolbarItems:
                    if i != self and i.type == self.type and i.isChosen is True:
                        i.isChosen = False
                self.isChosen = True

        if self.isChosen:
            self.outlineColor = WHITE

            if self.type == "rect":
                self.color = (225, 225, 225)
        else:
            self.outlineColor = (100, 100, 100)

            if self.type == "rect":
                self.color = (150, 150, 150)


toolbarItems = []

blackPalette = ToolbarItem(BLACK, (WINDOW_WIDTH - 200, 16), 10, "circle")
redPalette = ToolbarItem(RED, (WINDOW_WIDTH - 170, 16), 10, "circle")
orangePalette = ToolbarItem(ORANGE, (WINDOW_WIDTH - 140, 16), 10, "circle")
yellowPalette = ToolbarItem(YELLOW, (WINDOW_WIDTH - 110, 16), 10, "circle")
greenPalette = ToolbarItem(GREEN, (WINDOW_WIDTH - 80, 16), 10, "circle")
bluePalette = ToolbarItem(BLUE, (WINDOW_WIDTH - 50, 16), 10, "circle")
purplePalette = ToolbarItem(PURPLE, (WINDOW_WIDTH - 20, 16), 10, "circle")

grayPalette = ToolbarItem(GRAY, (WINDOW_WIDTH - 200, 44), 10, "circle")
lightredPalette = ToolbarItem(LIGHTRED, (WINDOW_WIDTH - 170, 44), 10, "circle")
lightorangePalette = ToolbarItem(LIGHTORANGE, (WINDOW_WIDTH - 140, 44), 10, "circle")
lightyellowPalette = ToolbarItem(LIGHTYELLOW, (WINDOW_WIDTH - 110, 44), 10, "circle")
lightgreenPalette = ToolbarItem(LIGHTGREEN, (WINDOW_WIDTH - 80, 44), 10, "circle")
lightbluePalette = ToolbarItem(LIGHTBLUE, (WINDOW_WIDTH - 50, 44), 10, "circle")
lightpurplePalette = ToolbarItem(LIGHTPURPLE, (WINDOW_WIDTH - 20, 44), 10, "circle")

brushButton = ToolbarItem((150, 150, 150), (10, 10), (40, 40), "rect")
eraserButton = ToolbarItem((150, 150, 150), (60, 10), (40, 40), "rect")


def drawToolbar():
    pygame.draw.rect(SCREEN, (175, 175, 175), [0, 0, WINDOW_WIDTH, 60])

    for i in toolbarItems:
        if i.type == "circle":
            pygame.draw.circle(SCREEN, i.color, i.origin, i.size)
            pygame.draw.circle(SCREEN, i.outlineColor, i.origin, i.size + 2, 2)
        elif i.type == "rect":
            pygame.draw.rect(SCREEN, i.color, [i.origin[0], i.origin[1], i.size[0], i.size[1]], 0, 4)
            pygame.draw.rect(SCREEN, i.outlineColor, [i.origin[0], i.origin[1], i.size[0], i.size[1]], 2, 4)

    pygame.draw.circle(SCREEN, BLACK, (30, 30), 12)

    pygame.draw.rect(SCREEN, WHITE, [72, 17, 16, 8], 0, 0, 3, 3)
    pygame.draw.rect(SCREEN, BLACK, [72, 17, 16, 8], 1, 0, 3, 3)
    pygame.draw.rect(SCREEN, LIGHTBLUE, [71, 24, 18, 20])
    pygame.draw.rect(SCREEN, BLACK, [71, 24, 18, 20], 1)


color = BLACK
storeColor = BLACK
blackPalette.isChosen = True
brushButton.isChosen = True
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
            if event.key == pygame.K_c:
                canvas = []

    if MOUSE_PRESSED[0] and MOUSE_SPEED != (0, 0) and MOUSE[1] > 60:
        canvas.append((color, MOUSE, radius))
    else:
        pass

    for i in toolbarItems:
        i.check()
        if i.isChosen:
            if i.type == "circle":
                color = i.color
            elif i.type == "rect":
                if i == brushButton:
                    color = storeColor
                elif i == eraserButton:
                    storeColor = color
                    color = WHITE

    drawCanvas()
    drawCursor()
    drawToolbar()
    pygame.display.flip()

pygame.quit()
sys.exit()
