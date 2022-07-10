class GameStats:
    """Track clock and other statistics."""

    def __init__(self, si_game):
        self.settings = si_game.settings
        self.si_game = si_game
        self.initialize_stats()
        self.game_running = False
        self.boss_status = False
        self.power_up = 0

    def initialize_stats(self):
        """Initialize stats."""
        self.spaceships_left = self.settings.spaceship_lifes
        self.si_game.invasors.empty()
        self.si_game.bullets.empty()
        self.si_game.invasors_bullets.empty()
        self.si_game.bosses.empty()
        self.si_game.boss_bullets.empty()
        self.boss_status = False
        self.score = 0
