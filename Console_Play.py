from Sudoku import *

class ConsolePlay:
    def __init__(self, map_size=3, difficulty=4):
        self.game = Sudoku(map_size, difficulty)

    @staticmethod
    def menu():
        print("""
        1. Play Game
        2. Select Random Map
        3. Create Map
        4. Options
        5. Exit
        """)

        while True:
            option = input("OPTION > ")
            if option and option.isnumeric() and 1 <= int(option) <= 5:
                return int(option)
            else:
                print("INVALID OPTION !!!")

    def play_game(self, select=False):
        self.game.generate_maps()
        if select:
            self.select_map()
        else:
            self.display_frame(self.game.view_frame)
        # Play

    def select_map(self):
        while True:
            self.display_frame(self.game.view_frame)

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
    def hex_print(value, k=False):
        if k and value == 0:
            return "."
        elif value < 10:
            return value
        else:
            return ['A', 'B', 'C', 'D', 'E', 'F', 'G'][value - 10]

    def display_frame(self, frame):
        def borders():
            for n in range(self.game.map_size):
                if not n:
                    print("   ", end="")
                print("+" + "-" * (self.game.map_size * 3 + (2 if 0 < n < (self.game.map_size - 1) else 3)), end="")
            print("+")

        for i in range(self.game.map_size ** 2):
            if not i:
                print("       ", end="")
            if i and not i % self.game.map_size:
                print("   ", end="")
            print(self.hex_print(i), end="  ")
        print("")

        borders()

        for ri, row in enumerate(frame):
            if ri and not ri % self.game.map_size:
                for i in range(self.game.map_size):
                    if i:
                        print("+", end="")
                    else:
                        print("   ", end="||")
                    print("-" * (self.game.map_size * 3 + 2), end="")
                print("||")
            print(f"{self.hex_print(ri)}- ||", end="  ")

            for ci, cell in enumerate(row):
                if ci and not ci % self.game.map_size:
                    print("|", end="  ")
                print(self.hex_print(cell, True), end="  ")
            print("||")

        borders()

    @staticmethod
    def exit():
        print("EXITING...")
        exit(1)
