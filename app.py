from Console_Play import *

game = ConsolePlay()
while True:
    option = game.menu()
    if option == 1:
        game.play_game()
    elif option == 2:
        game.play_game(True)
    elif option == 3:
        pass  # create map
    elif option == 4:
        pass  # option
    elif option == 5:
        game.exit()
