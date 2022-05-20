from Sudoku import *
from userdefined import select_numeric_option


class ConsolePlay:
    def __init__(self):
        self.game = Sudoku()

    @staticmethod
    def menu():
        menu_prompt = """
        1. Play Game
        2. Select Random Map
        3. Create Map
        4. Options
        5. Exit
        """
        return select_numeric_option((1, 5), "OPTION > ", menu_prompt, "INVALID OPTION !!!")

    @staticmethod
    def hex_dec(value: str, v=False):
        if v and value == '0':
            return 16
        arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        if value in arr:
            return arr.index(value)
        else:
            return -1

    def select_cell(self):
        while True:
            c = input("Select Cell > ").upper()
            if c and len(c) == 2 and c.isalnum():
                a, b = self.hex_dec(c[0]), self.hex_dec(c[1])
                if a != -1 or b != -1:
                    if self.game.valid_cell((a, b)):
                        return a, b
                    else:
                        print("THIS CELL CANNOT BE SELECTED !!!")
                else:
                    print("INVALID CELL INPUT !!!")
            else:
                print("INVALID INPUT !!!")

    def select_value(self):
        while True:
            v = input("Select Value > ").upper()
            if v and len(v) == 1 and v.isalnum():
                a = self.hex_dec(v, True)
                if a and self.game.valid_value(a):
                    return a
                else:
                    print("INVALID VALUE INPUT !!!")
            else:
                print("INVALID INPUT !!!")

    def play(self):
        while self.game.view_frame != self.game.solution_map:
            cell = self.select_cell()
            value = self.select_value()
            if self.game.input_value(cell, value):
                self.display_frame(self.game.view_frame)
            else:
                print(f"{value} does not statisfy at {cell} !!!")
        print("Game WON")

    def create_map(self):
        print("Creating Map")

    def start_game(self, select=False):
        self.game.generate_maps()
        if select:
            if not self.select_map():
                return
        self.display_frame(self.game.view_frame)
        self.play()

    def select_map(self):
        while True:
            self.display_frame(self.game.view_frame)

            print("""
            1- Select and Play
            2- Next Map
            3- Back to Menu
            """)

            while True:
                option = input("OPTION > ")

                if option and option.isnumeric() and 1 <= int(option) <= 4:
                    break
                else:
                    print("INVALID OPTION!!!")

            if option == '1':
                return True
            elif option == '2':
                print("NEXT MAP...")
                self.game.generate_maps()
            elif option == '3':
                print("Back to Menu...")
                return False

    def options(self):
        menu_prompt = """
        1. Set Map Size
        2. Set Difficulty
        3. Back to Menu
                """
        option = select_numeric_option((1, 3), "OPTION > ", menu_prompt, "INVALID OPTION !!!")

        if option == 1:
            self.game.set_map_size(select_numeric_option((2, 4), "Enter Map Size > ",
                                                         None, "Enter Map size between 2 and 4 (default 3)"))
        elif option == 2:
            self.game.set_difficulty(select_numeric_option((1, 8), "Enter Difficulty > ",
                                                           None, "Enter Difficulty between 1 and 8 (default 4)"))
        elif option == 3:
            print("Back to Menu...")

    def display_frame(self, frame):
        def hex_print(value, k=False):
            if k and value == 0:
                return "."
            elif value < 10:
                return value
            else:
                return ['A', 'B', 'C', 'D', 'E', 'F', '0'][value - 10]

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
            print(hex_print(i), end="  ")
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
            print(f"{hex_print(ri)}- ||", end="  ")

            for ci, cell in enumerate(row):
                if ci and not ci % self.game.map_size:
                    print("|", end="  ")
                print(hex_print(cell, True), end="  ")
            print("||")

        borders()

    @staticmethod
    def exit():
        print("EXITING...")
        exit(1)
