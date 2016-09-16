import pygame

class Bullet:

    image = pygame.image.load("Green_laser.png")


    def __init__(self, x_coordinate, y_coordinate):
        self.image = pygame.transform.scale(self.image, (30, 10))
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate



    def bullet_mover(self):
        self.x_coordinate += 50

    def getrect(self):
        return self.image.get_rect()