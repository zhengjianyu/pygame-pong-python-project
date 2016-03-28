import os, sys
import pygame
from pygame.locals import *

from ball import *
from paddle import *
from scoreboard import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')


class PongMain:
    """Initializes the game and creates the window to play in."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pong | space to start")
        pygame.event.set_allowed([KEYUP, KEYDOWN, QUIT])
        
        self.background = pygame.Surface((800,800))
        self.background.fill((0, 0, 0))
        self.screen.blit(self.background, (0,0))
        pygame.display.flip()
        
        self.sprites = pygame.sprite.RenderUpdates()
        self.LoadObjects()
        


    def MainLoop(self):
        """Main loop for the game to keep it running."""
        game = True
        
        while game:
            self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game = False
                    if event.key == K_SPACE:
                        if self.ball.vel[0] == 0 or self.ball.vel[1] == 0:
                            self.ball.start()
                        
                    if event.key == K_w:
                        self.lpaddle.move_up()
                    if event.key == K_s:
                        self.lpaddle.move_down()
                    if event.key == K_UP:
                        self.rpaddle.move_up()
                    if event.key == K_DOWN:
                        self.rpaddle.move_down()

                #Calling the opposite function stops the paddle from moving
                elif event.type == KEYUP:
                    if event.key == K_w:
                        self.lpaddle.move_down()
                    if event.key == K_s:
                        self.lpaddle.move_up()
                    if event.key == K_UP:
                        self.rpaddle.move_down()
                    if event.key == K_DOWN:
                        self.rpaddle.move_up()

            #Re-render all of the sprites
            for item in self.sprites:
                item.update()
            self.render()
            self.ball.move(self.lpaddle, self.rpaddle, self.scoreboard)


    def LoadObjects(self):
        """Loads the ball, paddles, and edges of the screen."""
        self.lpaddle = Paddle(30)
        self.sprites.add(self.lpaddle)
        self.rpaddle = Paddle(770)
        self.sprites.add(self.rpaddle)
        self.ball = Ball()
        self.sprites.add(self.ball)
        self.scoreboard = ScoreBoard()
        self.sprites.add(self.scoreboard)


    def render(self):
        """Re-renders all of the sprites on screen"""
        self.sprites.clear(self.screen, self.background)
        redraw_list = self.sprites.draw(self.screen)
        pygame.display.update(redraw_list)


if __name__ == "__main__":
    MainWindow = PongMain()
    MainWindow.MainLoop()
