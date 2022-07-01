# Import standard modules.
import random
import sys

# Import non-standard modules.
import pygame
from pygame.locals import *
 

screen_width = 1200
screen_height = 1200
 #makes class for block
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.alive = random.randint(0,1)

    def update_is_alive(self,alive):
        self.alive = alive

    def is_alive_or_dead(self):
        return self.alive

    #get location of block
    def get_location(self):
        return self.rect.x, self.rect.y
    #get size of block
    def get_size(self):
        return self.rect.width, self.rect.height

    #update block location
    def update_location(self, x, y):
        self.rect.x += x
        self.rect.y += y
    

#track all blocks  
def create_blocks():
    block_width =6
    block_height =6 
    blocks_group = []
    for i in range(0, screen_width//block_width):
        blocks_group.append([])
        for j in range(0, screen_height//block_height):
            block = Block((255, 255, 255), block_width, block_height)
            block.rect.x = i*block_width
            block.rect.y = j*block_height
            blocks_group[i].append(block)
            
    return blocks_group
