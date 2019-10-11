from Game.PPlay.sprite import *

class Btn:

    obj = None
    text = None
    gui = None
    size = 40
    color = (0, 0, 0)
    mouse = None
    padding = 0

    def __init__(self, path, txt, window_, x=0, y=0):
        self.obj = Sprite(path)
        self.text = txt
        self.gui = window_
        self.obj.x = x
        self.obj.y = y
        self.mouse = self.gui.get_mouse()

    def set_location(self, x, y):
        self.obj.x = x
        self.obj.y = y

    def mouse_over(self):
        if self.obj.x <= self.mouse.get_position()[0] <= self.obj.x + self.obj.width:
            if self.obj.y <= self.mouse.get_position()[1] <= self.obj.y + self.obj.height:
                self.color = (100, 100, 100)
                self.padding = 20
                return True
        self.color = (0, 0, 0)
        self.padding = 0
        return False

    def draw(self):
        self.obj.draw()
        self.gui.draw_text(self.text, self.obj.x + self.obj.width//4 + self.padding, self.obj.y, int(self.obj.width)//6, self.color)

        return self.mouse_over() and self.mouse.is_button_pressed(1)


