from Scene import Scene
from Database import Database
# from Director import Director
import pygame

class MainScene(Scene):
    def __init__(self):
        super(MainScene, self).__init__()
        db = Database()
        width = round(db['screen_width'] * 4)
        # print(self.__rails.get_rect())
        rails_img = pygame.image.load("Resources/ClickerBg.png")
        scale_ratio = width / rails_img.get_rect()[2]
        height = round(rails_img.get_rect()[3] * scale_ratio)
        self.__bg_offset = float(0)
        self.__bg_color = (0, 123, 228)
        self.__rails = pygame.transform.scale(rails_img, (width, height))
        self.__rails_rect = self.__rails.get_rect()
        self.__rails_rect.centery = round(db['screen_height'] - height / 2)
        self.__font = pygame.font.Font("Resources/F77-Minecraft.ttf", 16)
        self.__points = 0
        self.__label = self.__font.render("Points: {}".format(self.__points), 1, (255, 255, 255))

        self.__train_img = pygame.image.load("Resources/locomotive.png")
        rect = self.__train_img.get_rect()
        self.__train_img = pygame.transform.scale(self.__train_img, (rect.width * 5, rect.height * 5))
        self.__train_rect = self.__train_img.get_rect()
        self.__train_rect.centerx = db['screen_width'] / 2
        self.__train_rect.centery = db['screen_height'] - 120



    def render(self, screen):
        screen.fill(self.__bg_color)
        screen.blit(self.__rails, self.__rails_rect)
        self.__label = self.__font.render("Points: {}".format(self.__points), 1, (255, 255, 255))
        screen.blit(self.__label, (10, 10))
        screen.blit(self.__train_img, self.__train_rect)
        # print('Rendering')

    def update(self, delta_time: float):
        if self.__rails_rect.centerx < 0:
            self.__rails_rect.centerx = Database()['screen_width'] / 2
            #if self.__bg_offset < -10000:
                #self.__bg_offset = 0
        #self.__bg_offset -= delta_time * 1000000
        self.__rails_rect.centerx -= delta_time * 2000000

