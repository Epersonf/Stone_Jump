from Game.PPlay.window import *
from Game.game import *
from Game.main_menu import *
from Game.gameover import *

level = [0]

gui = Window(1024, 768)
gui.set_title("Game")
game = Game_itself(gui, level)
main_menu = Main_menu(gui, level, game)
gameover_menu = Gameover(gui, level, game)

while True:
    if level[0] == 0:
        #case menu
        gui.set_background_color((0, 0, 0))
        main_menu.draw()
    elif level[0] == 1:
        game.draw()
    elif level[0] == 2:
        #gameover
        gui.set_background_color((0, 0, 0))
        gameover_menu.draw()
    gui.update()
