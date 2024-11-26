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
    game.state = initial_state  
    game.draw_board()



    # # Solve with BFS
    # print("Solving the puzzle with BFS...")
    solver = Solver(initial_state)
    solver.solve_with_bfs()






    # # Solve with DFS Recursive
    print("\nSolving the puzzle with DFS...")
    solver.solve_with_dfs_recursive()








#   # Solve with UCS
    print("\nSolving the puzzle with UCS...")
    solver.solve_with_ucs()




    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
