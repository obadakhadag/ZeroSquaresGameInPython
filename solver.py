from collections import deque
from state import State
import heapq  # For priority queue

class Solver:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.visited = []  # To keep track of visited states

    def solve_with_bfs(self):
        queue = [(self.initial_state, [])]  # Queue holds tuples of (current state, path)
        visited = []  # Visited states

        while queue:
            current_state, path = queue.pop(0)

            # Check if the state has already been visited
            if any(not current_state.NotEqualState(state) for state in visited):
                continue

            # Mark the current state as visited
            visited.append(current_state)

            # Check if the current state is the goal state
            if current_state.is_final_state():
                print("Solution found using BFS!")
                for step, state in enumerate(path + [current_state]):
                    print(f"Step {step}:")
                    state.print_board()
                    print()
                print(f"Total number of visited boards: {len(visited)}")
                return

            # Add next states to the queue
            for next_state in current_state.get_next_states():
                queue.append((next_state, path + [current_state]))

        print("No solution found using BFS.")
        print(f"Total number of visited boards: {len(visited)}")








    def solve_with_dfs_recursive(self, current_state=None, path=None):
        if current_state is None:
            current_state = self.initial_state  # Start from the initial state
        if path is None:
            path = []  # Initialize the path if not provided

        # Check if the state has already been visited
        if any(not current_state.NotEqualState(state) for state in self.visited):
            return False

        # Mark the current state as visited
        self.visited.append(current_state)

        # Check if the current state is the goal state
        if current_state.is_final_state():
            print("Solution found using DFS Recursive!")
            for step, state in enumerate(path + [current_state]):
                print(f"Step {step}:")
                state.print_board()
                print()
            print(f"Total number of visited boards: {len(self.visited)}")
            return True

        # Explore next states recursively
        for next_state in current_state.get_next_states():
            if self.solve_with_dfs_recursive(next_state, path + [current_state]):
                return True

        return False  # No solution found from this path





    def solve_with_dfs(self):
        stack = [(self.initial_state, [])]  # Stack holds tuples of (current state, path)
        visited = []  # Visited states

        while stack:
            current_state, path = stack.pop()

            # Check if the state has already been visited
            if any(not current_state.NotEqualState(state) for state in visited):
                continue

            # Mark the current state as visited
            visited.append(current_state)

            # Check if the current state is the goal state
            if current_state.is_final_state():
                print("Solution found using DFS!")
                for step, state in enumerate(path + [current_state]):
                    print(f"Step {step}:")
                    state.print_board()
                    print()
                print(f"Total number of visited boards: {len(visited)}")
                return

            # Add next states to the stack
            for next_state in current_state.get_next_states():
                stack.append((next_state, path + [current_state]))

        print("No solution found using DFS.")
        print(f"Total number of visited boards: {len(visited)}")















    # def solve_with_ucs(self):
    #     priority_queue = []  # Priority queue holds tuples of (cost, current state, path)
    #     heapq.heappush(priority_queue, (0, self.initial_state, []))  # Initial state with cost 0
    #     visited = []  # Visited states

    #     while priority_queue:
    #         cost, current_state, path = heapq.heappop(priority_queue)

    #         # Check if the state has already been visited
    #         if any(not current_state.NotEqualState(state) for state in visited):
    #             continue

    #         # Mark the current state as visited
    #         visited.append(current_state)

    #         # Check if the current state is the goal state
    #         if current_state.is_final_state():
    #             print("Solution found using UCS!")
    #             for step, state in enumerate(path + [current_state]):
    #                 print(f"Step {step}:")
    #                 state.print_board()
    #                 print()
    #             print(f"Total number of visited boards: {len(visited)}")
    #             print(f"Total cost of the path: {cost}")
    #             return

    #         # Add next states to the priority queue with updated cost
    #         for next_state in current_state.get_next_states():
    #             heapq.heappush(priority_queue, (cost + 1, next_state, path + [current_state]))

    #     print("No solution found using UCS.")
    #     print(f"Total number of visited boards: {len(visited)}")
