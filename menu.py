import pygame
import main
import time
import name_input
#import print_highscore

class Option:
    hovered = False

    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos


pygame.init()
screen = pygame.display.set_mode((1280, 1024))
menu_font = pygame.font.Font("font/PressStart2P.ttf", 140)
string_font = pygame.font.Font(None, 10)
pygame.font.init()

new_game = Option("NEW GAME", (110, 155))
highscrore = Option("HIGHSCORE", (20, 380))
usual_font = pygame.font.Font("font/PressStart2P.ttf", 30)


label = usual_font.render("Press ESC if you want to QUIT !", 1, (255,255,0))

options = [new_game, highscrore]
new_game == True
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for joy in joysticks:
    joy.init()
joy1 = joysticks[0]

while True:
    pygame.event.pump()
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    screen.blit(label, (0, 10))

    for option in options:
        option.draw()

    for event in events:

        if event.type == pygame.JOYBUTTONDOWN:
            if joy1.get_button(10) == 1 or joy1.get_button(11) == 1:
                if new_game.hovered == True and highscrore.hovered == False:
                    new_game.hovered = False
                    highscrore.hovered = True
                    time.sleep(0.2)
                elif highscrore.hovered == True and new_game.hovered == False:
                    highscrore.hovered = False
                    new_game.hovered = True
                    time.sleep(0.2)
                elif new_game.hovered == False and highscrore.hovered == False:
                    new_game.hovered = True
                    time.sleep(0.2)
            elif joy1.get_button(0) == 1:
                if new_game.hovered == True:
                   name_input.name_input()
                if highscrore.hovered == True:
                    #print_highscore.print_highscore()
                    pass
            elif event.key == pygame.K_ESCAPE:
                    exit()

    pygame.display.update()