import pygame
import time
from pygame import K_UP, K_DOWN, K_SPACE, K_a

# Define some colors
WHITE = (255, 255, 255)


pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for joy in joysticks:
    joy.init()
joy1 = joysticks[0]
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
screen.fill(WHITE)

done = False
n = 0
list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "Z"]
usual_font = pygame.font.Font("font/PressStart2P.ttf", 50)
usual_font_2 = pygame.font.Font("font/PressStart2P.ttf", 10)

label = usual_font.render("User : {}".format(list[0]), 1, (0, 0, 0))
screen.blit(label, (100, 100))
username = []
clock = pygame.time.Clock()
pygame.font.init()

# -------- Main Program Loop -----------
while not done:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.JOYAXISMOTION:
            if joy1.get_axis(1) < 0:
                time.timeout(1)
                if n != 19:
                    n += 1
                    screen.fill(WHITE)
                    label = usual_font.render("User : {}".format(list[n]), 1, (0, 0, 0))
                    screen.blit(label, (100, 100))
                else:
                    n = 0
                    screen.fill(WHITE)
                    label = usual_font.render("User : {}".format(list[n]), 1, (0, 0, 0))
                    screen.blit(label, (100, 100))
            elif joy1.get_axis(1) > 0:
                time.timeout(1)
                if n != -1:
                    n -= 1
                    screen.fill(WHITE)
                    label = usual_font.render("User : {}".format(list[n]), 1, (0, 0, 0))
                    screen.blit(label, (100, 100))
                else:
                    n =19
                    screen.fill(WHITE)
                    label = usual_font.render("User : {}".format(list[n]), 1, (0, 0, 0))
                    screen.blit(label, (100, 100))
            elif keys[K_SPACE]:
                username.append(list[n])
            elif keys[K_a]:
                print("itt vagyok")
                data = " ".join(i for i in username)
                label = usual_font_2.render("User : {}".format(data), 1, (0, 0, 0))
                screen.blit(label, (150, 150))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()