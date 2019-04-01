from abc import ABC
from abc import abstractmethod
from Entity import Entity
from pygame import Surface
import pygame


# TODO:
class Scene(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(self, delta_time: float):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    def handle_event(self, event: pygame.event):
        pass
