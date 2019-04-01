from Entity import Entity
from pygame import Surface


class Background(Entity):
    def __init__(self, color):
        super().__init__()
        self.__bg_color = color

    def render(self, screen: Surface):
        screen.fill(self.__bg_color)

    def update(self, delta_time):
        pass
