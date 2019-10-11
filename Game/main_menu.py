from Game.button import *

class Main_menu:

    play = None
    gui = None
    level = None
    keyboard = None
    mouse = None
    game = None

    def __init__(self, gui, level, game):
        self.gui = gui
        self.level = level
        self.game = game
        self.play = Btn("Assets/BTN.PNG", "Play", gui, gui.width/2, gui.height/2)
        self.play.set_location(self.play.obj.x - self.play.obj.width/2, self.play.obj.y - self.play.obj.height/2)
        self.mouse = self.gui.get_mouse()
        self.keyboard = self.gui.get_keyboard()

    def draw(self):
        self.play.draw()
        if self.play.mouse_over() and self.mouse.is_button_pressed(1):
            self.game.reset(self.gui, self.level)
            self.level[0] = 1

