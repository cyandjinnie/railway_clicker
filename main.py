from Application import Application
from Database import Database
import Director
from pygame import *

def main():
    db = Database()
    db['screen_width'] = 800
    db['screen_height'] = 450
    app = Application("MyApp")
    app.create_window(db['screen_width'], db['screen_height'], "ClickerGame")
    return app.run()


if __name__ == "__main__":
    main()
