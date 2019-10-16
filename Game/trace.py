from Game.PPlay.sprite import *

class Trace:

    jumping = False
    touching = False

    x_speed = 0
    y_speed = 0
    tend_y = 230
    gravity = 0.01

    char = None
    obj = None

    @staticmethod
    def trace_distance():
        return 70

    def __init__(self, img_name, char_main):
        self.obj = Sprite(img_name)
        self.char = char_main

    def hit_up(self):
        self.x_speed = 0
        self.y_speed = 0
        self.jumping = False
        self.touching = True

    def hit_down(self):
        if self.y_speed < 0:
            self.y_speed = 0

    def hit_side(self):
        if not self.char.grab_mode:
            self.x_speed = -(self.x_speed / 2)

    def set_speed(self, new_spd_x, new_spd_y):
        self.x_speed = new_spd_x
        self.y_speed = new_spd_y

    def draw_trace(self, jump_force_x, jump_force_y, loops, gui):
        if not self.char.can_jump():
            return
        self.obj.x = self.char.obj.x + self.char.obj.width/2 - self.obj.width/2
        self.obj.y = self.char.obj.y
        self.x_speed = jump_force_x
        self.y_speed = jump_force_y
        for i in range(loops):
            self.y_speed += 1*self.trace_distance()
            self.obj.move_x((self.x_speed/380) * self.trace_distance())
            self.obj.move_y((self.y_speed/180) * self.trace_distance())

            if self.obj.x < 0 or self.obj.x > 1024 - self.obj.width:
                self.hit_side()
                if self.obj.x < 0:
                    self.obj.x = 0
                else:
                    self.obj.x = 1024 - self.obj.width
            if self.obj.y > 768:
                break
            self.obj.draw()
