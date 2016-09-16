import pygame


class SpaceShip:
    life = 3
    image = pygame.image.load("spaceship.bmp")

    def event_handler(self, event, shiprect):
        if event == "left":
            if shiprect.left > 0:
                return shiprect.move([-4, 0])
            return shiprect
        elif event == "right":
            if shiprect.right < 1260:
                return shiprect.move([4, 0])
            return shiprect
        elif event == "up":
            if shiprect.top > 0:
                return shiprect.move([0, -4])
            return shiprect
        elif event == "down":
            if shiprect.bottom < 950:
                return shiprect.move([0, 4])
            return shiprect

    def getrect(self):
        return self.image.get_rect()