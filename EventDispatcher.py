from Lib.Singleton import Singleton
from Event import Event
from Scene import Scene
import pygame


class EventDispatcher(metaclass=Singleton):
    def __init__(self):
        pass

    def dispatch(self, event: pygame.event, scene: Scene):
        scene.handle_event(event)
