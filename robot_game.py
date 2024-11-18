import sys
import pygame
from settings import Settings
from robot import Robot
from enemy import BadRobot

class RobotGame:
    # Game class
    def __init__(self):
        """Init the game and create resources"""
        pygame.init()
        self.settings = Settings()
        #screen 
        self.screen = pygame.display.set_mode([self.settings.screen_width,self.settings.screen_height])
        pygame.display.set_caption("RobotGame")
        #instance of Robot
        self.robot = Robot(self)
        self.enemy = BadRobot(self)
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start the main loop or the game"""
        while True:
            #Watch for user input
            self._check_events()
            #Check for update to the robot position
            self.robot.update()
            #Check for update to the enemy's position
            self.enemy.update(self.robot.x, self.robot.y)
            #Redraw the screen during each pass
            self.clock.tick(self.settings.frame_rate)    
            self._update_screen()

    def _check_events(self):
        """Respond to user input """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events((event))
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events((event))
                
    def _check_keydown_events(self, event):
        """Respods to a keypress"""
        if event.key == pygame.K_RIGHT:
                self.robot.moving_right = True
        if event.key == pygame.K_LEFT:
                self.robot.moving_left = True
        if event.key == pygame.K_UP:
                self.robot.moving_up = True
        if event.key == pygame.K_DOWN:
                self.robot.moving_down = True
        if event.key == pygame.K_q:
                sys.exit()

    def _check_keyup_events(self, event):
        """Respods to a releases"""
        if event.key == pygame.K_RIGHT:
                self.robot.moving_right = False
        elif event.key == pygame.K_LEFT: 
                self.robot.moving_left = False
        elif event.key == pygame.K_UP: 
                self.robot.moving_up = False
        elif event.key == pygame.K_DOWN: 
                self.robot.moving_down = False

    def _update_screen(self):
        """Redraw the screen during each pass"""

        self.screen.fill(self.settings.bg_color)
        #load robot
        self.robot.blitme()
        #load bad robot
        self.enemy.blitme()
        # Make the most recent screen visible
        pygame.display.flip()

if __name__ == '__main__':
    """make a game instance, and run the game"""
    ai = RobotGame()
    ai.run_game()