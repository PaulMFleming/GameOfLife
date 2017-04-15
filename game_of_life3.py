import random
import sys

import pygame

from  colors import *

def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, green, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, green, (0, y), (width, y))

def draw_cells():
    for (x, y) in cells:
        color = dark_blue if cells[x, y] else white
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, color, rectangle)

def get_cells(density=0.2):
    return {(c, r): random.random() < density for c in range(columns) for r in range(rows)}
    return cells

def get_neighbours((x, y)):
    positions = [(x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y),
                 (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y)]
    return [cells[r, c] for (r, c) in positions if 0 <= r < rows and 0 <= c < columns]

def evolve():
    global cells

    newCells = cells.copy()

    for position, alive in cells.items():
        live_neighbours = sum(get_neighbours(position))
        if alive:
            if live_neighbours not in [2, 3]:
                newCells[position] = False
        elif live_neighbours == 3:
            newCells[position] = True
    cells = newCells

pygame.init()

columns, rows = 50, 50
cell_size = 10
cells = get_cells()


size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
speed = 2

while True:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed += 1
            if event.key == pygame.K_DOWN:
                speed -= 1

    draw_cells()
    evolve()
    draw_grid()

    pygame.display.update()