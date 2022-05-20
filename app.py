from Console_Play import *

game = ConsolePlay()
while True:
    option = game.menu()
    if option == 1:
        game.start_game()
    elif option == 2:
        game.start_game(True)
    elif option == 3:
        game.create_map()
    elif option == 4:
        game.options()
    elif option == 5:
        game.exit()

# ..7..*... * is selected
