from PPlay.window import *
from char import *
from ground import *
from trace import *
from random import randint



gui = Window(1024, 768)
gui.set_title("Game")
char = Char("Assets/Char.png")
char.obj.set_position(1024/2-char.obj.width/2, 768/2-char.obj.height/2)

keyboard = gui.get_keyboard()
mouse = gui.get_mouse()

trace = Trace("Assets/Trace.png", char)

grounds_initial_qt = 8
GROUNDS = [None]*grounds_initial_qt
for i in range(grounds_initial_qt):
    GROUNDS[i]  = Ground("Assets/Ground_1.png", char, mouse, GROUNDS, "Assets/Arrow.png")
    if i == 0:
        GROUNDS[i].obj.set_position(1024/2-GROUNDS[i].obj.width/2, 768/2 + 200)
    elif i == 1:
        GROUNDS[i].obj.set_position(1024/2 - 400, 768 / 2 + 100)
    elif i == 2:
        GROUNDS[i].obj.set_position(1024 / 2 + 250, 768 / 2 + 100)
    elif i == 3:
        GROUNDS[i].obj.set_position(1024 / 2 + 350, 300)
    elif i == 4:
        GROUNDS[i].obj.set_position(1024 / 2 - 500, 300)


score = 0
while True:
    gui.set_background_color((150, 150, 240))

    for g in GROUNDS:
        g.draw_ground()

    score += 1
    #char edit
    trace.draw_trace(mouse.get_position()[0] - char.obj.x, -abs(mouse.get_position()[1] - char.obj.y), 20)
    char.draw_char()
    gui.update()
