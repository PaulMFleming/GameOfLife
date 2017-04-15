import random
import sys

import pygame

from colors import *

def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))

def get_cells(density=0.2):
    return {(c, r): random.random() < density for c in range(columns) for r in range(rows)}
# get_cells() basically gives every cell a random number between o and 1
# if the number is lower than population density (0.2) then that cell is
# True, which means it's 'alive'. If the cell is > 0.2 then that cell is
# False, and therefore it's 'dead'.

def draw_cells():
    for (x, y) in cells:
        color = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, color, rectangle)

pygame.init()
columns, rows = 75, 50
cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)
cells = get_cells()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_cells()
    draw_grid()

    pygame.display.update()