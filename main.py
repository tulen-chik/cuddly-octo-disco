import pygame as pg
from scripts.main_scene import MainGame
from scripts.menu_scene import MainMenu
from scripts.manager_scene import WindowManager

if __name__ == "__main__":
    scene_first = [
        {"bg": "assets/kbp.jfif", "char": "assets/amogus.png", "text": ["йоу", "мы наконец-то поступили в лучший колледж вселенной ", "ты этому рад?"]},
        {"bg": "assets/kbp.jfif", "char": "assets/amogus_green.png", "text": ["ну не знаю", "лучше пошли покурим" ]},
    ]

    pg.init()
    screen = pg.display.set_mode((1000, 1000))
    pg.display.set_caption("KBP")

    main_game = MainGame(screen, scene_first)
    main_menu = MainMenu(screen)
    window = WindowManager(main_menu, main_game)

    while window.running:
        window.update()
