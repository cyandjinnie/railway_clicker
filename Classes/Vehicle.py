import pygame
from Database import Database
from Entity import Entity


class Vehicle(Entity):
    def __init__(self):
        super().__init__()
        db = Database()
        self.train_image = pygame.image.load("Resources/locomotive.png")
        rect = self.train_image.get_rect()
        self.train_image = pygame.transform.scale(self.train_image, (rect.width * 5, rect.height * 5))
        self.rect = self.train_image.get_rect()
        self.rect.centerx = db['screen_width'] / 2
        self.rect.centery = db['screen_height'] - 120

    def update(self, delta_time):
        pass

    def render(self, surface: pygame.Surface):
        surface.blit(self.train_image, self.rect)

    def get_rect(self):
        return self.rect
