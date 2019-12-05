from Game.PPlay.window import *
from Game.game import *
from Game.main_menu import *
from Game.gameover import *
from Game.PPlay.sound import *

level = [0]

gui = Window(1024, 768)
gui.set_title("Stone Jump")
game = Game_itself(gui, level)
main_menu = Main_menu(gui, level, game)
gameover_menu = Gameover(gui, level, game)
sound = Sound("Assets/music.ogg")
sound.set_volume(80)
sound.set_repeat(True)

while True:
    if level[0] == 0:
        #case menu
        gui.set_background_color((0, 0, 0))
        main_menu.draw()
    elif level[0] == 1:
        if not sound.is_playing():
            sound.play()
        game.draw()
    elif level[0] == 2:
        #gameover
        if (sound.is_playing()):
            sound.stop()
        scoreFinal = game.score_counter
        score = game.score
        score.x = 415
        score.y = 450
        gui.set_background_color((0, 0, 0))
        gameover_menu.draw()
        score.draw(scoreFinal)
    gui.update()
