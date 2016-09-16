import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

speed = [2, 2]
ball = pygame.image.load("spaceship.bmp")
ballrect = ball.get_rect()
pygame.key.set_repeat(1, 50)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                ballrect = ballrect.move([-5, 0])
            elif event.key == pygame.K_RIGHT:
                ballrect = ballrect.move([5, 0])
            elif event.key == pygame.K_UP:
                ballrect = ballrect.move([0, -5])
            elif event.key == pygame.K_DOWN:
                ballrect = ballrect.move([0, 5])



    '''ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > size[0]:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > size[1]:
        speed[1] = -speed[1]'''

    # --- Game Logic

    # Move the object according to the speed vector.
    '''
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    # --- Drawing Code

    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    draw_stick_figure(screen, x_coord, y_coord)
    '''
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    screen.blit(ball, ballrect)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()