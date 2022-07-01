# PyGame template.
 
# Import standard modules.
import imp
import math 
import sys
from turtle import width
import random
# Import non-standard modules.
import pygame
from pygame.locals import *
from copy import copy, deepcopy
#global variables 
screen_width, screen_height = 1200, 1200
cells = []
cell_size= 6  
temp_alive_list = []

def update(dt):
  # Go through events that are passed to the script by the window.
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit() # Opposite of pygame.init
      sys.exit() # Not including this line crashes the script on Windows. Possibly

 #Draw things to the window. Called once per frame.
def draw(screen):
  screen.fill((0, 0, 0)) # Fill the screen with black.
  #draw blocks on if they have alive == 1 else dont draw them
  for row in range(len(cells)):
    for collum in range(len(cells[0])):
      if cells[row][collum] == 1:
        pygame.draw.rect(screen, (255,255,255), (cell_size*row, cell_size*collum, cell_size ,cell_size))
    

  # Flip the display so that the things we drew actually show up.
  pygame.display.flip()
 
def runPyGame():
  # Initialise PyGame.
  pygame.init()
  
  # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
  fps = 80.0
  fpsClock = pygame.time.Clock()
  # Set up the window.
  screen = pygame.display.set_mode((screen_width, screen_height))

  #create 2d array of cells 
  cells = create_initial_cells()
  #creat tempary 2d array the same size as cells
  temp_alive_list = [[0 for i in range(len(cells[0]))] for j in range(len(cells))]


  

  # Main game loop.
  dt = 1/fps # dt is the time since last frame.
  count = 0
  while True: # Loop forever!
    

    count+=1
    #loop through all the blocks and update their alive status
    for row in range(len(cells)):
      for collum in range(len(cells[0])):
        sum = count_neigbors(row,collum)
        #check if cell should die or stay dead
        if sum<2 or sum>3:
          temp_alive_list[row][collum] = 0
        elif sum == 3:
          temp_alive_list[row][collum] = 1


    #loop through and update the cells
    for row in range(len(cells)):
      for collum in range(len(cells[0])):
        if temp_alive_list[row][collum] == 1:
          cells[row][collum] = 1
        else:
          cells[row][collum] = 0
    

    update(dt) # You can update/draw here, I've just moved the code for neatness.
    draw(screen)
    dt = fpsClock.tick(fps)

#counts all the neighbors of a cell
def count_neigbors(row,collum):
  sum = 0 
  for i in range(row-1,row+2):
    for j in range(collum-1,collum+2):
      if i ==-1 or j ==-1 or i ==len(cells) or j == len(cells[0]):
        pass
      elif cells[i][j] == 1:
        sum +=1 
  #if middle cell was included remove 
  if cells[row][collum] == 1:
    sum -=1
    #return the nubmer of neighbors 
  return sum 


#creates all the initial cells as alive or dead 
def create_initial_cells():
    #expression that creates a list of lists of cells
  for i in range(screen_width//cell_size):
    cells.append([random.randint(0,1) for i in range(screen_width//cell_size)])
  return cells

runPyGame()