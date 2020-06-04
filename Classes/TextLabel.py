import pygame
from Entity import Entity


class TextLabel(Entity):
    def __init__(self, text, font_path, font_size, coordinate):
        super().__init__()
        self.font = pygame.font.Font(font_path, font_size)
        self.label = self.font.render(text, 1, (255, 255, 255))
        self.rect = self.label.get_rect()
        self.rect.center = coordinate

    def update(self, delta_time):
        pass

    def set_center(self, center):
        self.rect.center = center

    def update_text(self, text):
        self.label = self.font.render(text, 1, (255, 255, 255))

    def render(self, surface: pygame.Surface):
        surface.blit(self.label, self.rect)
