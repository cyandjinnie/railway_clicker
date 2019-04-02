from Scene import Scene
import pygame


class LoadingScene(Scene):
    def __init__(self):
        pass

    def render(self, screen: pygame.Surface):
        screen.fill((100, 100, 100))

    def update(self, delta_time):
        pass
