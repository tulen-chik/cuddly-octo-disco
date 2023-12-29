import pygame as pg


class Button:
    def __init__(self, text, display, function, menu_but=True):
        self.display = display
        self.text = text
        self.function = function
        self.active_color = (255, 99, 71)
        self.inactive_color = (255, 127, 80)
        self.menu_but = menu_but

    def update(self, x, y):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        font = pg.font.SysFont("arial", 36)
        font_surface = font.render(self.text, False, (64, 64, 64))

        if self.menu_but:
            button_surface = pg.image.load("assets/sys/menu_but.png").convert_alpha()
            if x < mouse[0] < x + 200 and y < mouse[1] < y + 66:
                button_surface = pg.image.load("assets/sys/menu_but_active.png").convert_alpha()
                if click[0] == 1:
                    self.function()
                    pg.time.delay(200)

            self.display.blit(button_surface, (x, y))
            self.display.blit(font_surface, (x + 60, y + 10))
        else:
            button_surface = pg.image.load("assets/sys/menu_menu_but.png").convert_alpha()
            if x < mouse[0] < x + 200 and y < mouse[1] < y + 66:
                button_surface = pg.image.load("assets/sys/menu_menu_but_active.png").convert_alpha()
                if click[0] == 1:
                    self.function()
                    pg.time.delay(200)

            self.display.blit(button_surface, (x, y))
            self.display.blit(font_surface, (x + 60, y + 10))
