import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# This sets the name of the window
pygame.display.set_caption('SPACE!!!!!!!!!!!!!')

clock = pygame.time.Clock()

pygame.display

# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
background_image = pygame.image.load("planets.jpg").convert()
player_image = pygame.image.load("spaceship.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
  # Copy image to screen:
    screen.blit(background_image, background_position)
    
    # Get the current mouse position. 
    # as a list of two numbers.
    playerPos = pygame.mouse.get_pos()
    
    # Copy image to screen:
    screen.blit(player_image, [playerPos[0], playerPos[1]])
    #Update the screen with what we've drawn.
    pygame.display.flip()
    
    #Limit frames per second
    clock.tick(60)
