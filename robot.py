#Handles the player 

import pygame

class Robot:
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
        self.rect.center = self.screen_rect.center
        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.image = pygame.image.load("images/Robot_Side.png")
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.image = pygame.transform.flip(pygame.image.load("images/Robot_Side.png"),flip_x=1 ,flip_y=0)
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.image = pygame.image.load("images/Robot.png")
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.image = pygame.transform.flip(pygame.image.load("images/Robot.png"),flip_x=0 ,flip_y=1)
            self.y += self.settings.ship_speed
        #update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at the center of the location"""
        self.screen.blit(self.image, self.rect)