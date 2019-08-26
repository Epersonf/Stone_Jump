from PPlay.sprite import *

class Char:
    jumping = False
    touching = False

    x_speed = 0
    y_speed = 0
    tend_y = 230
    gravity = 0.01

    obj = None
    def __init__(self, image_file):
        self.obj = Sprite(image_file)

    def jump(self, jump_force_x, jump_force_y):
        if self.jumping:
            return
        self.x_speed = (jump_force_x/280)
        self.y_speed = -(abs(jump_force_y)/140)
        self.jumping = True

    def hit_up(self):
        self.x_speed = 0
        self.y_speed = 0
        self.jumping = False
        self.touching = True

    def hit_down(self):
        if self.y_speed < 0:
            self.y_speed = 0

    def hit_side(self):
        self.x_speed = -(self.x_speed/2)

    def set_speed(self, new_spd_x, new_spd_y):
        self.x_speed = new_spd_x
        self.y_speed = new_spd_y

    def draw_char(self):
        self.y_speed += self.gravity
        self.obj.move_x(self.x_speed)
        self.obj.move_y(self.y_speed)

        #reflection
        if self.obj.x < 0 or self.obj.x > 1024 - self.obj.width:
            self.hit_side()
            if self.obj.x < 0:
                self.obj.x = 0
            else:
                self.obj.x = 1024 - self.obj.width


        #gameover
        if self.obj.y >= 768:
            exit(0)

        self.obj.draw()

