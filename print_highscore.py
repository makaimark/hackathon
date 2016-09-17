from high_score import Highscore
import time
from menu import menu
import pygame


def print_highscore():
    stuff = Highscore.print_score_out("highscore/highscore.csv")

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    pygame.init()
    size = (1280, 1024)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("HIGH SCORE")
    done = False
    clock = pygame.time.Clock()
    usual_font = pygame.font.Font("font/PressStart2P.ttf", 20)
    score_font = pygame.font.Font("font/PressStart2P.ttf", 40)
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)
        score = score_font.render("HIGH SCORES", 1, (0,0,0))
        label_1 = usual_font.render(stuff[-1], 1, (0, 0, 0))
        label_2 = usual_font.render(stuff[-2], 1, (0, 0, 0))
        label_3 = usual_font.render(stuff[-3], 1, (0, 0, 0))
        screen.blit(score, (200, 100))
        screen.blit(label_1, (200, 300))
        screen.blit(label_2, (200, 400))
        screen.blit(label_3, (200, 200))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
