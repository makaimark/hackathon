import pygame
import spaceship
import bullet
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 1024)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

ship = spaceship.SpaceShip()

shiprect = ship.getrect()
pygame.key.set_repeat(1, 40)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_1 = bullet.Bullet(shiprect.right, (shiprect.top + shiprect.bottom)/2)
                bulletrect = bullet_1.getrect()
                bullet_1.bullet_mover()
            else:
                shiprect = ship.event_handler(event, shiprect)


    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    screen.blit(ship.image, shiprect)
    screen.blit(bullet_1.image, bulletrect)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()