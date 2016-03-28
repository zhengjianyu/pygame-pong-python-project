import pygame
from pygame.locals import *
import helpers


class Paddle(pygame.sprite.Sprite):
    """Initializes and handles moving of the paddles."""

    def __init__(self, xloc):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = helpers.load_image('pong_paddle.png')
        self.rect.centerx = xloc
        self.rect.centery = 400
        self.speed = 5
        self.yvel = 0


    def move_up(self):
        """Moves the paddle vertically up"""
        self.yvel -= self.speed


    def move_down(self):
        """Moves the paddle vertically down"""
        self.yvel += self.speed


    def update(self):
        """Moves the paddle's rectangle location"""
        if self.rect.bottom + self.yvel > 800:
            self.rect.bottom = 800
        elif self.rect.top + self.yvel < 0:
            self.rect.top = 0
        else:
            self.rect.y += self.yvel
