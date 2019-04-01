from Renderer import Renderer
from Director import Director
from time import time
from Scenes.MainGameScene import MainGameScene
import pygame


class Application:
    def __init__(self, name: str):
        pygame.init()
        self.__title = name
        self.__gameover = False

    def create_window(self, width: int, height: int, name="default"):
        self.__renderer = Renderer(width, height, name)

    def exit(self):
        self.__gameover = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            else:
                Director().get_current_scene().handle_event(event)

    def run(self):
        director = Director()
        Director().set_scene(MainGameScene())
        previous_time = time()
        deltaT = time()
        while not self.__gameover:
            deltaT = (time() - previous_time)
            scene = director.get_current_scene()
            scene.update(deltaT)
            self.handle_events()
            self.__renderer.draw(scene)
            previous_time = time()
        return 0
