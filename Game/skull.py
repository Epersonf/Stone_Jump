from Game.PPlay.sprite import *
from random import randint

class Skull:

    name = ["neutral", "red", "horror"]
    skullType = 0

    path = "Assets/Skull_Assets/"

    sprites = [None]*3

    gui = None
    disbled = False

    skullPos = [0, 0]
    arrowPos = [-1000, -1000]

    anim = 0

    stage = 0

    char = None

    def __init__(self, gui, char):
        self.gui = gui
        self.char = char

        for i in range(3):
            self.sprites[i] = [self.name[i] + "Skull.png", self.name[i] + "Attack.png", self.name[i] + "Arrow.png"]
            self.sprites[i] = [Sprite(self.path + self.sprites[i][0]),
                               Sprite(self.path + self.sprites[i][1]),
                               Sprite(self.path + self.sprites[i][2])]

    thrown = False

    def throw_arrow(self):
        self.thrown = True
        self.arrowPos = self.skullPos.copy()
        self.arrowPos[0] += self.sprites[self.skullType][self.stage-1].width/2

    def draw(self, score):

        if self.thrown:
            self.arrowPos[1] -= 700 * self.gui.delta_time() * (self.skullType + 1)/2
            if self.arrowPos[1] < 0 - self.sprites[self.skullType][2].height:
                self.thrown = False
            else:
                self.sprites[self.skullType][2].draw()
            if self.sprites[self.skullType][2].collided(self.char.obj):
                self.thrown = False
                self.char.hit_up()
                self.char.jump(randint(-900, 900), randint(100, 200*(self.skullType+1)))

        if self.stage != 0:
            self.sprites[self.skullType][self.stage-1].x = self.skullPos[0]
            self.sprites[self.skullType][self.stage-1].y = self.skullPos[1]
            self.sprites[self.skullType][self.stage-1].draw()

            self.sprites[self.skullType][2].x = self.arrowPos[0]
            self.sprites[self.skullType][2].y = self.arrowPos[1]

        if self.stage == 0 and score % 60 == 0:
            self.stage = 1
            self.skullType = randint(0, 2)
            self.skullPos[1] = self.gui.height + self.sprites[self.skullType][self.stage-1].height
        elif self.stage == 1:
            self.skullPos[0] = self.char.obj.x - self.sprites[self.skullType][self.stage-1].width/2
            if self.skullPos[1] >= self.gui.height - self.sprites[self.skullType][self.stage-1].height:
                self.skullPos[1] -= 300 * self.gui.delta_time()
            else:
                self.stage = 2
                self.thrown = False
                self.throw_arrow()
        elif self.stage == 2:
            if self.skullPos[1] <= self.gui.height + self.sprites[self.skullType][self.stage-1].height:
                self.skullPos[1] += 50 * self.gui.delta_time()
            else:
                self.stage = 0




