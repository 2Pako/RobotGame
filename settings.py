#Creating a settings file to keep track of game settings


class Settings:
    """Settings for the game"""

    def __init__(self):

        #screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (80,80,80)
        #ship settings
        self.ship_speed = .3


