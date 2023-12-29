import pygame as pg
from scripts.button import Button
from scripts.bass_scene import Scene
from interface.Imain import IMainGame


class MainGame(Scene, IMainGame):
    def __init__(self, display, scenes):
        super().__init__(display)
        self.scenes = scenes
        self.current_scene = 0
        self.que = 0
        self.font = pg.font.SysFont("arial", 36)

        self.__update_scene()
        self.menu_but = Button("меню", self.display, lambda: self.change_state("menu-game"))

    def change_state(self, protocol):
        self.state = protocol

    def __update_scene(self):
        class StringShow:
            def __init__(self, string):
                self.string = string
                self.font = pg.font.SysFont("arial", 36)

            def blit(self, display, cords):
                cords = list(cords)
                for i in range(len(self.string) % 60):
                    self.__dict__['font_surface'] = self.font.render(self.string[i * 60: (i * 60) + 60],
                                                                     False, (64, 64, 64))
                    display.blit(self.__dict__['font_surface'], (cords[0], cords[1] + (40 * i)))

        self.text_scene = StringShow(self.scenes[self.current_scene].get("text")[self.que])
        self.frame_surface = pg.image.load("assets/sys/frame.png").convert_alpha()
        self.background_surface = pg.image.load(self.scenes[self.current_scene].get("bg")).convert_alpha()
        self.character_surface = pg.image.load(self.scenes[self.current_scene].get("char")).convert_alpha()

    def update(self):
        click = pg.mouse.get_pressed()

        if click[0] == 1:
            if self.que == len(self.scenes[self.current_scene].get("text")) - 1:
                if self.current_scene != len(self.scenes) - 1:
                    self.current_scene += 1
                    self.que = 0
                else:
                    self.current_scene = 0
                    self.que = 0
            else:
                self.que += 1

            self.__update_scene()
            pg.time.delay(200)

        self.display.blit(self.background_surface, (0, 0))
        self.display.blit(self.character_surface, (0, 0))
        self.display.blit(self.frame_surface, (20, 700))
        self.text_scene.blit(self.display, (80, 750))
        self.menu_but.update(10, 10)

        return self.state
