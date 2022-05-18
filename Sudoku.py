import random


class Sudoku:
    def __init__(self, map_size=3, difficulty=4):
        self.map_size: int = map_size  # temp 2
        self.difficulty = difficulty
        self.solution_map = None
        self.view_frame = None
        self.playable_frame = None
        self.mask_frame = None

    def generate_maps(self):
        self.solution_map = self.generate_solution()
        self.mask_frame = self.generate_mask()
        self.playable_frame = [[0 if c else 1 for c in r] for r in self.mask_frame]
        self.view_frame = [[c if self.mask_frame[ri][ci] else 0 for ci, c in enumerate(r)]
                           for ri, r in enumerate(self.solution_map)]

    def box_frame(self, frame):
        box_Frame = [[[[0] * self.map_size for c in range(self.map_size)]
                      for b in range(self.map_size)] for a in range(self.map_size)]
        for ri, row in enumerate(frame):
            for ci, cell in enumerate(row):
                box_Frame[ri // self.map_size][ci // self.map_size][ri % self.map_size][ci % self.map_size] = cell
        return box_Frame

    def rules_check(self, frame, position, value):
        if frame[position[0]][position[1]] == 0:
            for cell in frame[position[0]]:
                if cell == value:
                    return False
            for row in frame:
                if row[position[1]] == value:
                    return False
            rm, cm = position[0] // self.map_size, position[1] // self.map_size
            for row in frame[rm * self.map_size: (rm + 1) * self.map_size]:
                for cell in row[cm * self.map_size: (cm + 1) * self.map_size]:
                    if cell == value:
                        return False
            return True

    @staticmethod
    def valid_frame(frame):
        for row in frame:
            for cell in row:
                if cell == 0:
                    return False
        return True

    def generate_mask(self):
        frame = []
        for i in range(self.map_size ** 2):
            frame.append(random.choices([0, 1], weights=[4, 1], k=3 ** 2))
        return frame

    def generate_solution(self):
        range_list = list(range(1, (self.map_size ** 2) + 1))
        for force1 in range(64):
            frame = [[0 for b in range(self.map_size ** 2)] for a in range(self.map_size ** 2)]
            for ri, row in enumerate(frame):
                for force2 in range(1024):
                    for ci, cell in enumerate(row):
                        random.shuffle(range_list)
                        for value in range_list:
                            if self.rules_check(frame, (ri, ci), value):
                                frame[ri][ci] = value
                                break
                        else:
                            for c in range(ci):
                                frame[ri][c] = 0
                            break
                    else:
                        break
                else:
                    break
            else:
                if self.valid_frame(frame):
                    return frame
        else:
            return None

    @staticmethod
    def hex_print(value):
        if value < 10:
            return value
        else:
            if value == 10:
                return 'A'
            if value == 11:
                return 'B'
            if value == 12:
                return 'C'
            if value == 13:
                return 'D'
            if value == 14:
                return 'E'
            if value == 15:
                return 'F'
            if value == 16:
                return 'G'

    def display_frame(self, frame):
        for row in frame:
            for cell in row:
                print(self.hex_print(cell), end="  ")
            print()

    pass
# """ !@#$%^&*()_+}{":<>?|\/.,';][.+-*/ """
# """
#        0  1     2  3
#    +---------+---------+
# 0- ||  1  2  |  3  4  ||
# 1- ||  5  6  |  7  8  ||
#    ||--------+--------||
# 2- ||  9  0  |  1  2  ||
# 3- ||  3  4  |  5  6  ||
#    +---------+---------+
# """
