import pygame
from utils.constants import *

# important to initialize pygame before using any of its features
pygame.init()

# create a display surface object which is the window the players will see
# set_mode() is a function that creates a display surface object
# set_mode() should receive at least one argument which is a tuple of width and height
screen = pygame.display.set_mode((800, 400))
# set the title of the window
pygame.display.set_caption(TITLE)
# create a clock object to control the frame rate
clock = pygame.time.Clock()
# creating a font object
test_font = pygame.font.Font(FONT_TYPE, 50)

# creating a sky image surface object
# it's a good idea for performance to convert images to a format that is easier for pygame to work with
sky_surface = pygame.image.load(SKY).convert()
ground_surface = pygame.image.load(GROUND).convert()
# creating a text surface object
# the render method takes 3 arguments:
# 1. the text to be rendered
# 2. a boolean value that enables or disables anti-aliasing (smoothing of the text edges)
# 3. a color
text_surface = test_font.render("Hello World!", False, 'Black')
# creating an image that will be animated
snail_surface = pygame.image.load(SNAIL).convert_alpha()
snail_x_pos = SNAIL_INITIAL_X_POS
# creating a player surface with its rect object
player_surface = pygame.image.load(PLAYER).convert_alpha()
# get_rect() is a method that takes the surface of the object and draws a rectangle around it
# and in order to position the rectangle we can use any of the available points
player_rect = player_surface.get_rect(midbottom=(80, GROUND_X_POS))

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
    
    # now we want to display our surface on the screen
    # blit stands for block image transfer and it's just a fancy way to say we want to put one surface on top of another
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, GROUND_X_POS))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= SNAIL_MOVE_SPEED
    if snail_x_pos <= -100: snail_x_pos = SNAIL_INITIAL_X_POS
    screen.blit(snail_surface, (snail_x_pos, 250))
    # since we have a rectangle for the player_surface we can use that to position it on the screen
    screen.blit(player_surface, player_rect)

    # we update the display at the end of the loop so that any changes made are reflected on the screen
    pygame.display.update()
    # we need to control the frame rate of the game
    # we do this by calling the tick() method of the clock object
    # we pass the FPS constant as an argument to the tick() method
    clock.tick(FPS)
