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

    def update(self):
        """Update the ship's position based on the movement flag"""
        self._check_direction()
        #update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    
    def blitme(self):
        """Draw the ship at the center of the location"""
        self.screen.blit(self.image, self.rect)