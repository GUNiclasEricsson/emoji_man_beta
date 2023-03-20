import pygame

from settings import *

from tiles import Tile1, Tile2, Tile3


BACKGROUND = pygame.image.load("assets/emoji_man_background.png").convert()


class GameMap(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.image.load(EMOJI_TILE01).convert()
        self.rect = self.surface.get_rect()
        #self.groups = 1 #groups


    def draw_map(self, groups):
        for r_index, row in enumerate(GAME_MAP):
                for c_index, col in enumerate(row):
                    x = c_index * RECT_SIZE
                    y = r_index * RECT_SIZE
                    if col == 1:
                        Tile1((x, y), groups= groups)
                    if col == 2:
                         Tile2((x, y), groups= groups)
                    if col == 3:
                         Tile3((x, y), groups= groups)
                    