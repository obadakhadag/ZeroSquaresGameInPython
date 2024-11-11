# main.py

import tkinter as tk
from game import Game
from state import State  # Importing State to access debugging methods

def main():
    root = tk.Tk()
    game = Game(root)

    # Debug: Print possible next states for initial game state
    print("Initial next states for 'B':")
    game.state.get_next_states("B")  # Trigger board printing for debug

    root.mainloop()

if __name__ == "__main__":
    main()
