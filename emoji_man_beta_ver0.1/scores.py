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
            print("WATERMELON SCORE!")
            self.kill()

class Apples(pygame.sprite.Sprite):
    def __init__(self, groups):
        super(Apples, self).__init__()
        self.surface = pygame.image.load("assets/emoji_man_apple1.png").convert_alpha()

        self.rect = self.surface.get_rect(center = (1440, 1000))

        apple = self.rect

        


        
        
    def get_score(self, player):

        if pygame.Rect.colliderect(self.rect, player.rect):
            print("APPLE SCORE!")
            self.kill()
        
class Scores():
    def __init__(self, fruit_group):

        self.fruit_group = fruit_group

        self.current_score = 0

    def get_scores(self, player):
        for fruit in self.fruit_group:
            if pygame.Rect.colliderect(player.rect, fruit.rect):
                print("YOU SCOREED!")
                self.current_score += 1
                fruit.kill()
                #time = pygame.time.get_ticks()
                #print(time)


#clock = pygame.time.Clock()



class Score():
    def __init__(self):
        #score_surf = score_font.render('EmojiMan', False, (64, 64, 64))
        #self.start_time = 0
        #self.current_time = 0

        #self.score_amount = 0
        self.score_font = pygame.font.Font('assets/RETRO_SPACE.ttf', 50)
        self.instruct_font = pygame.font.Font('assets/RETRO_SPACE.ttf', 60)

        self.surface = pygame.image.load("assets/start_screen.png").convert_alpha()
        self.rect = self.surface.get_rect(x = 0, y = 0)
        self.start_sprites = pygame.sprite.Group() #
        self.flying_emoji = FlyingEmoji() #
    

    def display_score(self, current_score):
        #self.current_time = int(pygame.time.get_ticks()/1000) - self.start_time

        self.current_score = current_score
        
        self.score_surf = self.score_font.render(f'SCORE {self.current_score}', False, (10,10,10))
        #self.score_rect = self.score_surf.get_rect (center = (400,50))
        SCREEN.blit(self.score_surf, (100, 70)) #, self.score_rect)

        #return self.current_time
    
    def score_reset(self): #, #current_score)
        #self.current_score = current_score
        return 0


    def game_over(self, current_score):
        SCREEN.blit(BACKGROUND, (0, 0))

        self.instruct_surf = self.instruct_font.render('Press ENTER to start the game.', False, (10, 10, 10))
        self.instruct_rect = self.instruct_surf.get_rect(center = (960, 540))
        #self.name_surf = self.score_font.render('EmojiMan in rect land', False, (64, 64, 64))
        #self.name_rect = self.name_surf.get_rect(center = (960, 220))
        self.final_score = current_score
        #SCREEN.blit(self.name_surf, self.name_rect)
        
        #pygame.draw.rect(SCREEN, "#c0e8ec", self.name_rect)
        #pygame.draw.rect(SCREEN, "#c0e8ec", self.name_rect,10)
        #pygame.draw.rect(SCREEN, "#c0e8ec", self.instruct_rect)
        #pygame.draw.rect(SCREEN, "#c0e8ec", self.instruct_rect,10)

        self.score_message = self.score_font.render(f'YOUR SCORE: {self.final_score}', False, (64, 64, 64))
        self.score_message_rect = self.score_message.get_rect(center = (960, 540))

        SCREEN.blit(self.surface, self.rect)

        if current_score == 0:

            SCREEN.blit(self.instruct_surf, self.instruct_rect)

        else:
            SCREEN.blit(self.score_message, self.score_message_rect)

    def start_screen(self):
        SCREEN.blit(BACKGROUND, (0, 0))

    def draw_text(self):
        self.instruct_surf = self.instruct_font.render('Press ENTER to start the game.', False, (10, 10, 10))
        self.instruct_rect = self.instruct_surf.get_rect(center = (960, 540))
        SCREEN.blit(self.instruct_surf, self.instruct_rect)
        SCREEN.blit(self.surface, self.rect)


        
            
    def update(self, current_score):
        self.display_score(current_score)


class Life:
    def __init__(self):

        self.starting_hearts = [1, 1, 1]

        self.current_hearts = self.starting_hearts

        self.surface = pygame.image.load("assets/heart.png").convert_alpha()

        self.rect = self.surface.get_rect()

        # self.font = pygame.font.SysFont("arial", 50)
        self.score_font = pygame.font.Font('assets/RETRO_SPACE.ttf', 50)

    def draw_hearts(self):

        # draw LIFE text
        self.life_counter = self.score_font.render(f"LIFE ", False, (10, 25, 25))
        SCREEN.blit(self.life_counter, (1440, 70))

        self.hearts = self.current_hearts
        
        #check hearts
        
        # blit for each heart with an offset
        #print(len(self.hearts))
        if len(self.hearts) == 3:
            #self.heart1 = self.surface.get_rect(center = (1600, 70))
            SCREEN.blit(self.surface, (1600, 60))

        if len(self.hearts) >= 2:
            SCREEN.blit(self.surface, (1680, 60))

        if len(self.hearts) >= 1:
            SCREEN.blit(self.surface, (1760, 60))
        
    def reset_hearts(self):

        self.current_hearts = [1, 1, 1]
        
        # get the collision boolean
        # update the hearts amount if takemn damage
        

        



        


        

