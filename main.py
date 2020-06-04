from Application import Application
from Database import Database
import Director
from pygame import *

def main():
    db = Database()
    db['screen_width'] = 800
    db['screen_height'] = 450
    db['locomotive_img'] = "locomotive.png"
    db['rails_img'] = "ClickerBg.png"
    db['font'] = "F77-Minecraft.ttf"
    app = Application("MyApp")
    app.create_window(db['screen_width'], db['screen_height'], "ClickerGame")
    return app.run()


if __name__ == "__main__":
    main()
