import pygame
from settings import Settings


class SpaceShip:
    """Make the ship work"""

    def __init__(self, si_game):
        """Initialize the ship and set the start pos"""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()
        self.settings = Settings()

        # Load the image

        image = pygame.image.load('images\pixel-spaceship-better.bmp')
        self.IMAGE_SMALL = pygame.transform.scale(image, (50, 50))
        self.rect = self.IMAGE_SMALL.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # Decimal value for the ship's horizontal pos
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movement
        self.move_right = False
        self.move_left = False
        self.move_down = False
        self.move_up = False

    def blitme(self):
        """Draw the ship in the current location"""
        self.screen.blit(self.IMAGE_SMALL, self.rect)

    def update(self):
        """Ship position based on the move flag"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.move_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # updating rect object based on self.x
        self.rect.x = self.x
        self.rect.y = self.y
