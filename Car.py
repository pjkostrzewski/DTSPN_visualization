import pygame
from math import pi


class Car(object):
    def __init__(self, screen, filepath):
        self.screen = screen
        self.car_img = pygame.transform.scale(pygame.image.load(filepath).convert_alpha(), (34, 22))
        self.rotation = 180
        self._x = 400
        self._y = 400

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        assert value >= 0, f"{value} should be bigger or equal 0"
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        assert value >= 0, f"{value} should be bigger or equal 0"
        self._y = value

    def display(self):
        car = pygame.transform.rotate(self.car_img, self.rotation)
        self.screen.blit(car, (self.x-15, self.y-15))

    def set_rotation(self, rotate):
        self.rotation = rotate

    def set_position(self, x, y):
        self.x, self.y = x, y

    def get_degrees(self):
        return self.rotation
    
    def get_radians(self):
        return self.rotation * pi / 180

    def rotate(self, degrees):
        self.rotation -= degrees
