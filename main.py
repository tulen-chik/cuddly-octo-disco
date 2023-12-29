import pygame as pg
from scripts.main_scene import MainGame
from scripts.menu_scene import MainMenu
from scripts.manager_scene import WindowManager

if __name__ == "__main__":
    scene_first = [
        {"bg": "assets/kbp.jfif", "char": "assets/amogus.png", "text": ["1", "2", "3"]},
        {"bg": "assets/kbp.jfif", "char": "assets/amogus_green.png", "text": ["4", "5", "6"]},
    ]

    pg.init()
    screen = pg.display.set_mode((1000, 1000))
    pg.display.set_caption("KBP")

    main_game = MainGame(screen, scene_first)
    main_menu = MainMenu(screen)
    window = WindowManager(main_menu, main_game)

    while window.running:
        window.update()
