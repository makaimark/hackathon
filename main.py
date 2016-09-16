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
bullet_list = []

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

ship = spaceship.SpaceShip()

shiprect = ship.getrect()
pygame.key.set_repeat(1, 40)
bullet_1 = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_1 = bullet.Bullet(pygame.image.load("Green_laser.png"),  shiprect.midright[0], shiprect.midright[1])
                bulletrect = (bullet_1.x_coordinate, bullet_1.y_coordinate -5)
                bullet_list.append(bullet_1)
            else:
                shiprect = ship.event_handler(event, shiprect)


    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    screen.blit(ship.image, shiprect)
    for bull in bullet_list:
        if bull.x_coordinate > 1260:
            bullet_list.remove(bull)
        bulletrect = (bull.x_coordinate, bull.y_coordinate - 5)
        bull.bullet_mover()
        screen.blit(bull.image, bulletrect)



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()