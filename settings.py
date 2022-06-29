class Settings:
    """Self explanatory"""

    def __init__(self):
        """starts the game's settings"""
        self.screen_width = 600
        self.screen_height = 800
        self.back_color = (5, 55, 123)

        # ship settings
        self.ship_speed = 0.17
        self.spaceship_lifes = 3

        # bullet settings
        self.bullet_speed = 0.3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (192, 0, 0)
        self.bullets_limit = 7

        # Invasor setting
        self.invasors_speed = 0.15
        self.max_number_of_invasors = 10
