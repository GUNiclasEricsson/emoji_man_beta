import pygame
from settings import *


class EmojiEnemy(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, steps, speed):
        super(EmojiEnemy, self).__init__()
        self.surface = pygame.image.load(ENEMY_SURFACE).convert()  
        self.rect = self.surface.get_rect(center = (start_x + 20, start_y + 20))
        self.steps = steps 
        self.speed = speed
        self.direction_left = -self.speed
        self.direction_right = self.speed
        self.steps_left = 0
        self.steps_right = 0
        
    def update(self):
        # checks if the amount of steps to the left has NOT been taken
        # if not continue in the loop
        #print(f"BOTTOM: {self.top_line}")
        if self.steps_left != self.steps:
            # moves the rect to the left
            self.rect.move_ip(self.direction_left, 0)
            # adds the steps in to the step counter
            self.steps_left = self.steps_left + 1
            #print(f"Left: {self.steps_left}")

        # checks to see if the steps to the right has been taken 
        # and the steps to the right has NOT been taken
        if self.steps_left == self.steps and self.steps_right != self.steps:
            # moves the rect to the right
            self.rect.move_ip(self.direction_right, 0)
            # adds the steps taken in to the step counter
            self.steps_right = self.steps_right + 1
            #print(f"Right: {self.steps_right}")
            # if the steps to the right has been taken
            # set the steps counters back to 1
            if self.steps_right == self.steps:
                self.steps_left = 0
                self.steps_right = 0

        



    
