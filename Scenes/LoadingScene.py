from Scene import Scene
import pygame


class LoadingScene(Scene):
    def __init__(self):
        pass
        # Paste initial scene here

    def render(self, screen: pygame.Surface):
        screen.fill((100, 100, 100))
        # print('rendering')

    def update(self, delta_time):
        pass
