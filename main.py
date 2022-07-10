import sys
from turtle import Screen
import pygame
from game_stats import GameStats
from settings import Settings
from spaceship import SpaceShip
import bullets
import invasors
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

        # enemies
        self.invasors_bullets = pygame.sprite.Group()
        self.invasors = pygame.sprite.Group()
        self.bosses = pygame.sprite.Group()
        self.boss_bullets = pygame.sprite.Group()

       # game stats
        self.stats = GameStats(self)
        self.score = Score(self)
        self.lives_table = Lives(self)

        # game clock
        self.time_elapsed_game = 0
        self.time_elapsed_fleets = 0
        self.time_invasors_bullets_cooldowns = 0
        self.time_boss_bullets_cooldowns = 0
        self.clock = pygame.time.Clock()

        # background
        self.bg = pygame.image.load(
            'images\d775ufv-b90740cd-0664-48a1-9de9-04518f65b857.png')

        # teste
        self.bg_size = self.bg.get_size()
        self.bg_rect = self.bg.get_rect()
        self.screen = pygame.display.set_mode(self.bg_size)
        self.w = self.settings.screen_width
        self.h = self.settings.screen_height
        self.bg_y = 0
        self.bg_y1 = -self.h

        # Play button
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
                self._fleet_bullets()
                self._boss_bullets()
                self._update_invasors()
                # clock related
                self.clock_ticks = self.clock.tick()
                self.time_elapsed_fleets += self.clock_ticks
                self.time_invasors_bullets_cooldowns += self.clock_ticks
                self.time_boss_bullets_cooldowns += self.clock_ticks

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
        self.invasors_bullets.update()
        self.boss_bullets.update()

        # Delete old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 or bullet.rect.bottom > self.settings.screen_height:
                self.bullets.remove(bullet)

        collision = pygame.sprite.groupcollide(
            self.bullets, self.invasors, True, True)

        boss_collision = pygame.sprite.groupcollide(
            self.bullets, self.bosses, True, False)

        if boss_collision:
            self.settings.Redboss_health -= 1
            if self.settings.Redboss_health < 1:
                self.bosses.empty()
                self.stats.score += 320
                self.score.prep_score()
                self.stats.boss_status = False
                self.settings.Redboss_health = 10

            # if the boss is active the enimies gives no points
        if collision and self.stats.boss_status == False:
            self.stats.score += 20
            self.score.prep_score()

         # Delete old bullets of invasors
        for bullet in self.invasors_bullets.copy():
            if bullet.rect.bottom > self.settings.screen_height:
                self.invasors_bullets.remove(bullet)

        collision_invasors_bullets = pygame.sprite.spritecollide(
            self.spaceship, self.invasors_bullets, True)

        if collision_invasors_bullets:
            self.stats.spaceships_left -= 1
            self.lives_table.prep_lives()

        for bullet in self.boss_bullets.copy():
            if bullet.rect.bottom > self.settings.screen_height:
                self.boss_bullets.remove(bullet)

        collision_boss_bullets = pygame.sprite.spritecollide(
            self.spaceship, self.boss_bullets, True)

        if collision_boss_bullets:
            self.stats.spaceships_left -= 1
            self.lives_table.prep_lives()

    def _update_invasors(self):
        # Update the invasors y pos
        self.invasors.update()
        self.bosses.update()

        if pygame.sprite.spritecollide(self.spaceship, self.invasors, True):
            self.stats.spaceships_left -= 1
            self.lives_table.prep_lives()
        if self.stats.spaceships_left <= 0:
            self.stats.game_running = False

        if pygame.sprite.spritecollide(self.spaceship, self.bosses, True):
            self.stats.spaceships_left -= 1
            self.lives_table.prep_lives()
        if self.stats.spaceships_left <= 0:
            self.stats.game_running = False

        for invasor in self.invasors.copy():
            if invasor.rect.bottom > self.settings.screen_height + 50:
                self.invasors.remove(invasor)
            if invasor.rect.left < 0:
                self.settings.invasor_direction = 1
            if invasor.rect.right > self.settings.screen_width:
                self.settings.invasor_direction = -1

        for boss in self.bosses.copy():
            if boss.rect.left < 0:
                self.settings.boss_direction = 1
            if boss.rect.right > self.settings.screen_width:
                self.settings.boss_direction = -1

    def _update_screen(self):
        # redraw the screen each pass
        self.screen.blit(self.bg, [0, self.bg_y-25])
        self.screen.blit(self.bg, [0, self.bg_y1-25])
        # teste
        if self.stats.game_running:
            self.bg_y1 += 0.5
            self.bg_y += 0.5
            if self.bg_y > self.h:
                self.bg_y = -self.bg_y
            if self.bg_y1 > self.h:
                self.bg_y1 = -self.h

        self.spaceship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.invasors_bullets.sprites():
            bullet.draw_bullet()
        self.invasors.draw(self.screen)
        self.bosses.draw(self.screen)
        self.boss_bullets.draw(self.screen)

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
            new_bullet = bullets.Bullets(self)
            self.bullets.add(new_bullet)

    def _check_play_button(self, mouse_pos):
        """Start a new game"""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_running:
            self.stats.game_running = True
            self.stats.initialize_stats()
            self.score.prep_score()
            self.lives_table.prep_lives()

    def _enemy_spawn(self):
        enemy_list = ['green', 'green', 'green', 'blue']
        spawn_enemy = random.choice(enemy_list)
        return spawn_enemy

    def _create_fleat(self):
        if self.settings.max_number_of_invasors > len(self.invasors) and self.time_elapsed_fleets > 500:
            enemy_spawn = self._enemy_spawn()
            if enemy_spawn == 'green' and self.stats.boss_status == False:
                green_invasor = invasors.GreenInvasors(self)
                invasors_width = green_invasor.rect.width
                green_invasor.y = -50
                green_invasor.x = random.randint(
                    invasors_width, self.settings.screen_width - invasors_width)
                green_invasor.rect.x = green_invasor.x
                green_invasor.rect.y = green_invasor.y
                green_invasor.add(self.invasors)
                self.time_elapsed_fleets = 0
            if enemy_spawn == 'blue' and self.stats.boss_status == False:
                blue_invasor = invasors.BlueInvasors(self)
                invasors_width = blue_invasor.rect.width
                blue_invasor.y = -50
                blue_invasor.x = random.randint(
                    invasors_width, self.settings.screen_width - invasors_width)
                blue_invasor.rect.x = blue_invasor.x
                blue_invasor.rect.y = blue_invasor.y
                blue_invasor.add(self.invasors)
                self.time_elapsed_fleets = 0
            if self.stats.score % 100 == 0 and self.stats.score != 0 and self.stats.boss_status == False:
                self.stats.boss_status = True
                boss = invasors.RedBoss(self)
                boss.y = -50
                boss.x = self.settings.screen_width / 2
                boss.rect.x = boss.x
                boss.rect.y = boss.y
                boss.add(self.bosses)
            if self.stats.boss_status and self.time_elapsed_fleets == 1000:
                yellow_invasor = invasors.YellowInvasors(self)
                invasors_width = yellow_invasor.rect.width
                yellow_invasor.y = -50
                yellow_invasor.x = random.randint(
                    invasors_width, self.settings.screen_width - invasors_width)
                yellow_invasor.rect.x = yellow_invasor.x
                yellow_invasor.rect.y = yellow_invasor.y
                yellow_invasor.add(self.invasors)
                self.time_elapsed_fleets = 0

    def _fleet_bullets(self):
        if self.time_invasors_bullets_cooldowns > 250 and len(self.invasors) >= 1 and self.stats.boss_status == False:
            new_bullet = bullets.InvasorsBullets(self)
            self.invasors_bullets.add(new_bullet)
            self.time_invasors_bullets_cooldowns = 0

    def _boss_bullets(self):
        if self.time_boss_bullets_cooldowns > 750 and self.bosses:
            new_bullet = bullets.BossBullets(self)
            self.boss_bullets.add(new_bullet)
            self.time_boss_bullets_cooldowns = 0


if __name__ == '__main__':
    si = SpaceInvaders()
    si.main_loop()
