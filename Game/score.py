from Game.PPlay.gameimage import *


class Score:
    gui = None
    x = None
    y = None
    NUMBERS = []

    def __init__(self, path, gui, x=0, y=0):
        obj = gameobject(path)
        self.NUMBERS.append(obj)
        for i in range(10):
            self.NUMBERS.append(gameobject(path + str(i + 1)))
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
            self.NUMBERS[st[i]+1].x = self.x + dist
            self.NUMBERS[st[i]+1].y = self.y
            self.NUMBERS[st[i]+1].draw()
            dist += self.NUMBERS[st[i]+1].width
