# PyGame template.
 
# Import standard modules.
import imp
import math 
import sys
from turtle import width

# Import non-standard modules.
import pygame
from pygame.locals import *
 
#import block_class file 
import block_class
#import everything from block_class
from block_class import *


def update(dt):

  
  # Go through events that are passed to the script by the window.
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit() # Opposite of pygame.init
      sys.exit() # Not including this line crashes the script on Windows. Possibly

 
def draw(screen):
  """
  Draw things to the window. Called once per frame.
  """
  screen.fill((0, 0, 0)) # Fill the screen with black.
  

  #draw blocks on if they have alive == 1 else dont draw them
  for row in blocks_group:
    for blocks in row:
      if blocks.is_alive_or_dead() == 1:
        screen.blit(blocks.image, blocks.get_location())
      else:
        pass


  # Flip the display so that the things we drew actually show up.
  pygame.display.flip()
 
def runPyGame():
  # Initialise PyGame.
  pygame.init()
  
  # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
  fps = 80.0
  fpsClock = pygame.time.Clock()
  
  
  # Set up the window.
  screen_width, screen_height = 1200, 1200
  screen = pygame.display.set_mode((screen_width, screen_height))


  

  # screen is the surface representing the window.
  # PyGame surfaces can be thought of as screen sections that you can draw onto.
  # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
  
  # Main game loop.
  dt = 1/fps # dt is the time since last frame.
  count = 0
  while True: # Loop forever!
    temp_alive_list = []

    count+=1
    #loop through all the blocks and update their alive status
    if count == 3:
      count = 0
      for row in range(0, len(blocks_group)):
        temp_alive_list.append([])
        for col in range(0, len(blocks_group[0])):
          #get number of neighbors
          neighbors = count_neighbors(row,col)
          #if cell is alive and has 2 or 3 neighbors, keep it alive
          if blocks_group[row][col].is_alive_or_dead() == 1 and neighbors == 2 or neighbors == 3:
            temp_alive_list[row].append(1)
          #if cell is alive and has less than 2 or more than 3 neighbors, kill it
          elif blocks_group[row][col].is_alive_or_dead() == 1 and neighbors < 2 or neighbors > 3:
            temp_alive_list[row].append(0)
          #if cell is dead and has 3 neighbors, make it alive
          elif blocks_group[row][col].is_alive_or_dead() == 0 and neighbors == 3:
            temp_alive_list[row].append(1)
          #if cell is dead and has less than 3 neighbors, keep it dead
          elif blocks_group[row][col].is_alive_or_dead() == 0 and neighbors < 3:
            temp_alive_list[row].append(0)
          else:
            pass
          #loop through all the blocks and update their alive status
      for row in range(0, len(blocks_group)):
        for col in range(0, len(blocks_group[0])):
          blocks_group[row][col].update_is_alive(temp_alive_list[row][col])



    update(dt) # You can update/draw here, I've just moved the code for neatness.
    draw(screen)
    
    dt = fpsClock.tick(fps)



#create the block sprites group
blocks_group = block_class.create_blocks()

#counts all the neighbors of a cell
def count_neighbors(i,j):
  count = 0
  for row in range(i-1, i+2):
    for col in range(j-1, j+2):
      if row == i and col == j:
        pass
      else:
        if row >= 0 and row < len(blocks_group) and col >= 0 and col < len(blocks_group[0]):
          if blocks_group[row][col].is_alive_or_dead() == 1:
            count += 1
  return count

runPyGame()