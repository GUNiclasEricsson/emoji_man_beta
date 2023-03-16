# imports the library/module pygame
import pygame

# imports all variables, functions and classes
from settings import *

from emojienemy import EmojiEnemy

from emojiman import EmojiMan, FlyingEmoji, FlyingClouds

from gamemap import GameMap, BACKGROUND

#from tiles import Tile1

from scores import Watermelon, Apples, Scores, Score, Life

# calls the init method to init the modules 
pygame.init()

# the running variable takes the boolean true to be able to use in the while-loop
running = True


# creates an instance of the Clock class for keeping the framerate

clock = pygame.time.Clock() 
sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
fruits = pygame.sprite.Group()
start_sprites = pygame.sprite.Group() #

level = GameMap((0, 0), sprites)

enemy_1 = EmojiEnemy(start_x= 720, start_y= 120, steps= 450, speed = 5)
enemy_2 = EmojiEnemy(start_x= 1270, start_y= 520, steps= 110, speed = 1)
enemy_3 = EmojiEnemy(start_x= 1000, start_y= 800, steps = 800, speed = 10)
enemies.add(enemy_1, enemy_2, enemy_3)

player_1 = EmojiMan(player)
player.add(player_1)

flying_emoji = FlyingEmoji() #
clouds = FlyingClouds()
#level = GameMap((0, 0), sprites)

#def draw():
#    for r_index, row in enumerate(GAME_MAP):
#                for c_index, col in enumerate(row):
#                    x = c_index * RECT_SIZE
#                    y = r_index * RECT_SIZE
#                    if col == 1:
#                        #print("1")
#                        print(x, y)
#
#    level = GameMap((x, y), sprites)
#    return level

#draw()



water_melon01 = Watermelon(sprites)
apple_01 = Apples(sprites)
all_fruits = [water_melon01, apple_01]
fruits.add(all_fruits)#water_melon01, apple_01)
scores = Scores(fruits)
score = Score()


sprites.add(player_1, enemy_1, enemy_2, enemy_3, water_melon01, apple_01)

level.draw_map([collision_sprites, sprites])

#is_damaged = False
started = False
taken_damage = False
current_time = 0
damaged_time = 0
current_score = 0
invincible = False


hearts = Life()

# while run the main game loop as long as the value is True
while running: 
    # goes trough each event in the .get method from the .event module 
    # they are stored as a (object)?
    #flying_emoji.fly()
    
    for event in pygame.event.get():
        #print(pygame.KEYDOWN)
        #print(event)
        # checks if the type of event is a key being pressed
        if event.type == pygame.KEYDOWN:
            if event.key == ESC:
                running = False
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
        #player_1.apply_gravity()

        enemies.update()

        

        #clouds.fly()
        

        #print(enemies)
        
        #level.draw_map(sprites)


        player_1.collision(player = player_1, collision_sprites = collision_sprites)



        #test_col = pygame.sprite.groupcollide(player, collision_sprites, False, False) 
        #for element in collision_sprites:
        #    if pygame.Rect.colliderect(player_1.rect, element.rect):
                
                
        #        print(element.rect, "COLLISION")
            #print(element.rect)

        if player_1.power_up == False:
            for enemy in enemies:
                if pygame.Rect.colliderect(player_1.rect, enemy.rect):
                    taken_damage = True #pygame.Rect.colliderect(player_1.rect, enemy_1.rect)
        #print(collide)

        scores.get_scores(player_1)

        #water_melon01.get_score(player_1)
        #test1 = Scores(Watermelon, Apples)
        #test1.get_score(player= player_1)

        if taken_damage:
            #print("DIE!", player_1.rect, enemy_1.rect)
            player_1.surface = EMOJI_DAMAGED
            offset_x = 10 + player_1.rect.topright[0]
            offset_y = player_1.rect.topright[1]
            offset = (offset_x, offset_y)
            #print(f"offset: {offset}")
            SCREEN.blit(OUCH, offset)
            #print(player_1.rect.topright)
            
            
            #print(is_damaged)
            is_damaged = True
            if is_damaged == True:
                current_time = pygame.time.get_ticks()
                print(f"CURRENT:{current_time}")
                #print(current_time)
                damaged_time = current_time + 400
                print(f"DAMAGED:{damaged_time}")
                #print(damaged_time)
                taken_damage = False
                if invincible == False and len(hearts.current_hearts) != 0:
                    invincible = True
                    hearts.current_hearts.remove(1)
                    
                print(is_damaged)

            
        new_time = pygame.time.get_ticks()
        #print(f"NEW:{new_time}")
        if new_time >= damaged_time:
            

            player_1.surface = pygame.image.load(EMOJI_SURFACE).convert()
            is_damaged = False
            invincible = False


        for sprite in start_sprites:   
            #print(sprite.surface, sprite.rect)
            sprite.fly(started)
            SCREEN.blit(sprite.surface, sprite.rect)
        for sprite in sprites:
            #print(sprite.surface, sprite.rect)
            SCREEN.blit(sprite.surface, sprite.rect)

        #sprites.draw(SCREEN)
        #for player in player.sprites():
        #    print(player.rect)
        #    for enemy in enemies.sprites():
        #        print(enemy.rect)



        score.update(scores.current_score)
        hearts.draw_hearts()
        

    if started == False:
        #score.game_over(scores.current_score)
        score.start_screen()
        
        
        for sprite in start_sprites:   
            #print(sprite.surface, sprite.rect)
            sprite.fly(started)
            SCREEN.blit(sprite.surface, sprite.rect)
            
        score.draw_text() 
        invincible = True   
                
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ENTER:
                    scores.current_score = score.score_reset()
                    running = True
                    sprites.add(player_1, enemy_1, enemy_2, enemy_3, water_melon01, apple_01)
                    fruits.add(all_fruits)
                    player_1.rect.center = (100, 200)
                    started = True
            
            #elif event.type == SPAWN_EMOJI:
            #    flying_emoji = FlyingEmoji()
            #    start_sprites.add(flying_emoji)

            #elif event.type == SPAWN_CLOUD:
            #    flying_cloud = FlyingClouds()
            #    start_sprites.add(flying_cloud)
                
                
                #print(start_sprites)
                
                #SCREEN.blit(flying_emoji.surf, flying_emoji.rect)
                #print("SPAWNING")
        
            #pygame.display.flip()
            
            
        
        
    if scores.current_score == 2 or len(hearts.current_hearts) == 0 or player_1.rect.bottom > 2000:        
        score.game_over(scores.current_score)
        print(scores.current_score)
        #hearts.reset_hearts()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                #hearts.reset_hearts(hearts.current_hearts)
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



