from Game.PPlay.sprite import *
from random import randint

class Ground:

    speed = 0.05

    obj = None
    char = None
    mouse = None
    arrow = None
    GROUNDS = None
    def __init__(self, img_obj, c, d, e, img_arrow):
        self.obj = Sprite(img_obj)
        self.char = c
        self.mouse = d
        self.GROUNDS = e
        self.arrow = Sprite(img_arrow)

    def draw_ground(self):

        self.obj.move_y(self.speed)

        #collision
        if self.char.obj.collided(self.obj) and self.obj.x + self.obj.width > self.char.obj.x > self.obj.x - self.obj.width:
            if self.char.obj.y < self.obj.y - self.obj.height / 2:
                self.char.hit_up()
            elif self.char.obj.y > self.obj.y + self.obj.height / 2:
                self.char.hit_down()
        elif self.char.obj.collided(self.obj):
            self.char.hit_side()

        #warning
        if self.obj.y < -self.obj.height:
            self.arrow.x = self.obj.x
            self.arrow.y = self.arrow.height
            self.arrow.draw()

        #jump
        if self.mouse.is_button_pressed(1):
            self.char.jump(self.mouse.get_position()[0] - self.char.obj.x, -abs(self.mouse.get_position()[1] - self.char.obj.y))

        #down
        if self.obj.y > 768 + self.obj.height + self.char.obj.height:
            collided = True
            while collided:
                self.obj.x = randint(0, 1024 - self.obj.width)
                self.obj.y = -300
                self.speed = 0.02 + randint(1,100)/1000
                collided = False
                for i in range(len(self.GROUNDS)):
                    if self.obj.collided(self.GROUNDS[i].obj) and self.obj != self.GROUNDS[i].obj:
                        collided = True
                        break
        self.obj.draw()


