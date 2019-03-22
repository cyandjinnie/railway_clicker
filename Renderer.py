from Director import Director
from Scene import Scene
import pygame

class Renderer:
    def __init__(self, width: int, height: int, name: str):
        self.__surface = pygame.display.set_mode((width, height))
        self.__surface.fill((0, 0, 0))
        pygame.display.set_caption(name)

    # TODO:
    def draw(self, scene: Scene):
        scene.render(self.__surface)
        pygame.display.flip()
        #scene.draw()
