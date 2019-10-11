from Game.PPlay.sprite import *

class Btn:

    obj = None
    objOver = None
    gui = None
    size = 40
    color = (0, 0, 0)
    mouse = None

    def __init__(self, path, path2, window_, x=0, y=0):
        self.obj = Sprite(path)
        self.objOver = Sprite(path2)
        self.gui = window_
        self.obj.x = x - self.obj.width/2
        self.obj.y = y - self.obj.height/2
        self.objOver.x = x - self.objOver.width/2
        self.objOver.y = y - self.objOver.height/2
        self.mouse = self.gui.get_mouse()

    def set_location(self, x, y):
        self.obj.x = x - self.obj.width/2
        self.obj.y = y - self.obj.height/2
        self.objOver.x = x - self.objOver.width/2
        self.objOver.y = y - self.objOver.height/2

    def mouse_over(self):
        if self.obj.x <= self.mouse.get_position()[0] <= self.obj.x + self.obj.width:
            if self.obj.y <= self.mouse.get_position()[1] <= self.obj.y + self.obj.height:
                self.objOver.draw()
                return True
        self.color = (0, 0, 0)
        return False

    def draw(self):
        self.obj.draw()

        return self.mouse_over() and self.mouse.is_button_pressed(1)


