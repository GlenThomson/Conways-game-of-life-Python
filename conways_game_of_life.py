import sys
import pygame
from pygame.locals import *
import numpy as np
from copy import deepcopy
# global variables
screen_width, screen_height = 1200, 1200
cell_size = 8
#make 2d numpy array fill with random 0s and 1s acting as cells states
cells = np.random.randint(0, 2, (screen_width // cell_size, screen_height // cell_size))
temp_cell_states = deepcopy(cells)

# Draw things to the window. Called once per frame.
def draw(screen):
    screen.fill((0, 0, 0))  # Fill the screen with black.
    for row in range(len(cells)):
        draw_and_update_temp_cells(screen,row)
    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()


# Quit the game if the user presses the exit button.
def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # loop through and update the cells
    for row in range(len(cells)):
        for column in range(len(cells[0])):
            if temp_cell_states[row][column] == 1:
                cells[row][column] = 1
            else:
                cells[row][column] = 0


#updates the temp_cell_states and draws alive cells
def draw_and_update_temp_cells(screen,row):
    mmmlist = deepcopy(cells)

    for column in range(len(cells[0])):
        sum = count_neigbors(row, column)
        # check if cell should die or stay dead
        if sum < 2 or sum > 3:
            temp_cell_states[row][column] = 0
        elif sum == 3:
            temp_cell_states[row][column] = 1
        if cells[row][column] == 1:
            pygame.draw.rect(screen, (255, 255, 255), (cell_size * row, cell_size * column, cell_size, cell_size))


# counts all the neighbors of a cell
def count_neigbors(row, collum):
    sum = 0
    for i in range(row - 1, row + 2):
        for j in range(collum - 1, collum + 2):
            if i == -1 or j == -1 or i == len(cells) or j == len(cells[0]): #checks that not outsde of map bounds
                pass
            elif cells[i][j] == 1:
                sum += 1
                # if middle cell was included remove
    if cells[row][collum] == 1:
        sum -= 1
        # return the nubmer of neighbors
    return sum


def runPyGame():
    pygame.init() # Initialise PyGame.
    screen = pygame.display.set_mode((screen_width, screen_height))# Set up the window.
    # Main game loop.
    while True:
        draw(screen)
        update()

runPyGame()
