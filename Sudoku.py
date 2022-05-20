import random


class Sudoku:
    def __init__(self):
        self.map_size = 3
        self.difficulty = 4

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
