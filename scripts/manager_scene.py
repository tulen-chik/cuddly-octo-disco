import pygame as pg


class WindowManager:
    def __init__(self, *args):
        self.displays = args
        self.running = True
        self.clock = pg.time.Clock()
        self.current_scene = 0

    def is_running(self):
        return self.running

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        match self.displays[self.current_scene].update():
            case "start-game":
                self.current_scene += 1
                self.displays[self.current_scene - 1].change_state(None)
            case "menu-game":
                self.current_scene -= 1
                self.displays[self.current_scene + 1].change_state(None)
            case "close-game":
                self.running = False

        pg.display.update()
        self.clock.tick(60)
