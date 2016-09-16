import pygame
import spaceship
import bullet
import datetime
import random
from enemy_class import Enemy

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 1024)

screen = pygame.display.set_mode(size)
enemy_list = pygame.sprite.Group()

# Loop until the user clicks the close button.
done = False


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

ship = spaceship.SpaceShip()

shiprect = ship.getrect()
pygame.key.set_repeat(1, 40)
bullet_list = []
delay = 250000
last_shot = datetime.datetime.now()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for joy in joysticks:
    joy.init()


def spawn_enemy(default):
    for i in range(default):
        enemy = Enemy(WHITE, 20, 15)
        enemy.rect.x = random.randrange(1000,size[0])
        enemy.rect.y = random.randrange(50 , size[1] -50)
        enemy_list.add(enemy)


for joy in joysticks:
    if joy.get_init() == True:
        print("Initialized")
# -------- Main Program Loop ----------

while not done:

    level = 2
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.JOYAXISMOTION:
            if joy.get_axis(0) == -1:
                shiprect = ship.event_handler("left", shiprect)
            elif joy.get_axis(0) == 1:
                shiprect = ship.event_handler("right", shiprect)
            elif joy.get_axis(1) == 1:
                shiprect = ship.event_handler("down", shiprect)
            elif joy.get_axis(1) == -1:
                shiprect = ship.event_handler("up", shiprect)
            # if event.key == pygame.K_SPACE:
            #     delta_time = datetime.datetime.now() - last_shot
            #     if delta_time.microseconds > delay:
            #         last_shot = datetime.datetime.now()
            #         bullet_1 = bullet.Bullet(pygame.image.load("Green_laser.png"),  shiprect.midright[0], shiprect.midright[1])
            #         bulletrect = (bullet_1.x_coordinate, bullet_1.y_coordinate -5)
            #         bullet_list.append(bullet_1)
            # else:
                shiprect = ship.event_handler(event, shiprect)



    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    enemy_list.update()
    enemy_list.draw(screen)

    screen.blit(ship.image, shiprect)
    for bull in bullet_list:
        if bull.x_coordinate > 1260:
            bullet_list.remove(bull)
            continue
        bulletrect = (bull.x_coordinate, bull.y_coordinate-5)
        bull.bullet_mover()
        screen.blit(bull.image, bulletrect)

    for enemy in enemy_list:
        if enemy.rect.colliderect(shiprect):
            done = True

    for enemy in enemy_list:
        for bull in bullet_list:
            if enemy.rect.colliderect((bull.x_coordinate, bull.y_coordinate, 30, 10)):
                bullet_list.remove(bull)
                enemy_list.remove(enemy)
                continue

    if len(enemy_list) <= 5:
        spawn_enemy(level*5)
        level += 1



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()