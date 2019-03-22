from abc import ABC
from abc import abstractmethod

import pygame

# TODO:
class Scene(ABC):
    def __init__(self):
        self.__scene_graph = []

    @abstractmethod
    def update(self, delta_time: float):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    def handle_event(self, event: pygame.event):
        pass
