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


class BlueInvasors(Sprite):

    def __init__(self, si_game):
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings

        self.image = pygame.image.load('images\Blue-ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        self.x += self.settings.invasors_speed * self.settings.invasor_direction
        self.y += self.settings.invasors_speed
        self.rect.y = self.y
        self.rect.x = self.x


class YellowInvasors(Sprite):

    def __init__(self, si_game):
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.health = 3

        self.image = pygame.image.load('images\meteor.bmp')
        self.image = pygame.transform.scale(self.image, (84, 84))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        self.y += self.settings.invasors_speed
        self.rect.y = self.y


class RedBoss(Sprite):

    def __init__(self, si_game):
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings

        self.image = pygame.image.load(
            'images\enemy_spaceship_by_sethenius_d92ziiw-fullview.bmp')
        self.image = pygame.transform.scale(self.image, (180, 180))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        if self.rect.y < 100:
            self.y += self.settings.invasors_speed
            self.rect.y = self.y
        else:
            self.x += self.settings.boss_speed * self.settings.boss_direction
            self.rect.x = self.x
