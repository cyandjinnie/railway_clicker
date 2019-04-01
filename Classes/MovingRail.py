from Entity import Entity
from Database import Database
import pygame


class MovingRail(Entity):
    def __init__(self):
        super().__init__()
        db = Database()
        self.rail_img = rails_img = pygame.image.load("Resources/ClickerBg.png")
        width, height = self.get_scaling_vector()
        self.rail_img = pygame.transform.scale(self.rail_img, (width, height))
        self.rect = self.rail_img.get_rect()
        self.rect.centery = round(db['screen_height'] - height / 2)

    def get_scaling_vector(self):
        db = Database()
        width = round(db['screen_width'] * 4)
        scale_ratio = width / self.rail_img.get_rect()[2]
        height = round(self.rail_img.get_rect()[3] * scale_ratio)
        return width, height

    def render(self, surface: pygame.Surface):
        surface.blit(self.rail_img, self.rect)

    def update(self, delta_time):
        if self.rect.centerx < 0:
            self.rect.centerx = Database()['screen_width'] / 2
        self.rect.centerx -= delta_time * 50000 * Database()['speed']
