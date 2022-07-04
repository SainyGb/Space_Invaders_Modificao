class Settings:
    """Self explanatory"""

    def __init__(self):
        """starts the game's settings"""
        self.screen_width = 800
        self.screen_height = 600
        self.back_color = (5, 2, 3)
        self.text_color = (49, 0, 71)

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
        self.invasor_direction = -1
        self.max_number_of_invasors = 10
