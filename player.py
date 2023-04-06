import pygame
import time
# Player class
class Player(pygame.sprite.Sprite):
    last_jump_y = 0
    
    def __init__(self):
        super().__init__()
        self.pos = (100, 50)
        self.pos_x = 100
        self.pos_y = 50 
        self.x_velocity = 2
        self.y_velocity = 0  #5
        self.image = pygame.image.load('Assets/player03.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
    
    def jump(self):
        global last_jump_y
        global can_jump
        self.y_velocity = -5
        can_jump = False
        last_jump_y = self.rect.y
        print(last_jump_y)
