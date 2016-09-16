import pygame

class Bullet:

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


    def bullet_mover(self):
        self.x_coordinate += 50