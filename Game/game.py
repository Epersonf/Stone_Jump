from Game.char import *
from Game.ground import *
from Game.trace import *
from Game.stone_wall import *


class Game_itself:

    char = None
    trace = None
    keyboard = None
    mouse = None
    gui = None
    GROUNDS = None
    score = None
    stone_wall = None

    def reset(self, gui, level):
        if self.GROUNDS != None:
            self.GROUNDS.clear()
        self.score = 0
        self.gui = gui
        self.char = Char("Assets/Char.png", level, gui)
        self.char.obj.set_position(1024 / 2 - self.char.obj.width / 2, 768 / 2 - self.char.obj.height / 2)
        self.trace = Trace("Assets/Trace.png", self.char)

        self.keyboard = gui.get_keyboard()
        self.mouse = gui.get_mouse()
        grounds_initial_qt = 8
        self.GROUNDS = [None] * grounds_initial_qt
        for i in range(grounds_initial_qt):
            self.GROUNDS[i] = Ground("Assets/Ground_1.png", self.char, self.mouse, self.GROUNDS, "Assets/Arrow.png",
                                     gui)
            if i == 0:
                self.GROUNDS[i].obj.set_position(1024 / 2 - self.GROUNDS[i].obj.width / 2, 768 / 2 + 200)
            elif i == 1:
                self.GROUNDS[i].obj.set_position(1024 / 2 - 400, 768 / 2 + 100)
            elif i == 2:
                self.GROUNDS[i].obj.set_position(1024 / 2 + 250, 768 / 2 + 100)
            elif i == 3:
                self.GROUNDS[i].obj.set_position(1024 / 2 + 350, 300)
            elif i == 4:
                self.GROUNDS[i].obj.set_position(1024 / 2 - 500, 300)

        self.stone_wall = Stone_wall(self.gui)

    def __init__(self, gui, level):
        self.reset(gui, level)

    def draw(self):
        self.gui.set_background_color((150, 150, 240))
        self.stone_wall.draw()
        for g in self.GROUNDS:
            g.draw_ground()

        self.score += 1
        # char edit
        self.trace.draw_trace(self.mouse.get_position()[0] - self.char.obj.x, -abs(self.mouse.get_position()[1] - self.char.obj.y), 20, self.gui)
        self.char.draw_char()
