# Highlight-able menu in Pygame
#
# To run, use:
#     python pygame-menu-mouseover.py
#
# You should see a window with three grey menu options on it.  Place the mouse
# cursor over a menu option and it will become white.

import pygame


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
screen = pygame.display.set_mode((480, 320))
menu_font = pygame.font.Font(None, 40)
options = [Option("NEW GAME", (140, 105)), Option("LOAD GAME", (135, 155)),
           Option("OPTIONS", (145, 205))]
while True:
    pygame.event.pump()
    screen.fill((0, 0, 0))
    actual = 0
    events = pygame.event.get()

    for option in options:
        option.draw()

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                actual -= 1
                if actual != -1:
                    if actual == -1:
                        actual = 2
                        options[actual - 1].hovered = False
                        options[actual].hovered = True

            # if event.key == pygame.K_DOWN:
            #     actual += 1
            #     if actual != 3 or actual != -1:
            #         options[actual].hovered = True
            #         options[actual - 1].hovered = False
            #     else:
            #         actual = 0
            #         options[actual].hovered = True
    pygame.display.update()