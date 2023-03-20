import pygame
from settings import *

class Tile1(pygame.sprite.Sprite):
    def __init__(self, pos1, groups):
        super().__init__(groups)
        self.surface = pygame.image.load(EMOJI_TILE01).convert()
        self.rect = self.surface.get_rect(topleft = pos1)

class Tile2(pygame.sprite.Sprite):
    def __init__(self, pos1, groups):
        super().__init__(groups)
        self.surface = EMOJI_TILE02
        self.rect = self.surface.get_rect(topleft = pos1)

class Tile3(pygame.sprite.Sprite):
    def __init__(self, pos1, groups):
        super().__init__(groups)
        self.surface = EMOJI_TILE03
        self.rect = self.surface.get_rect(topleft = pos1)