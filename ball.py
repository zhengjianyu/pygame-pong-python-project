import pygame
from pygame.locals import *
import random, math
import helpers


class Ball(pygame.sprite.Sprite):
    """Ball class to initialize and move the ball across the screen."""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = helpers.load_image('pong_ball.png')
        self.speed = 5

        self.set_center()


    def set_center(self):
        """Sets the balls initial position in the center of the screen"""
        self.rect.centerx = 400
        self.rect.centery = 400
        self.vel = [0, 0]


    def start(self):
        """Starts the ball initially and whenever a goal is made"""
        self.angle = 0

        while abs(self.angle) < 5 or abs(self.angle-180) < 5:
            self.angle = random.randint(-45, 45)
        side = random.randint(0, 1)
        if side == 1:
            self.angle += 180

        xloc = math.cos(math.radians(self.angle))
        yloc = math.sin(math.radians(self.angle))

        self.vel[0] = self.speed * xloc
        self.vel[1] = self.speed * yloc


    def move(self, lpaddle, rpaddle, scoreboard):
        """Updates the ball and checks collision with walls and paddles"""
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]
        
        if self.rect.top < 0:
            self.vel[1] *= -1
        elif self.rect.bottom > 800:
            self.vel[1] *= -1

        if self.rect.left < 0:
            scoreboard.goal("right")
            self.set_center()

        elif self.rect.right > 800:
            scoreboard.goal("left")
            self.set_center()

        collision_list = pygame.sprite.spritecollide(self, [lpaddle, rpaddle], dokill = False)
        if len(collision_list) == 1:
            self.vel[0] *= -1
