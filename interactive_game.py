import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

while True:
    for event in pygame.event.get():
        # User pressed down on a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

 # User let up on a key
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or 	event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or 	event.key == pygame.K_DOWN:
                y_speed = 0

    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    #Draw a white background
    screen.fill(WHITE)
 
    #Draw our character
    draw_stick_figure(screen, x_coord, y_coord)

    #Update the screen with what we've drawn.
    pygame.display.flip()
 
    #Limit frames per second
    clock.tick(60) 