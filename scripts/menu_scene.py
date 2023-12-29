import pygame as pg
from scripts.button import Button
from scripts.bass_scene import Scene
from interface.Imenu import IMainMenu


class MainMenu(Scene, IMainMenu):
    def __init__(self, display):
        super().__init__(display)
        self.menu_but = Button("играть", self.display, lambda: self.change_state("start-game"), menu_but=False)
        self.menu_but_close = Button("выйти из игры", self.display, lambda: self.change_state("close-game"),
                                     menu_but=False)
        self.background_surface = pg.image.load("assets/sys/Menu_background.png").convert_alpha()

    def change_state(self, protocol):
        self.state = protocol

    def update(self):
        self.display.blit(self.background_surface, (0, 0))
        self.menu_but.update(200, 200)
        self.menu_but_close.update(200, 400)

        return self.state
