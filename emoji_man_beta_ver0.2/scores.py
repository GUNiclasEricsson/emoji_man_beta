import pygame
import random
from settings import *
from emojiman import FlyingEmoji

class Watermelon(pygame.sprite.Sprite):
    def __init__(self, groups):
        super(Watermelon, self).__init__()
        self.surface = pygame.image.load("assets/emoji_man_watermelon1.png").convert_alpha()
        self.rect = self.surface.get_rect(center = (1520, 560))
        watermelon = self.rect
    
    def get_score(self, player):
        if pygame.Rect.colliderect(self.rect, player.rect):
            self.kill()

class Apples(pygame.sprite.Sprite):
    def __init__(self, groups):
        super(Apples, self).__init__()
        self.surface = pygame.image.load("assets/emoji_man_apple1.png").convert_alpha()
        self.rect = self.surface.get_rect(center = (1440, 1000))
        apple = self.rect
  
    def get_score(self, player):
        if pygame.Rect.colliderect(self.rect, player.rect):
            self.kill()
        
class Scores():
    def __init__(self, fruit_group):
        self.fruit_group = fruit_group
        self.current_score = 0

    def get_scores(self, player):
        for fruit in self.fruit_group:
            if pygame.Rect.colliderect(player.rect, fruit.rect):
                self.current_score += 1
                fruit.kill()
                



class Score():
    def __init__(self):
        self.score_font = pygame.font.Font('assets/RETRO_SPACE.ttf', 50)
        self.instruct_font = pygame.font.Font('assets/RETRO_SPACE.ttf', 40)
        self.surface = pygame.image.load("assets/start_screen.png").convert_alpha()
        self.rect = self.surface.get_rect(x = 0, y = 0)
        self.start_sprites = pygame.sprite.Group() 
        self.flying_emoji = FlyingEmoji() 
    

    def display_score(self, current_score):
        self.current_score = current_score
        self.score_surf = self.score_font.render(f'SCORE {self.current_score}', False, (10,10,10))
        SCREEN.blit(self.score_surf, (100, 70))

    def score_reset(self): 
        return 0

    def game_over(self, current_score):
        SCREEN.blit(BACKGROUND, (0, 0))
        self.instruct_surf = self.instruct_font.render('You lost. Press ENTER to start again.', False, (10, 10, 10))
        self.instruct_rect = self.instruct_surf.get_rect(center = (960, 540))
        self.final_score = current_score
        self.score_message = self.score_font.render(f'YOU WON!', False, (64, 64, 64))
        self.score_message_rect = self.score_message.get_rect(center = (960, 540))
        SCREEN.blit(self.surface, self.rect)

        if current_score == 0 or current_score == 1:
            SCREEN.blit(self.instruct_surf, self.instruct_rect)

        else:
            SCREEN.blit(self.score_message, self.score_message_rect)

    def start_screen(self):
        SCREEN.blit(BACKGROUND, (0, 0))

    def draw_text(self):
        self.instruct_surf = self.instruct_font.render('Press ENTER to start the game.', False, (10, 10, 10))
        self.instruct_rect = self.instruct_surf.get_rect(center = (660, 540))
        self.instruct2_surf = self.instruct_font.render('Jump - SPACE', False, (10, 10, 10))
        self.instruct2_rect = self.instruct_surf.get_rect(center = (660, 590))
        self.instruct3_surf = self.instruct_font.render('Direction - LEFT and RIGHT', False, (10, 10, 10))
        self.instruct3_rect = self.instruct_surf.get_rect(center = (660, 640))
        self.instruct4_surf = self.instruct_font.render('ESC to exit.', False, (10, 10, 10))
        self.instruct4_rect = self.instruct_surf.get_rect(center = (660, 690))
        self.instruct5_surf = self.instruct_font.render('Collect the fruits to win while avoiding the enemies.', False, (10, 10, 10))
        self.instruct5_rect = self.instruct_surf.get_rect(center = (660, 740))

        SCREEN.blit(self.instruct_surf, self.instruct_rect)
        SCREEN.blit(self.instruct2_surf, self.instruct2_rect)
        SCREEN.blit(self.instruct3_surf, self.instruct3_rect)
        SCREEN.blit(self.instruct4_surf, self.instruct4_rect)
        SCREEN.blit(self.instruct5_surf, self.instruct5_rect)
        SCREEN.blit(self.surface, self.rect)
        
      
    def update(self, current_score):
        self.display_score(current_score)


class Life:
    def __init__(self):
        self.starting_hearts = [1, 1, 1]
        self.current_hearts = self.starting_hearts
        self.surface = pygame.image.load("assets/heart.png").convert_alpha()
        self.rect = self.surface.get_rect()
        self.score_font = pygame.font.Font('assets/RETRO_SPACE.ttf', 50)

    def draw_hearts(self):
        self.life_counter = self.score_font.render(f"LIFE ", False, (10, 25, 25))
        SCREEN.blit(self.life_counter, (1440, 70))
        self.hearts = self.current_hearts
        if len(self.hearts) == 3:
          
            SCREEN.blit(self.surface, (1600, 60))

        if len(self.hearts) >= 2:
            SCREEN.blit(self.surface, (1680, 60))

        if len(self.hearts) >= 1:
            SCREEN.blit(self.surface, (1760, 60))
        
    def reset_hearts(self):
        self.current_hearts = [1, 1, 1]