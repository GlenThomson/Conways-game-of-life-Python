# PyGame template.
 
# Import standard modules.
import imp
import sys
from turtle import width

# Import non-standard modules.
import pygame
from pygame.locals import *
 
#import block_class file 
import block_class
#import everything from block_class
from block_class import *

import player_class
from  player_class import *

def update(dt):
  """
  Update game. Called once per frame.
  dt is the amount of time passed since last frame.
  If you want to have constant apparent movement no matter your framerate,
  what you can do is something like
  
  x += v * dt
  
  and this will scale your velocity based on time. Extend as necessary."""
  
  # Go through events that are passed to the script by the window.
  for event in pygame.event.get():
    # We need to handle these events. Initially the only one you'll want to care
    # about is the QUIT event, because if you don't handle it, your game will crash
    # whenever someone tries to exit.
    if event.type == QUIT:
      pygame.quit() # Opposite of pygame.init
      sys.exit() # Not including this line crashes the script on Windows. Possibly
      # on other operating systems too, but I don't know for sure.
    # Handle other events as you wish.
 
def draw(screen):
  """
  Draw things to the window. Called once per frame.
  """
  screen.fill((0, 0, 0)) # Fill the screen with black.
  


  #draw the blocks
  blocks_group.draw(screen)

    #draw the player
  player.draw(screen)


  # Flip the display so that the things we drew actually show up.
  pygame.display.flip()
 
def runPyGame():
  # Initialise PyGame.
  pygame.init()
  
  # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
  fps = 80.0
  fpsClock = pygame.time.Clock()
  
  
  # Set up the window.
  width, height = 1600, 1200
  screen = pygame.display.set_mode((width, height))

  #set up size of map
  Map_width = 2222
  Map_height = 2222
  Player_map_position_xy= [1500,1000]

  

  #player starting position
  Player_starting_position_xy = [0.5*width-(0.5*player1.rect.width),0.5*height-(0.5*player1.rect.height)]
  #put player in center of screen
  player1.update_position(Player_starting_position_xy[0],Player_starting_position_xy[1])
  # screen is the surface representing the window.
  # PyGame surfaces can be thought of as screen sections that you can draw onto.
  # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
  
  # Main game loop.
  dt = 1/fps # dt is the time since last frame.
  while True: # Loop forever!
    

    def sprites_update():
      #get variables 
      player_map_position_xy = Player_map_position_xy

      #get first sprite from player
      player1 = player.sprites()[0]
      #checks if player vertical speed is less then Max_movement_speed_down
      if player1.get_vertical_speed() < player1.get_Max_movement_speed_down():
        #gravity effect on player
        player1.update_vertical_speed(player1.get_vertical_speed()+gravity)
        #gravity effect on player_map_position_xy
        player_map_position_xy[1] = player_map_position_xy[1]+gravity
      
      if player1.get_location()[1] > height-player1.rect.height:
          print("")
      else:
        player_map_position_xy[1] += player1.get_vertical_speed()
        #move player if near edge of map
        if player_map_position_xy[1] > Map_height-height/2:
          player1.update_position(0, player1.get_vertical_speed())
        #keeps player in center of screen
        elif player_map_position_xy[1] < height/2 and player1.get_location()[1] < Player_starting_position_xy[1]:
          player1.update_position(0, player1.get_vertical_speed())
        else:
          for block in blocks_group.sprites():
            block.update_location(0, -player1.get_vertical_speed())


      #control player with arrow keys by player movement speed
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
        if player1.get_location()[0] < 0:
          #update horizontal speed
          player1.update_horizontal_speed(0)  #stop player from moving left
        else:
          player_map_position_xy[0] += player1.get_horizontal_speed()
          #move player if near edge of map
          if player_map_position_xy[0] < 0 +width/2:
            player1.update_position(player1.get_horizontal_speed(), 0)
          #keeps player in center of screen
          elif player_map_position_xy[0] > width/2 and player1.get_location()[0] > Player_starting_position_xy[0]:
            player1.update_position(player1.get_horizontal_speed(), 0)
          else:
            #loop through blocks and update location
            for block in blocks_group.sprites():
              block.update_location(-player1.get_horizontal_speed(), 0)    
          #update horizontal speed if horizontal speed is less then Max_movement_speed_left
          if player1.get_horizontal_speed() > player1.get_Max_movement_speed_left():
            player1.update_horizontal_speed(player1.get_horizontal_speed()-player1.get_movement_speed())

      if keys[pygame.K_RIGHT]:
        if player1.get_location()[0] > width-player1.rect.width:
          #update horizontal speed
          player1.update_horizontal_speed(0)  #stop player from moving right
        else:
          player_map_position_xy[0] += player1.get_horizontal_speed()
          #move player if near edge of map
          if player_map_position_xy[0] > Map_width-width/2:
            player1.update_position(player1.get_horizontal_speed(), 0)
          #keeps player in center of screen
          elif player_map_position_xy[0] < width/2 and player1.get_location()[0] < Player_starting_position_xy[0]:
            player1.update_position(player1.get_horizontal_speed(), 0)
          else:
            #loop through blocks and update location
            for block in blocks_group.sprites():
              block.update_location(-player1.get_horizontal_speed(), 0)
          #update horizontal speed if horizontal speed is less then Max_movement_speed_right
          if player1.get_horizontal_speed() < player1.get_Max_movement_speed_right():
            player1.update_horizontal_speed(player1.get_horizontal_speed()+player1.get_movement_speed())

      if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        player1.update_horizontal_speed(0)
        






      
    
      #loop through blocks and check if player is touching
      for block in blocks_group:
        for player1 in player:
          if player1.rect.colliderect(block.rect):
            #delete block from group
            blocks_group.remove(block)
      return player_map_position_xy
      
    sprites_update()
    update(dt) # You can update/draw here, I've just moved the code for neatness.
    draw(screen)
    
    dt = fpsClock.tick(fps)


#create instance of player
player = player_class.create_player()
#get first player
player1 = player.sprites()[0]
#gravity variable
gravity = 0.1

#create the block sprites group
blocks_group = block_class.create_blocks()

runPyGame()