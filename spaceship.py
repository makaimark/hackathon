import pygame


class SpaceShip:
    life = 3
    image = pygame.image.load("spaceship.jpg")

    def event_handler(self, event, shiprect):
        if event.key == pygame.K_LEFT:
            return shiprect.move([-5, 0])
        elif event.key == pygame.K_RIGHT:
            return shiprect.move([5, 0])
        elif event.key == pygame.K_UP:
            return shiprect.move([0, -5])
        elif event.key == pygame.K_DOWN:
            return shiprect.move([0, 5])

    def getrect(self):
        return self.image.get_rect()