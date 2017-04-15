import random
import sys

import pygame

from colors import *

def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))



def draw_cells():
    for (x, y) in cells:
        color = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, color, rectangle)


def get_cells(density=0.5):
    return {(c, r): random.random() < density for c in range(columns) for r in range(rows)}
# get_cells() basically gives every cell a random number between o and 1
# if the number is lower than population density (0.2) then that cell is
# True, which means it's 'alive'. If the cell is > 0.2 then that cell is
# False, and therefore it's 'dead'.

def get_neighbours((point)):
     x, y = point
     positions = [(x - 1, y -1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                  (x + 1, y +1), (x, y +1), (x - 1, y + 1), (x - 1, y)]
     return [cells[r, c] for (r, c) in positions if 0 <= r < rows and 0 <= c < columns]

def evolve():
    global cells

    newCells = cells.copy()

    for positiion, alive in cells.items():
        live_neighbours = sum(get_neighbours(positiion))
        if alive:
            if live_neighbours not in [2, 3]:
                newCells[positiion] = False
        elif live_neighbours == 3:
            newCells[positiion] = True
    cells = newCells

pygame.init()
columns, rows = 75, 75
cells = get_cells()

cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    clock.tick(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_cells()
    evolve()
    draw_grid()

    pygame.display.update()