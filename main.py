from io import open_code
import pygame
from pygame.locals import *
import sys
from functions import *
from settings import *
from cool_patterns import *
import random

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()  # For syncing the FPS

# Globals

cells = [[0 for i in range(cell_count)]
         for i in range(cell_count)]

mousedata = (False, False, False)
inbuilt_pattern_index = 0

# Game loop
setup = True
while setup:
    # 1 Process input/events
    clock.tick(FPS)  # will make the loop run at the same speed all the time
    # gets all the events which have occured till now and keeps tab of them.
    for event in pygame.event.get():
        # listening for the the X button at the top
        if event.type == QUIT:
            setup = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedata = pygame.mouse.get_pressed()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                setup = False
                running = True
            if event.key == K_s:            # Saves pattern
                file = open('temp.py','w')
                file.write(str(cells))
                file.close()
                print("Saved")
            if event.key == K_r:        # Get random inbuilt pattern
                cells = inbuilt_patterns[list(inbuilt_patterns.keys())[inbuilt_pattern_index]]
                inbuilt_pattern_index += 1
                inbuilt_pattern_index %= len(inbuilt_patterns)
    # 3 Draw/render
    screen.fill(bg_color)
    for x in range(cell_count):
        for y in range(cell_count):
            if Rect(
                    x*(cell_size+1)+grid_offset, y*(cell_size+1)+grid_offset, cell_size, cell_size).collidepoint(pygame.mouse.get_pos()) and mousedata[0]:
                if cells[x][y] == 0:
                    cells[x][y] = 1
                else:
                    cells[x][y] = 0
            if cells[x][y] == 0:
                cell_color = dead_color
            elif cells[x][y] == 1:
                cell_color = alive_color
            pygame.draw.rect(screen, cell_color, Rect(
                x*(cell_size+1)+grid_offset, y*(cell_size+1)+grid_offset, cell_size, cell_size))

    ########################
    #        LOGIC         #
    ########################

    # Done after drawing everything to the screen
    pygame.display.update()
    mousedata = (False, False, False)

# Actual game loop
running = True
state = cells.copy()
while running:

    # 1 Process input/events
    clock.tick(FPS)  # will make the loop run at the same speed all the time
    # gets all the events which have occured till now and keeps tab of them.
    for event in pygame.event.get():
        # listening for the the X button at the top
        if event.type == QUIT:
            running = False
            sys.exit()
    # 2 Update
    cells = state

    # 3 Draw/render
    screen.fill(bg_color)
    for x in range(cell_count):
        for y in range(cell_count):
            if cells[x][y] == 0:
                cell_color = dead_color
            elif cells[x][y] == 1:
                cell_color = alive_color
            pygame.draw.rect(screen, cell_color, Rect(
                x*(cell_size+1)+grid_offset, y*(cell_size+1)+grid_offset, cell_size, cell_size))
    nearby_data = nearby_cell_data(cells)
    state = cells.copy()
    for x in range(cell_count):
        for y in range(cell_count):
            nearby = nearby_data[x][y]
            if cells[x][y] == 0:  # For dead cells
                if nearby == 3:  # Reproduction
                    state[x][y] = 1
            elif cells[x][y] == 1:  # For alive cells
                if nearby < 2 or nearby > 3:  # Dies by underpop / overpop
                    state[x][y] = 0

    # Done after drawing everything to the screen
    clock.tick(FPS)
    pygame.display.update()
    mousedata = (False, False, False)
