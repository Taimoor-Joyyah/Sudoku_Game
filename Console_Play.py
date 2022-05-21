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
        3. Options
        4. Exit
        """
        return select_numeric_option((1, 4), "OPTION > ", menu_prompt, "INVALID OPTION !!!")

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

    @staticmethod
    def print_state(cell, value, hint, life):
        print(f"Cell: {cell}, Value: {value}, Hints: {hint}, Life: {life}")

    def play(self):
        cell = value = option = cs = None
        hints_rem = (3 - self.game.difficulty // 3) * (self.game.map_size - 1)
        lives = (3 - self.game.difficulty // 3) * (self.game.map_size - 1)
        while True:
            if option is not None:
                self.display_frame(self.game.view_frame, cell)
                self.print_state(cell, value, hints_rem, lives)

            menu_prompt = f"""
            1. Select Cell
            2. Select Value
            3. Input Value
            4. Empty Cell
            5. Take Hint
            6. Leave Game 
            """

            option = select_numeric_option((1, 6), "OPTION > ", menu_prompt, "INVALID INPUT !!!")
            if option == 1:
                cell = self.select_cell()
                self.game.selected_cell_map(cell)
                cs = False
            elif option == 2:
                value = self.select_value()
            elif option == 3:
                if cell is None:
                    print("CELL NOT SELECTED !!!")
                elif value is None:
                    print("VALUE NOT SELECTED !!!")
                elif self.game.input_value(cell, value, cs):
                    print(f"Taken {value} at {cell}")
                    cs = True
                    if self.game.view_frame == self.game.solution_map:
                        self.display_frame(self.game.view_frame, None)
                        self.print_state(cell, value, hints_rem, lives)
                        break
                else:
                    print(f"{value} does not statisfy at {cell} !!!")
                    lives -= 1
                    if lives:
                        print(f"{lives} Lives Remaining")
                    else:
                        print("No Life Remaining !!!")
                        print("Game OVER !!!")
                        return False
            elif option == 4:
                if cell is None:
                    print("CELL NOT SELECTED !!!")
                else:
                    self.game.empty_cell(cell)
            elif option == 5:
                if hints_rem:
                    hint = self.game.hint()
                    print(f"HINT: {hint[1]} at {hint[0]}")
                    hints_rem -= 1
                    print(f"{hints_rem} Hint(s) Remaining !")
                else:
                    print("No Hint Remaining !!!")
            elif option == 6:
                print("Leaving Game...")
                return True
        print("Game WON")
        return True

    def start_game(self, select=False):
        self.game.generate_maps()
        if select:
            if not self.select_map():
                return
        self.display_frame(self.game.view_frame, None)
        self.play()

    def select_map(self):
        while True:
            self.display_frame(self.game.view_frame, None)

            menu_prompt = """
            1. Select and Play
            2. Next Map
            3. Back to Menu
            """

            option = select_numeric_option((1, 3), "OPTION > ", menu_prompt, "INVALID OPTION !!!")

            if option == 1:
                return True
            elif option == 2:
                print("NEXT MAP...")
                self.game.generate_maps()
            elif option == 3:
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

    def display_frame(self, frame, scell):
        def hex_print(value, c=None, k=False):
            if k and value == 0:
                if scell is not None and c is not None:
                    if c[0] == scell[0] and c[1] == scell[1]:
                        return '_'
                    elif self.game.scell_map[c[0]][c[1]]:
                        return '*'
                    else:
                        return '.'
                else:
                    return '.'
            elif value < 10:
                return value
            else:
                return ['A', 'B', 'C', 'D', 'E', 'F', '0'][value - 10]

        def borders():
            for n in range(self.game.map_size):
                if not n:
                    print("   ", end="")
                print("+" + "=" * (self.game.map_size * 3 + (2 if 0 < n < (self.game.map_size - 1) else 3)), end="")
            print("+")

        print()
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
                print(hex_print(cell, (ri, ci), True), end="  ")
            print("||")

        borders()

    @staticmethod
    def Exit():
        print("EXITING...")
        exit(1)
