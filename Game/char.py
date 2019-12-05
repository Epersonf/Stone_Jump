from Game.PPlay.sprite import *
from Game.PPlay.gameimage import *

class Char:
    jumping = True
    touching = False
    grab_mode = False
    did_grab = False

    x_speed = 0
    y_speed = 0
    gravity = 0.01
    tend_y = 2

    obj = None
    level_manager = None
    gui = None
    mouse = None
    selected_anim = 0
    anim = None

    def __init__(self, image_file, level, gui_main):
        self.obj = Sprite(image_file)
        self.level_manager = level
        self.gui = gui_main
        self.mouse = self.gui.get_mouse()
        self.anim = [GameImage("Assets/Char_Stand.png"),
                     GameImage("Assets/Char_Left.png"),
                     GameImage("Assets/Char_Right.png"),
                     GameImage("Assets/Char_Left_Grabbing.png"),
                     GameImage("Assets/Char_Right_Grabbing.png"),
                     GameImage("Assets/Char_Falling.png")
                     ]

    def can_jump(self):
        if not (not self.jumping or (self.jumping and self.touching_wall)):
            return False
        if self.jumping or not self.touching:
            if not self.grab_mode or self.did_grab:
                return False
        return True

    def jump(self, jump_force_x, jump_force_y):
        if self.jumping:
            return
        self.x_speed = (jump_force_x/780)
        if self.x_speed > 0:
            self.selected_anim = 2
        else:
            self.selected_anim = 1
        self.y_speed = -(abs(jump_force_y)/400)
        self.jumping = True

    def hit_up(self):
        self.did_grab = False
        self.x_speed = 0
        self.y_speed = 0
        self.jumping = False
        self.touching = True
        self.selected_anim = 0

    def hit_down(self):
        if self.y_speed < 0:
            self.y_speed = 0

    touching_wall = False

    def hit_side(self):
        if not self.grab_mode and not self.did_grab:
            self.x_speed = -(self.x_speed / 2)
            if self.touching_wall:
                #release_btn while
                self.jumping = False
                self.did_grab = True
                self.jump(self.mouse.get_position()[0] - self.obj.x, -abs(self.mouse.get_position()[1] - self.obj.y))
                self.touching_wall = False
        else:
            self.y_speed = 0.4
            self.touching_wall = True
            if self.x_speed > 0:
                self.selected_anim = 4
            else:
                self.selected_anim = 3

    def set_speed(self, new_spd_x, new_spd_y):
        self.x_speed = new_spd_x
        self.y_speed = new_spd_y


    def draw_char(self):
        if self.y_speed <= self.tend_y:
            self.y_speed += self.gravity * self.gui.delta_time() * 160
        self.obj.x += (self.x_speed) * self.gui.delta_time() * 1300
        self.obj.y += (self.y_speed) * self.gui.delta_time() * 1300

        #grab_mode
        if self.mouse.is_button_pressed(0):
            self.grab_mode = True
        else:
            self.grab_mode = False

        #reflection window border
        if self.obj.x < 0 or self.obj.x > self.gui.width - self.obj.width - 20:
            self.hit_side()
            if self.obj.x < 0:
                self.obj.x = 0
            else:
                self.obj.x = self.gui.width - self.obj.width - 20
        else:
            self.touching_wall = False

        #gameover
        if self.obj.y >= 768:
            self.level_manager[0] = 2

        if self.jumping and not self.touching_wall and self.y_speed > 0:
            self.selected_anim = 5

        self.anim[self.selected_anim].x = self.obj.x
        self.anim[self.selected_anim].y = self.obj.y
        self.anim[self.selected_anim].draw()

        self.obj.draw()

