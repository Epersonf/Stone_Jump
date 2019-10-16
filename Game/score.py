from Game.PPlay.gameimage import *


class Score:
    gui = None
    x = None
    y = None
    NUMBERS = []

    def __init__(self, path, gui, x=0, y=0):
        obj = GameImage(path + ".png")
        self.NUMBERS.append(obj)
        for i in range(10):
            self.NUMBERS.append(GameImage(path + str(i) + ".png"))
        self.gui = gui
        self.x = x
        self.y = y

    def draw(self, value):
        dist = 0
        self.NUMBERS[0].x = self.x + dist
        self.NUMBERS[0].y = self.y
        self.NUMBERS[0].draw()
        dist += self.NUMBERS[0].width
        st = str(value)
        for i in range(len(st)):
            r = int(st[i])+1
            self.NUMBERS[r].x = self.x + dist
            self.NUMBERS[r].y = self.y
            self.NUMBERS[r].draw()
            dist += self.NUMBERS[r].width
