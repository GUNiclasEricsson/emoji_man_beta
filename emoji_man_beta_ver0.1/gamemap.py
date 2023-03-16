import pygame

from settings import *

from tiles import Tile1, Tile2


BACKGROUND = pygame.image.load("assets/emoji_man_background.png").convert()


class GameMap(pygame.sprite.Sprite):
    def __init__(self, pos1, groups):
        super().__init__(groups)
        self.surface = pygame.image.load(EMOJI_TILE01).convert()

        self.rect = self.surface.get_rect(topleft = pos1)


        self.groups = groups
        #rows = 0

        #self.position_y = 0
        #self.position_x = 0
        #for r_index, row in enumerate(GAME_MAP):
        #    for c_index, col in enumerate(row):
        #        x = c_index * RECT_SIZE
        #        y = r_index * RECT_SIZE
        #        if col == 1:
        #            print("1")

    def draw_map(self, groups):
        for r_index, row in enumerate(GAME_MAP):
                for c_index, col in enumerate(row):
                    x = c_index * RECT_SIZE
                    y = r_index * RECT_SIZE
                    if col == 1:
                        #print("1")
                        #print(x, y)
                        Tile1((x, y), groups= groups)
                        #print(Tile1.groups)
                    #if col == 2:
                    #     self.position_x = x
                    #     self.position_y = y
                    #     print(x, y)
                    if col == 2:
                         Tile2((x, y), groups= groups)
                    