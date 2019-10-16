from Game.PPlay.sprite import *
from random import randint

class Stone_wall():

    gui = None

    def rand_stone(self):
        num = randint(1, 4)
        if randint(1, 100) == 1:
            num += 1000
        return "Assets/Bricks/Brick_" + str(num) + ".png"

    def gen_line(self, y):
        count = 0
        VEC = []
        while count <= self.gui.width:
            VEC.append(Sprite(self.rand_stone()))
            VEC[len(VEC) - 1].x = count
            VEC[len(VEC) - 1].y = y
            count += VEC[len(VEC) - 1].width
        return VEC

    def gen_matrix(self):
        count = -20
        VEC = []
        while count <= self.gui.height:
            VEC.append(self.gen_line(count))
            count += VEC[0][0].height
        return VEC

    def gen_new_line(self, WALL_MATRIX):
        WALL_MATRIX.insert(0, self.gen_line(WALL_MATRIX[0][0].y - WALL_MATRIX[0][0].height))

    vel = 40
    WALL_MATRIX = []

    def __init__(self, gui):
        self.gui = gui
        self.WALL_MATRIX = self.gen_matrix()

    def draw(self):
        if self.WALL_MATRIX[len(self.WALL_MATRIX) - 1][0].y > self.gui.height:
            self.WALL_MATRIX.pop(len(self.WALL_MATRIX) - 1)
            self.gen_new_line(self.WALL_MATRIX)
        for line in self.WALL_MATRIX:
            for brick in line:
                brick.y += self.vel * self.gui.delta_time()
                brick.draw()
