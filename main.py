import sys
import pygame
from game_stats import GameStats
from settings import Settings
from spaceship import SpaceShip
from bullets import Bullets
from invasors import GreenInvasors
import random
from buttons import Buttons
from score import Score
from lives_table import Lives


class SpaceInvaders:
    """Assets and behavior"""

    def __init__(self):
        """Starts the game and configs"""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Invaders")

        self.spaceship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()
        self.green_invasors = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.score = Score(self)
        self.lives_table = Lives(self)

        # game clock
        self.time_elapsed_game = 0
        self.time_elapsed_fleets = 0
        self.clock = pygame.time.Clock()

        # background color
        self.bg_color = self.settings.back_color

        self.play_button = Buttons(self, "Play")

    def main_loop(self):
        """Initialize the main loop"""
        while True:

            self._check_events()
            self._update_screen()

            if self.stats.game_running:
                self._update_bullets()
                self.spaceship.update()
                self._create_fleat()
                self._update_invasors()
                # clock related
                self.clock_ticks = self.clock.tick()
                self.time_elapsed_fleets += self.clock_ticks

            # Deleting bullets that cross the top screen

    def _check_events(self):
        """Keypresses and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _update_bullets(self):
        # Update the bullet y pos
        self.bullets.update()

        # Delete old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        collision = pygame.sprite.groupcollide(
            self.bullets, self.green_invasors, True, True)

        if collision:
            self.stats.score += 20
            self.score.prep_score()

    def _update_invasors(self):
        # Update the invasors y pos
        self.green_invasors.update()
        if pygame.sprite.spritecollide(self.spaceship, self.green_invasors, True):
            self.stats.spaceships_left -= 1
            self.lives_table.prep_lives()
        if self.stats.spaceships_left <= 0:
            self.stats.game_running = False

        for invasor in self.green_invasors.copy():
            if invasor.rect.bottom > self.settings.screen_height + 50:
                self.green_invasors.remove(invasor)

    def _update_screen(self):
        # redraw the screen each pass
        self.screen.fill(self.settings.back_color)
        self.spaceship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.green_invasors.draw(self.screen)

        self.score.draw_score()
        self.lives_table.draw_lives()

        if self.stats.game_running == False:
            self.play_button.draw_button()

        # make the most recently screen visible
        pygame.display.flip()

    def _keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.spaceship.move_right = True
        if event.key == pygame.K_LEFT:
            self.spaceship.move_left = True
        if event.key == pygame.K_UP:
            self.spaceship.move_up = True
        if event.key == pygame.K_DOWN:
            self.spaceship.move_down = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

        # FOR DEV TEST ONLY, REMEMBER TO COMMENT LATER
        if event.key == pygame.K_e:
            sys.exit()

    def _keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.spaceship.move_right = False
        if event.key == pygame.K_LEFT:
            self.spaceship.move_left = False
        if event.key == pygame.K_UP:
            self.spaceship.move_up = False
        if event.key == pygame.K_DOWN:
            self.spaceship.move_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_limit:
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet)

    def _check_play_button(self, mouse_pos):
        """Start a new game"""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_running:
            self.stats.game_running = True
            self.stats.initialize_stats()
            self.score.prep_score()
            self.lives_table.prep_lives()

    def _create_fleat(self):
        if self.settings.max_number_of_invasors > len(self.green_invasors) and self.time_elapsed_fleets > 500:
            green_invasor = GreenInvasors(self)
            invasors_width = green_invasor.rect.width
            green_invasor.y = -50
            green_invasor.x = random.randint(
                invasors_width, self.settings.screen_width - invasors_width)
            green_invasor.rect.x = green_invasor.x
            green_invasor.rect.y = green_invasor.y
            green_invasor.add(self.green_invasors)
            self.time_elapsed_fleets = 0


if __name__ == '__main__':
    si = SpaceInvaders()
    si.main_loop()
