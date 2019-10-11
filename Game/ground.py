from Game.PPlay.sprite import *
from random import randint

class Ground:

    speed = 0.05

    obj = None
    char = None
    mouse = None
    arrow = None
    GROUNDS = None
    gui = None
    up = False
    down = False
    def __init__(self, img_obj, c, d, e, img_arrow, g):
        self.obj = Sprite(img_obj)
        self.char = c
        self.mouse = d
        self.GROUNDS = e
        self.arrow = Sprite(img_arrow)
        self.gui = g


    prev_x = None
    dif_y = None
    anim = None
    def draw_ground(self):

        self.obj.y += (self.speed) * self.gui.delta_time() * 1300

        #collision
        marginY = (self.obj.height/100)*10
        marginX = 5
        if self.obj.x - marginX < self.char.obj.x < self.obj.x + self.obj.width - self.char.obj.width/2 + marginX:
            if self.obj.collided(self.char.obj) and self.obj.y - marginY < self.char.obj.y + self.char.obj.height < self.obj.y + marginY:
                self.char.y_speed = self.speed
                self.char.hit_up()
                self.down = True
            elif self.obj.collided(self.char.obj) and self.obj.y + self.obj.height - marginY < self.char.obj.y < self.obj.y + self.obj.height + marginY:
                self.char.hit_down()
                self.up = True
        elif self.obj.collided(self.char.obj) and self.obj.y - marginY < self.char.obj.y + self.char.obj.height < self.obj.y + marginY:
            if self.obj.x + self.obj.width / 2 < self.char.obj.x + self.obj.width / 2:
                self.char.obj.x += 50 * self.gui.delta_time()
            else:
                self.char.obj.x -= 50 * self.gui.delta_time()
            self.char.y_speed = self.speed
            self.char.hit_up()
            self.down = True
        elif self.obj.collided(self.char.obj):
            if self.anim is None:
                if self.obj.x + self.obj.width/2 < self.char.obj.x + self.obj.width/2:
                    self.anim = 3
                else:
                    self.anim = 4
            self.char.x_speed = -self.char.x_speed/2
            if self.char.grab_mode:
                if self.prev_x is None:
                    self.prev_x = self.char.obj.x
                else:
                    self.char.obj.x = self.prev_x
                if self.dif_y is None:
                    self.dif_y = self.obj.y - self.char.obj.y
                else:
                    self.char.obj.y = self.obj.y - self.dif_y
                self.char.hit_up()
                self.char.selected_anim = self.anim
                if not self.mouse.is_button_pressed(0):
                    self.char.jump(self.mouse.get_position()[0] - self.char.obj.x, -abs(self.mouse.get_position()[1] - self.char.obj.y))
                    self.prev_x = None
                    self.dif_y = None
                    self.anim = None
            else:
                self.prev_x = None
                self.dif_y = None
                self.anim = None
        else:
            self.down = False
            self.up = False

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


