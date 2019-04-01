from Scene import Scene
from Database import Database
from Director import Director
import pygame
from Classes.Background import Background
from Classes.MovingRail import MovingRail
from Classes.TextLabel import TextLabel
from Classes.Vehicle import Vehicle
from Classes.Button import Button

class ShopScene(Scene):
    def __init__(self):
        self.db = Database()
        super().__init__()
        self.background = Background((0, 123, 228))
        self.button = Button(60, 200, 32, "Shop", (100, 100), color=(180, 190, 45))
        self.button_rect = self.button.get_rect()
        self.label = TextLabel("Points: {}".format(self.db['points']), "Resources/F77-Minecraft.ttf", 16, (50, 18))
        self.ten_km_up = Button(60, 350, 24, "+10km/h (50 pts)", (200, 370), color=(180, 190, 45))
        self.hundred_km_up = Button(60, 350, 24, "+100km/h (300 pts)", (200, 280), color=(180, 190, 45))
        self.five_hundred_km_up = Button(60, 350, 24, "+500km/h (1000 pts)", (200, 190), color=(180, 190, 45))
        self.double_click_points = Button(60, 350, 24, "2X pts. (200 pts)", (600, 370), color=(180, 190, 45))

    def render(self, screen: pygame.Surface):
        self.background.render(screen)
        self.button.render(screen)
        self.label.render(screen)
        self.ten_km_up.render(screen)
        self.hundred_km_up.render(screen)
        self.five_hundred_km_up.render(screen)
        self.double_click_points.render(screen)

    def update(self, delta_time: float):
        self.label.update_text("Points: {}".format(self.db['points']))

    def handle_event(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                Director().pop_scene()
            elif self.ten_km_up.get_rect().collidepoint(event.pos):
                if self.db['points'] >= 50:
                    self.db['speed'] += 10
                    self.db['points'] -= 50
            elif self.hundred_km_up.get_rect().collidepoint(event.pos):
                if self.db['points'] >= 300:
                    self.db['speed'] += 100
                    self.db['points'] -= 300
            elif self.five_hundred_km_up.get_rect().collidepoint(event.pos):
                if self.db['points'] >= 1000:
                    self.db['speed'] += 500
                    self.db['points'] -= 1000
            elif self.double_click_points.get_rect().collidepoint(event.pos):
                if self.db['points'] >= 200:
                    self.db['points_per_click'] *= 2
                    self.db['points'] -= 200
