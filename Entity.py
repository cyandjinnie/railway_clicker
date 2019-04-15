from abc import ABC
from abc import abstractmethod
from sortedcontainers import SortedDict
from pygame import Surface


class Entity(ABC):
    def __init__(self):
        self.__children = SortedDict()

    def add_child(self, entity, z_index: int):
        self.__children[Entity] = z_index

    @abstractmethod
    def render(self, surface: Surface):
        pass

    @abstractmethod
    def update(self, delta_time):
        pass
