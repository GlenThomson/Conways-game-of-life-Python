# Import standard modules.
import sys

# Import non-standard modules.
import pygame
from pygame.locals import *
 
 #makes class for Player
class Player(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
    movement_speed = 0.05
    #the max movements in any direction
    Max_movement_speed_down = 10
    Max_movement_speed_up = -10
    Max_movement_speed_left = -5
    Max_movement_speed_right = 5

    #the current speeds in both all direction
    vertical_speed = 0
    horizontal_speed = 0
    #update vertical speed
    def update_vertical_speed(self, speed):
        self.vertical_speed += speed
    #update horizontal speed
    def update_horizontal_speed(self, speed):
        self.horizontal_speed += speed
    
    #get vertical speed
    def get_vertical_speed(self):
        return self.vertical_speed
    #get horizontal speed
    def get_horizontal_speed(self):
        return self.horizontal_speed
    
    #get Max_movement_speed_down
    def get_Max_movement_speed_down(self):
        return self.Max_movement_speed_down
    #get max movement speed left
    def get_Max_movement_speed_left(self):
        return self.Max_movement_speed_left
    #get Max_movement_speed_up
    def get_Max_movement_speed_up(self):
        return self.Max_movement_speed_up
    #get Max_movement_speed_right
    def get_Max_movement_speed_right(self):
        return self.Max_movement_speed_right

    #get location of player
    def get_location(self):
        return self.rect.x, self.rect.y
    #get size of player
    def get_size(self):
        return self.rect.width, self.rect.height
    
    #update player location
    def update_position(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def get_movement_speed(self):
        return self.movement_speed
#initiat player sprite 
def create_player():
    player_group = pygame.sprite.Group()
    player = Player((255, 0, 0), 100, 100)
    player.rect.x = 0
    player.rect.y = 0
    player_group.add(player)
    return player_group
