import pygame
from pygame.locals import *

class ScoreBoard(pygame.sprite.Sprite):
    """Keeps track of the current game score"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loc = [400, 30]
        self.font = pygame.font.Font(None, 25)
        self.lscore = 0
        self.rscore = 0
        self.render()


    def render(self):
        """Updates the screen to reflect the current score"""
        #Cannot use helpers.py here, as we need a font, not an image
        #May rework helpers.py to load fonts as well
        self.image = self.font.render(str(self.lscore) + "     " + str(self.rscore), True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.loc


    def new_game(self):
        """Creates new game with score at zero"""
        self.lscore = 0
        self.rscore = 0
        self.render()


    def goal(self, player):
        """Adds a point to the scoring player's score"""
        if player == "left":
            self.lscore += 1
        elif player == "right":
            self.rscore += 1
        self.render()

    def update(self):
        """Had to add this due to sprite update loop; crashed game otherwise"""
        pass
