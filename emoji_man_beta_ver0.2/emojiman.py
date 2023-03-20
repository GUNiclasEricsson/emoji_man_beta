import pygame
import random
from settings import *


class EmojiMan(pygame.sprite.Sprite):
    def __init__(self, groups):
        super(EmojiMan, self).__init__()
        self.surface = pygame.image.load(EMOJI_SURFACE).convert()
        self.rect = self.surface.get_rect(topleft = PLAYER_START)
        self.bottom = self.rect.bottom

        self.direction = pygame.math.Vector2()
        self.steps = 4
        self.jump_speed = 8
        self.gravity = 0.3
        self.jumped = False
        self.power_up = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self, key):
        if key[LEFT]:
            self.direction.x = -self.steps
            self.rect.x += self.direction.x
        if key[RIGHT]:
            self.direction.x = self.steps
            self.rect.x += self.direction.x 
        if key[DOWN]:
            self.direction.y = self.steps + 5
        if key[SPACE] and self.jumped == False:
            self.direction.y = -self.jump_speed
            self.jumped = True
 
    def collision(self, player, collision_sprites):        
        for sprite in collision_sprites:
            if sprite.rect.colliderect(player.rect):
                
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                    
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
        
        self.apply_gravity()

        for sprite in collision_sprites:
            if sprite.rect.colliderect(player.rect):                
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.jumped = False

class FlyingEmoji(pygame.sprite.Sprite):
    def __init__(self):
        super(FlyingEmoji, self).__init__()
        self.surface = pygame.image.load("assets/emoji_man_rect3.png").convert()
        self.direction = pygame.math.Vector2()
        self.rect = self.surface.get_rect(
            center = 
            (
            random.randint(0, 2900), 
            random.randint(-20, 0)
            )
        )
    def fly(self, started):
        self.rect.move_ip(-4, 4)
        if self.rect.right == 0:
            self.kill()
        if started == True:
            self.kill()
        

class FlyingClouds(pygame.sprite.Sprite):
    def __init__(self):
        super(FlyingClouds, self).__init__()
        self.surface = pygame.image.load("assets/emoji_cloud1.png").convert_alpha()
        self.rect = self.surface.get_rect(center = 
            (
            random.randint(W, W + 100), 
            random.randint(0, H)
            ))
        self.flying_speed = random.randint(-5, -1)

    def fly(self, started):
        self.rect.move_ip(self.flying_speed, 0)
        if self.rect.right < -50:
            self.kill()
        
