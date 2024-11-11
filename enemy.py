#Handles the enemy

import pygame

class BadRobot:
    """Class to manage the robot"""

    def __init__(self,robot_game):
        """Init the robot and sets its starting position"""
        self.screen = robot_game.screen
        self.screen_rect = robot_game.screen.get_rect()
        self.settings = robot_game.settings
        #load the robot and get its rect.
        #note: image must be 120 by 107 pixels
        self.image =pygame.image.load('images/Robot.png')
        self.rect = self.image.get_rect()
        #Start each robot at the center of the screen.
        self.rect.top = self.screen_rect.top
         #Store a decimal value for the enemy's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self, player_x, player_y):
        """Update the enemy's position based new destination"""
        self._check_direction(player_x, player_y)
        #update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def _check_direction(self, player_x, player_y):
        """Check the direction the enemy is moving.
            Take the player location and make enemy move towards"""
        #current location
        x0 = self.x
        y0 = self.y
        #step = (new - old)/speed
        step_x = (player_x - x0)/self.settings.enemy_speed 
        step_y = (player_y-y0)/self.settings.enemy_speed
        self.x += step_x
        self.y += step_y

        return [step_x,step_y]
 
    
    def blitme(self):
        """Draw the ship at the center of the location"""
        self.screen.blit(self.image, self.rect)