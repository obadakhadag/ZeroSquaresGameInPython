import tkinter as tk
from state import State
from solver import Solver
from game import Game

def main():
    # Initialize the Tkinter root
    root = tk.Tk()

    # Create the initial state using its default initialization
    initial_state = State()

    # Initialize and start the GUI
    game = Game(root)
    game.state = initial_state  # Sync the game GUI with the initial state
    game.draw_board()  # Draw the initial board

    # Solve the puzzle in the background
    print("Solving the puzzle...")
    solver = Solver(initial_state)
    solver.solve()

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
