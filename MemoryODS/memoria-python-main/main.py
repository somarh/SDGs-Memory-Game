#main

from game import Game

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
    g.game2_loop()
    g.game3_loop()