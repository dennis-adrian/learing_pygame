import pygame
from utils.constants import *

# important to initialize pygame before using any of its features
pygame.init()

# create a display surface object which is the window the players will see
# set_mode() is a function that creates a display surface object
# set_mode() should receive at least one argument which is a tuple of width and height
screen = pygame.display.set_mode((800, 600))
# set the title of the window
pygame.display.set_caption(TITLE)
# create a clock object to control the frame rate
clock = pygame.time.Clock()

while True:
    # inside this loop we're going to draw all our elements
    # and update everything

    # look for any player input which are called events
    for event in pygame.event.get():
        # if the player clicks on the close button of the window
        if event.type == pygame.QUIT:
            pygame.quit()
            # we now need to break the loop so that the game stops running and doesn't throw an error
            # the best way to do this is to use the exit method from the sys module
            # generally we will import it (from sys import exit)
            # but since we're not going to use it anywhere else we can just call it directly
            exit()


    # we update the display at the end of the loop so that any changes made are reflected on the screen
    pygame.display.update()
    # we need to control the frame rate of the game
    # we do this by calling the tick() method of the clock object
    # we pass the FPS constant as an argument to the tick() method
    clock.tick(FPS)
