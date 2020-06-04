from abc import ABC
from abc import abstractmethod

import sys
sys.path.append("/usr/local/lib/python3.7/site-packages")

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
