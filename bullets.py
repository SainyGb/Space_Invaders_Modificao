import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):

    def __init__(self, si):
        super().__init__()
        self.screen = si.screen
        self.settings = si.settings
        self.color = si.settings.bullet_color

        self.rect = pygame.Rect(
            (0, 0), (self.settings.bullet_width, self.settings.bullet_height))

        self.rect.midtop = si.spaceship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class InvasorsBullets(Sprite):

    def __init__(self, si):
        super().__init__()
        self.screen = si.screen
        self.settings = si.settings
        self.color = 0, 0, 139

        self.rect = pygame.Rect(
            (0, 0), (self.settings.bullet_width, self.settings.bullet_height))

        for invasor in si.invasors:
            self.rect.midtop = invasor.rect.midtop
            self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class BossBullets(Sprite):

    def __init__(self, si):
        super().__init__()
        self.screen = si.screen
        self.settings = si.settings

        self.image = pygame.image.load(
            'images\gray-missile-pixel-art-maker-53754.bmp')
        self.image = pygame.transform.scale(self.image, (62, 100))
        self.rect = self.image.get_rect()

        for boss in si.bosses:
            self.rect.midtop = boss.rect.midtop
            self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bullet_speed
        self.rect.y = self.y
