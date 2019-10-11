from Game.button import *

class Gameover:

    gui = None
    level = None
    game = None
    replay = None
    keyboard = None
    mouse = None

    def __init__(self, gui, level, game):
        self.gui = gui
        self.level = level
        self.game = game
        self.replay = Btn("Assets/BTN.png", "Replay", gui, gui.width/2, gui.height/2)
        self.replay.set_location(self.replay.obj.x - self.replay.obj.width//2, self.replay.obj.y - self.replay.obj.height//2)
        self.mouse = gui.get_mouse()
        self.keyboard = gui.get_keyboard()



    def draw(self):
        self.replay.draw()
        if self.replay.mouse_over() and self.mouse.is_button_pressed(1):
            self.game.reset(self.gui, self.level)
            self.level[0] = 1
