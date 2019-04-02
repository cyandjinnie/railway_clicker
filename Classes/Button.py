import pygame
from Entity import Entity
from Classes.TextLabel import TextLabel
from Database import Database
import os

class Button(Entity):
    def __init__(self, width, height, font_size, text, center, color=(100, 100, 100)):
        self.label = TextLabel(text, os.path.join("Resources", Database()['font']), font_size, center)
        self.rect = pygame.Rect(0, 0, height, width)
        self.rect.center = center
        self.color = color

    def render(self, surface: pygame.Surface):
        rect = pygame.draw.rect(surface, self.color, self.rect)
        # surface.blit(rect)
        self.label.render(surface)
        # surface.blit(rect)

    def get_rect(self):
        return self.rect

    def update(self, delta_time):
        pass
