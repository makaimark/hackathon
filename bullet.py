import pygame

class Bullet:


    def __init__(self, image, x_coordinate, y_coordinate):
        self.image = pygame.transform.scale(image, (25, 10))
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def bullet_mover(self):
        self.x_coordinate += 50

    def getrect(self):
        return self.image.get_rect()