import pygame.font


class Lives:
    """A class to report scoring information."""

    def __init__(self, si_game):
        """Initialize liveskeeping attributes."""
        self.screen = si_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = si_game.settings
        self.stats = si_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial lives image.
        self.prep_lives()

    def prep_lives(self):
        """Turn the lives into a rendered image."""
        lifes_str = str(self.stats.spaceships_left)
        self.lives_image = self.font.render(lifes_str, True,
                                            self.text_color, self.settings.back_color)

        # lives at the top left of the screen.
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = self.screen_rect.left + 20
        self.lives_rect.top = 20

    def draw_lives(self):
        self.screen.blit(self.lives_image, self.lives_rect)
