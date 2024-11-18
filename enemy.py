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
        vector = pygame.math.Vector2
        #current location
        x0 = self.x
        y0 = self.y
        #need direction vector and normalize. 
        delta = vector(player_x - x0, player_y - y0).normalize()
        #Adjust for speed
        movement = delta * self.settings.enemy_speed
        #change image based on movement
        stepX = movement[0]
        stepY = movement[1]
        print(stepX, stepY)
        if stepX > 0 and stepY > 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/Robot.png"), -135)
        if stepX < 0 and stepY > 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/Robot.png"), 135)
        if stepX < 0 and stepY < 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/Robot.png"), 45)
        if stepX > 0 and stepY < 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/Robot.png"), -45)
        if stepX == 0 and stepY == 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/Robot.png"), 0)
        if stepX == 0 and stepY > 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/Robot.png"), 0)
        if stepX == 0 and stepY < 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/Robot.png"), 180)
        if stepX > 0 and stepY == 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/Robot.png"), 90)
        if stepX < 0 and stepY == 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/Robot.png"), 270)
        #move x and y
        self.x += stepX
        self.y += stepY
 
    def blitme(self):
        """Draw the ship at the center of the location"""
        self.screen.blit(self.image, self.rect)