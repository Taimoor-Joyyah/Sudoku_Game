from Sudoku import *


class ConsolePlay:
    def __int__(self, map_size=3, difficulty=4):
        self.game = Sudoku(map_size, difficulty)

    @staticmethod
    def menu():
        print("""
            1. Play Game
            2. Select Random Map
            3. Create Map
            3. Options
            4. Exit
        """)

        while True:
            option = input("OPTION > ")
            if option and option.isnumeric() and 1 <= int(option) <= 4:
                return option
            else:
                print("INVALID OPTION !!!")

    def play_game(self, select=False):
        self.game.generate_maps()
        if select:
            self.select_map()
        else:
            self.game.display_frame(self.game.view_frame)
        # Play

    def select_map(self):
        while True:
            self.game.display_frame(self.game.view_frame)

            while True:
                option = input("Enter 'N' for NEXT or 'P' to Play > ")

                if option and (option.upper() == 'N' or option.upper() == 'P'):
                    break
                else:
                    print("INVALID OPTION !!!")

            if option.upper() == 'P':
                break
            else:
                print("NEXT MAP...")
                self.game.generate_maps()

    @staticmethod
    def exit():
        print("EXITING...")
        exit(1)
