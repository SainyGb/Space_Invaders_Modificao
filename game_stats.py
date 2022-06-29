class GameStats:
    """Track clock and other statistics."""

    def __init__(self, si_game):
        self.settings = si_game.settings
        self.si_game = si_game
        self.initialize_stats()
        self.game_running = False

    def initialize_stats(self):
        """Initialize stats."""
        self.spaceships_left = self.settings.spaceship_lifes
        self.si_game.green_invasors.empty()
        self.si_game.bullets.empty()
        self.score = 0
