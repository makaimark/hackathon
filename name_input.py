import pygame
import time
from pygame import K_UP, K_DOWN, K_SPACE, K_a
import main

# Define some colors
WHITE = (255, 255, 255)

def name_input():
    pygame.init()

    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    for joy in joysticks:
        joy.init()
    joy1 = joysticks[0]
    # Set the width and height of the screen [width, height]
    size = (1280, 1024)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")
    screen.fill(WHITE)

    done = False
    n = 0
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "Z"]
    usual_font = pygame.font.Font("font/PressStart2P.ttf", 100)
    usual_font_2 = pygame.font.Font("font/PressStart2P.ttf", 30)

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
            elif event.type == pygame.JOYBUTTONDOWN:
                if joy1.get_button(10) == 1:
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
                elif joy1.get_button(11) == 1:
                    if n != -1:
                        n -= 1
                        screen.fill(WHITE)
                        label = usual_font.render("User : {}".format(list[n]), 1, (0, 0, 0))
                        screen.blit(label, (100, 100))
                    else:
                        n = 19
                        screen.fill(WHITE)
                        label = usual_font.render("User : {}".format(list[n]), 1, (0, 0, 0))
                        screen.blit(label, (100, 100))
                elif joy1.get_button(0) == 1:
                    username.append(list[n])
                    label = usual_font_2.render("User : {}".format(username), 1, (0, 0, 0))
                    screen.blit(label, (250, 250))
                elif joy1.get_button(1) == 1:
                    data = " ".join(i for i in username)
                    main(data)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()