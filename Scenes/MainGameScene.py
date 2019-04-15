from Scene import Scene
from Database import Database
from Director import Director
import pygame
from Classes.Background import Background
from Classes.MovingRail import MovingRail
from Classes.TextLabel import TextLabel
from Classes.Vehicle import Vehicle
from Classes.Button import Button
from Scenes.ShopScene import ShopScene
import os


class MainGameScene(Scene):
    def __init__(self):
        self.db = Database()
        self.db['points'] = 0
        self.db['points_per_click'] = 1
        self.db['speed'] = 10
        super(MainGameScene, self).__init__()
        self.background = Background((0, 123, 228))
        self.rails = MovingRail()
        self.label = TextLabel("Points: {}".format(self.db['points']), os.path.join("Resources", Database()['font']), 16, (50, 18))
        self.train = Vehicle()
        self.train_rect = self.train.get_rect()
        self.button = Button(60, 200, 32, "Shop", (100, 100))
        self.button_rect = self.button.get_rect()
        print(self.train_rect)

    def render(self, screen):
        self.background.render(screen)
        self.rails.render(screen)
        self.label.render(screen)
        self.train.render(screen)
        self.button.render(screen)

    def update(self, delta_time: float):
        self.rails.update(delta_time)
        self.label.update_text("Points: {}".format(self.db['points']))

    def handle_event(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.train_rect.collidepoint(event.pos):
                self.db['points'] += self.db['points_per_click']
            elif self.button_rect.collidepoint(event.pos):
                Director().set_scene(ShopScene())
