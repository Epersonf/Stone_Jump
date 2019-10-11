from Game.button import *
from Game.PPlay.gameimage import *

class Main_menu:

    play = None
    gui = None
    level = None
    keyboard = None
    mouse = None
    game = None
    bg = None

    def __init__(self, gui, level, game):
        self.gui = gui
        self.level = level
        self.game = game
        self.play = Btn("Assets/Btns/playButton.png", "Assets/Btns/playBlur.png", gui, gui.width/2, gui.height/2)
        self.exit = Btn("Assets/Btns/exitButton.png", "Assets/Btns/exitBlur.png", gui, gui.width/2, gui.height/2 + 200)
        self.mouse = self.gui.get_mouse()
        self.keyboard = self.gui.get_keyboard()
        self.bg = GameImage("Assets/menuBackground.png")
        self.bg.set_position(0, 0)


    def draw(self):
        self.bg.draw()
        self.play.draw()
        self.exit.draw()
        if self.play.mouse_over() and self.mouse.is_button_pressed(1):
            self.game.reset(self.gui, self.level)
            self.level[0] = 1
        if self.exit.mouse_over() and self.mouse.is_button_pressed(1):
            exit(0)

