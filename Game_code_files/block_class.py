# Import standard modules.
import sys

# Import non-standard modules.
import pygame
from pygame.locals import *
 
 #makes class for block
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

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
    blocks_group = pygame.sprite.Group()
    for i in range(0, 10):
        for j in range(0, 10):
            block = Block((255, 255, 255), 100, 100)
            block.rect.x = i*150
            block.rect.y = j*150
            blocks_group.add(block)
    return blocks_group
