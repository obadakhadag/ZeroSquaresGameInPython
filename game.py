# game.py

import tkinter as tk
from state import State
from square import Square

class Game:
    def __init__(self, root):
        self.state = State()
        self.root = root
        self.root.title("Squares Game")
        self.root.geometry("800x700")
        self.label = tk.Label(self.root, text="Try to solve this if you can:", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)
        self.cell_size = 60
        self.canvas = tk.Canvas(self.root, width=self.cell_size * 11, height=self.cell_size * 8, bg="white")
        self.canvas.pack()
        self.root.bind("<KeyPress>", self.on_key_press)
        
        restart_button = tk.Button(self.root, text="Restart", command=self.reset_game)
        restart_button.pack(pady=10)

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for y, row in enumerate(self.state.board):
            for x, cell in enumerate(row):
                square = Square(x, y, self.cell_size, self.canvas)

                if cell == "#":
                    square.set_color("black")
                elif (y, x) == self.state.targets["B"] and not self.state.targets_reached["B"]:
                    square.set_outline("blue", 6)
                elif (y, x) == self.state.targets["R"] and not self.state.targets_reached["R"]:
                    square.set_outline("red", 6)

                if (y, x) == self.state.positions["B"] and not self.state.targets_reached["B"]:
                    square.set_color("blue")
                elif (y, x) == self.state.positions["R"] and not self.state.targets_reached["R"]:
                    square.set_color("red")

        if self.state.is_final_state():
            self.canvas.create_text(330, 240, text="You Win!", font=("Arial", 24), fill="green")




    def on_key_press(self, event):
        moves = {
            "Up": (-1, 0),
            "Down": (1, 0),
            "Left": (0, -1),
            "Right": (0, 1)
        }

        if event.keysym in moves:
            dy, dx = moves[event.keysym]
            # Move both squares according to the key press
            self.state = self.state.move_square("B", dy, dx)
            self.state = self.state.move_square("R", dy, dx)
            self.draw_board()

            # Print possible next states for debugging
            # print(f"\nNext possible states after moving {event.keysym}:")
            # print("For 'B':")
            # self.state.get_next_states()
            # print("For 'R':")
            # self.state.get_next_states()



            # Check if the game is won and display a message if so
            if self.state.is_final_state():
                print("Game completed! Final state reached.")




    def reset_game(self):
        self.state = State()
        self.draw_board()
