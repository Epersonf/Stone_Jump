from Game.button import *
from Game.PPlay.gameimage import *


class Gameover:

    gui = None
    level = None
    game = None
    yes = None
    no = None
    keyboard = None
    mouse = None
    bg = None
    try_again = None

    def __init__(self, gui, level, game):
        self.gui = gui
        self.level = level
        self.game = game
        self.yes = Btn("Assets/Btns/yesButton.png", "Assets/Btns/yesBlur.png", gui, gui.width / 2 - 170, gui.height / 2 + 200)
        self.no = Btn("Assets/Btns/noButton.png", "Assets/Btns/noBlur.png", gui, gui.width / 2 + 170, gui.height / 2 + 200)
        self.mouse = gui.get_mouse()
        self.keyboard = gui.get_keyboard()
        self.bg = GameImage("Assets/menuBackground.png")
        self.bg.set_position(0, 0)
        self.try_again = GameImage("Assets/Try_Again.png")
        self.try_again.set_position(gui.width/2 - self.try_again.width/2, gui.height/2 - 100)



    def draw(self):
        self.bg.draw()
        self.try_again.draw()
        self.yes.draw()
        self.no.draw()
        if self.yes.mouse_over() and self.mouse.is_button_pressed(1):
            self.game.reset(self.gui, self.level)
            self.level[0] = 1
        if self.no.mouse_over() and self.mouse.is_button_pressed(1):
            self.level[0] = 0
