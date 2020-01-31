from helpers import *
from abc import ABC, abstractmethod


class AppView(ABC):
    points = []
    screen = pygame.display.set_mode((SIZE, SIZE))
    font = pygame.font.SysFont("comicsansms", 32)
    car = Car(screen, 'src/yellow.png')
    file_manager = FilesOperations()

    def __init__(self):
        self.clock = pygame.time.Clock()

    @abstractmethod
    def run(self):
        pass

    def draw_points(self):
        for point, radius in self.points:
            pygame.draw.circle(self.screen, COLOR_ACTIVE, point, 2, 1)
            pygame.draw.circle(self.screen, COLOR_INACTIVE, point, radius, 1)

    @abstractmethod
    def _navigate(self, event):
        pass
