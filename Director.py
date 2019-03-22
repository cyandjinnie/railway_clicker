from Singleton import Singleton
from Scenes.LoadingScene import LoadingScene
from Scene import Scene
import pygame

class Director(metaclass=Singleton):
    def __init__(self):
        self.__scene_stack = [LoadingScene()]
        self.__scene_counter = 1

    def set_scene(self, scene: Scene):
        self.__scene_counter += 1
        self.__scene_stack.append(scene)
        #print("ADDED SCENE (STACK DEPTH {})".format(self.__scene_counter))

    def pop_scene(self):
        if self.__scene_counter > 1:
            self.__scene_stack.pop()

    def get_current_scene(self) -> Scene:
        return self.__scene_stack[len(self.__scene_stack) - 1]

    def delegate_events_to_current_scene(self, event: pygame.event):
        scene = self.get_current_scene()
        scene.handle_event(event)
