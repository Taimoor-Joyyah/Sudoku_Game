import random


class Sudoku:
    def __init__(self):
        self.map_size = 3
        self.difficulty = 4

    def generate_maps(self):
        self.solution_map = self.generate_solution()
        self.mask_solution = self.generate_mask()
        self.view_mask = [[b for b in a] for a in self.mask_solution]
        self.playable_frame = [[0 if c else 1 for c in r] for r in self.mask_solution]
        self.view_frame = [[c if self.mask_solution[ri][ci] else 0 for ci, c in enumerate(r)]
                           for ri, r in enumerate(self.solution_map)]

    def box_frame(self, frame):
        box_Frame = [[[[0] * self.map_size for c in range(self.map_size)]
                      for b in range(self.map_size)] for a in range(self.map_size)]
        for ri, row in enumerate(frame):
            for ci, cell in enumerate(row):
                box_Frame[ri // self.map_size][ci // self.map_size][ri % self.map_size][ci % self.map_size] = cell
        return box_Frame

    def rules_check(self, frame, position, value, gen=False):
        if gen or self.playable_frame[position[0]][position[1]]:
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

    def valid_cell(self, cell: tuple):
        return (cell[0] < self.map_size ** 2 and
                cell[1] < self.map_size ** 2) and self.playable_frame[cell[0]][cell[1]]

    def valid_value(self, value):
        return 1 <= value <= self.map_size ** 2

    def selected_cell_map(self, cell):
        self.scell_map = [[0 for b in range(self.map_size ** 2)] for a in range(self.map_size ** 2)]

        for ci in range(self.map_size ** 2):
            self.scell_map[cell[0]][ci] = 1
        for ri in range(self.map_size ** 2):
            self.scell_map[ri][cell[1]] = 1
        rm, cm = cell[0] // self.map_size, cell[1] // self.map_size
        for r in range(rm * self.map_size, (rm + 1) * self.map_size):
            for c in range(cm * self.map_size, (cm + 1) * self.map_size):
                self.scell_map[r][c] = 1

    def input_value(self, cell, value, cs):
        if cs:
            self.empty_cell(cell)
        if self.rules_check(self.view_frame, cell, value):
            self.view_frame[cell[0]][cell[1]] = value
            self.view_mask[cell[0]][cell[1]] = 1
            return True
        else:
            return False

    def empty_cell(self, cell):
        if self.playable_frame[cell[0]][cell[1]]:
            self.view_frame[cell[0]][cell[1]] = 0
            self.view_mask[cell[0]][cell[1]] = 0

    def generate_mask(self):
        frame = []
        for i in range(self.map_size ** 2):
            frame.append(random.choices([0, 1], weights=[self.difficulty, 1], k=self.map_size ** 2))
        return frame

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_map_size(self, map_size):
        self.map_size = map_size

    def generate_solution(self):
        range_list = list(range(1, (self.map_size ** 2) + 1))
        for force1 in range(50):
            frame = [[0 for b in range(self.map_size ** 2)] for a in range(self.map_size ** 2)]
            for ri, row in enumerate(frame):
                for force2 in range(100):
                    for ci, cell in enumerate(row):
                        random.shuffle(range_list)
                        for value in range_list:
                            if self.rules_check(frame, (ri, ci), value, True):
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

    def hint(self):
        cells = []
        for r in range(self.map_size ** 2):
            for c in range(self.map_size ** 2):
                if not self.view_frame[r][c]:
                    cells.append((r, c))
        cell = random.choice(cells)
        value = self.solution_map[cell[0]][cell[1]]
        return cell, value
