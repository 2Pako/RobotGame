#Creating a settings file to keep track of game settings

class Settings:
    """Settings for the game"""

    def __init__(self):
        #screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (80,80,80)
        self.frame_rate = 60
        #ship settings
        self.robot_speed = 5
        # the bigger the slower the enemy moves
        self.enemy_speed = 2


