from collections import deque
from state import State


class Solver:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def solve_with_bfs(self):
        """
        Solves the game using the BFS algorithm.
        Prints the path to the solution and the number of visited boards.
        """
        queue = [(self.initial_state, [])]  # Queue holds tuples of (current state, path)
        visited = []  # List to store visited states

        while queue:
            current_state, path = queue.pop(0)

            # Check if the state has already been visited
            if any(not current_state.NotEqualState(state) for state in visited):
                continue

            # Mark the current state as visited
            visited.append(current_state)

            # Print the current board
            print(f"Visited Board {len(visited)} (BFS):")
            current_state.print_board()
            print()

            # Check if the current state is the goal state
            if current_state.is_final_state():
                print("Solution found using BFS!")
                for step, state in enumerate(path + [current_state]):
                    print(f"Step {step}:")
                    state.print_board()
                    print()
                print(f"Number of visited boards: {len(visited)}")
                return

            # Add next states to the queue
            for next_state in current_state.get_next_states():
                queue.append((next_state, path + [current_state]))

        print("No solution found using BFS.")
        print(f"Number of visited boards: {len(visited)}")

    def solve_with_dfs(self):
        """
        Solves the game using the DFS algorithm.
        Prints the path to the solution and the number of visited boards.
        """
        stack = [(self.initial_state, [])]  # Stack holds tuples of (current state, path)
        visited = []  # List to store visited states

        while stack:
            current_state, path = stack.pop()

            # Check if the state has already been visited
            if any(not current_state.NotEqualState(state) for state in visited):
                continue

            # Mark the current state as visited
            visited.append(current_state)

            # Print the current board
            print(f"Visited Board {len(visited)} (DFS):")
            current_state.print_board()
            print()

            # Check if the current state is the goal state
            if current_state.is_final_state():
                print("Solution found using DFS!")
                for step, state in enumerate(path + [current_state]):
                    print(f"Step {step}:")
                    state.print_board()
                    print()
                print(f"Number of visited boards: {len(visited)}")
                return

            # Add next states to the stack
            for next_state in current_state.get_next_states():
                stack.append((next_state, path + [current_state]))

        print("No solution found using DFS.")
        print(f"Number of visited boards: {len(visited)}")
