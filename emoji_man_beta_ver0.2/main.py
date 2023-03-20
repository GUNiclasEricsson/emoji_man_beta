# imports the library/module pygame
import pygame
# imports all variables, functions and classes
from settings import *
from emojienemy import EmojiEnemy
from emojiman import EmojiMan, FlyingEmoji, FlyingClouds
from gamemap import GameMap, BACKGROUND
from scores import Watermelon, Apples, Scores, Score, Life
# calls the init method to init the modules 
pygame.init()

# loads the music file and plays loops it forever
pygame.mixer.music.load("assets/emoji_man_song3.mp3")
pygame.mixer.music.play(loops =- 1)

# the running variable takes the boolean true to be able to use in the while-loop
running = True

# creates an instance of the Clock class for keeping the framerate
clock = pygame.time.Clock() 
sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
fruits = pygame.sprite.Group()
start_sprites = pygame.sprite.Group() 

level = GameMap()

enemy_1 = EmojiEnemy(start_x= 870, start_y= 120, steps= 90, speed = 5)
enemy_2 = EmojiEnemy(start_x= 1270, start_y= 480, steps= 17, speed = 6)
enemy_3 = EmojiEnemy(start_x= 1000, start_y= 800, steps = 80, speed = 10)
enemy_4 = EmojiEnemy(start_x= 1800, start_y= 300, steps = 40, speed = 5)
enemy_5 = EmojiEnemy(start_x= 1070, start_y= 480, steps = 65, speed = 3)
enemies.add(enemy_1, enemy_2, enemy_3, enemy_4, enemy_5)

player_1 = EmojiMan(player)
player.add(player_1)

flying_emoji = FlyingEmoji() 
clouds = FlyingClouds()

water_melon01 = Watermelon(sprites)
apple_01 = Apples(sprites)
all_fruits = [water_melon01, apple_01]
fruits.add(all_fruits)
scores = Scores(fruits)
score = Score()
hearts = Life()

sprites.add(player_1, enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, water_melon01, apple_01)

level.draw_map([collision_sprites, sprites])

started = False
taken_damage = False
current_time = 0
damaged_time = 0
current_score = 0
invincible = False


# while run the main game loop as long as the value is True
while running: 
    # goes trough each event in the .get method from the .event module 
    # they are stored as a (object)?    
    for event in pygame.event.get():

        # checks if the type of event is a key being pressed
        if event.type == pygame.KEYDOWN:
            if event.key == ESC:
                running = False
            if event.key == ENTER and started == False:
                    scores.current_score = score.score_reset()
                    running = True
                    sprites.add(player_1, enemy_1, enemy_2, enemy_3, water_melon01, apple_01)
                    fruits.add(all_fruits)
                    player_1.rect.center = (100, 200)
                    started = True
        elif event.type == SPAWN_CLOUD:
                flying_cloud = FlyingClouds()
                start_sprites.add(flying_cloud)
        if started == False:
            if event.type == SPAWN_EMOJI:
                flying_emoji = FlyingEmoji()
                start_sprites.add(flying_emoji)      
    
    if running:
        SCREEN.blit(BACKGROUND, (0, 0))
        key = pygame.key.get_pressed()
        player.update(key)
        enemies.update()
        player_1.collision(player = player_1, collision_sprites = collision_sprites)

        if player_1.power_up == False:
            for enemy in enemies:
                if pygame.Rect.colliderect(player_1.rect, enemy.rect):
                    taken_damage = True 

        scores.get_scores(player_1)

        if taken_damage:

            player_1.surface = EMOJI_DAMAGED
            offset_x = 10 + player_1.rect.topright[0]
            offset_y = player_1.rect.topright[1]
            offset = (offset_x, offset_y)
            SCREEN.blit(OUCH, offset)
            is_damaged = True
            if is_damaged == True:
                current_time = pygame.time.get_ticks()

                damaged_time = current_time + 400

                taken_damage = False
                if invincible == False and len(hearts.current_hearts) != 0:
                    invincible = True
                    hearts.current_hearts.remove(1)
        new_time = pygame.time.get_ticks()

        if new_time >= damaged_time:
            
            player_1.surface = pygame.image.load(EMOJI_SURFACE).convert()
            is_damaged = False
            invincible = False

        for sprite in start_sprites:   

            sprite.fly(started)
            SCREEN.blit(sprite.surface, sprite.rect)
        for sprite in sprites:

            SCREEN.blit(sprite.surface, sprite.rect)
        score.update(scores.current_score)
        hearts.draw_hearts()
        
    if started == False:
        score.start_screen()
        score.draw_text() 
        for sprite in start_sprites:   
            sprite.fly(started)
            SCREEN.blit(sprite.surface, sprite.rect)
        invincible = True   
    if scores.current_score == 2 or len(hearts.current_hearts) == 0 or player_1.rect.bottom > 2000:        
        score.game_over(scores.current_score)
        print(scores.current_score)
        for sprite in start_sprites:   
            sprite.fly(started)
            SCREEN.blit(sprite.surface, sprite.rect)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                scores.current_score = score.score_reset()
                hearts.reset_hearts()
                running = True
                sprites.add(player_1, enemy_1, enemy_2, enemy_3, water_melon01, apple_01)
                fruits.add(all_fruits)
                player_1.rect.center = (100, 200)
    
    pygame.display.flip()
    # calls the .tick method an passing the FPS variable as an argument for keeping the framerate locked
    clock.tick(FPS)
                
pygame.quit()



