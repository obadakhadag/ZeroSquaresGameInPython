# state.py

class State:
    def __init__(self, positions=None, targets=None, targets_reached=None):
        self.board = [
            [" ", "#", "#", "#", "#", "#", " ", " ", " ", " ", " "],
            ["#", "#", "R", " ", " ", "#", "#", "#", "#", "#", " "],
            ["#", " ", " ", " ", " ", "#", "#", "T_B", " ", "#", " "],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#"],
            ["#", " ", " ", " ", "#", "#", "#", " ", " ", "T_R", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#"],
            ["#", "#", "B", " ", "#", "#", "#", "#", "#", "#", " "],
            [" ", "#", "#", "#", "#", " ", " ", " ", " ", " ", " "],
        ]
        self.positions = positions or {"B": (6, 2), "R": (1, 2)}
        self.targets = targets or {"B": (2, 7), "R": (4, 9)}
        self.targets_reached = targets_reached or {"B": False, "R": False}

    def move_square(self, color, dy, dx):
        if self.targets_reached[color]:
            return self

        y, x = self.positions[color]
        while True:
            new_y, new_x = y + dy, x + dx
            if self.board[new_y][new_x] == "#" or (new_y, new_x) in self.positions.values():
                break
            y, x = new_y, new_x

        new_positions = self.positions.copy()
        new_positions[color] = (y, x)
        
        new_targets_reached = self.targets_reached.copy()
        if new_positions[color] == self.targets[color]:
            new_targets_reached[color] = True

        return State(new_positions, self.targets, new_targets_reached)
    
    
    
    
    
    
    def is_final_state(self):
        return all(self.targets_reached.values())

    def get_next_states(self, color):
        directions = {
            "Up": (-1, 0),
            "Down": (1, 0),
            "Left": (0, -1),
            "Right": (0, 1)
        }

        for direction, (dy, dx) in directions.items():
            new_state_B = self.move_square("B", dy, dx)
            new_state_R = new_state_B.move_square("R", dy, dx)
            print(f"Both squares move {direction}:")
            new_state_R.print_board()
            print()

    def print_board(self):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if (y, x) == self.positions["B"]:
                    print("B", end=" ")
                elif (y, x) == self.positions["R"]:
                    print("R", end=" ")
                elif cell == "#":
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            print()
