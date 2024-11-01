import sys
import pygame
from settings import Settings

class RobotGame:
    # Game class
    def __init__(self):
        """Init the game and create resources"""
        pygame.init()
        self.settings = Settings()

        #screen 
        self.screen = pygame.display.set_mode([self.settings.screen_width,self.settings.screen_height])
        pygame.display.set_caption("RobotGame")




    def run_game(self):
        """Start the main loop or the game"""
        while True:
            #Watch for user input
            self._check_events()


    def _check_events(self):
        """Respond to user input """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

if __name__ == '__main__':
    """make a game instance, and run the game"""
    ai = RobotGame()
    ai.run_game()