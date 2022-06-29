import pygame
from pygame.sprite import Sprite


class GreenInvasors(Sprite):

    def __init__(self, si_game):
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings

        self.image = pygame.image.load('images\Green-ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        self.y += self.settings.invasors_speed
        self.rect.y = self.y
