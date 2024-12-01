import heapq  
from collections import deque
from state import State  


class Solver:
    def __init__(self, initial_state):
        
        self.initial_state = initial_state
        self.visited = [] 






    def solve_with_bfs(self):
        queue = [(self.initial_state, [])]  
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
            current_state = self.initial_state  
        if path is None:
            path = []  

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

        return False  # No solution found 









    def solve_with_ucs(self):
        priority_queue = []
        heapq.heappush(priority_queue, (0, self.initial_state, []))
        visited = []  

        while priority_queue:
            total_cost, current_state, path = heapq.heappop(priority_queue)




            if any(not current_state.NotEqualState(state) for state in visited):
                continue


            # Mark the current state as visited
            visited.append(current_state)

            # Check if the current state is the goal state
            if current_state.is_final_state():
                print("Solution found using UCS!")
                for step, state in enumerate(path + [current_state]):
                    print(f"Step {step}:")
                    state.print_board()
                    print()
                print(f"Total cost: {total_cost}")
                print(f"Total number of visited boards: {len(visited)}")
                return

            # Add next states to the priority queue with their costs
            for next_state in current_state.get_next_states():
                heapq.heappush(priority_queue, (total_cost + 1, next_state, path + [current_state]))

        print("No solution found using UCS.")
        print(f"Total number of visited boards: {len(visited)}")
        
        
        
        
        
        
        
        
        
    def solve_with_a_star(self):
        
        priority_queue = []
        initial_heuristic = self.initial_state.calculate_heuristic()
        heapq.heappush(priority_queue, (initial_heuristic, 0, self.initial_state, []))  # (f = g + h, g, state, path)
        visited = []

        while priority_queue:
            _, g, current_state, path = heapq.heappop(priority_queue)

            # Skip already visited states
            if any(not current_state.NotEqualState(state) for state in visited):
                continue

            visited.append(current_state)

            # Check if the goal state is reached
            if current_state.is_final_state():
                print("Solution found using A*!")
                for step, state in enumerate(path + [current_state]):
                    heuristic_value = state.calculate_heuristic()
                    print(f"Step {step} (Heuristic: {heuristic_value}):")
                    state.print_board()
                    print()

                # Print final details
                final_heuristic = current_state.calculate_heuristic()
                print(f"Final heuristic value: {final_heuristic}")
                print(f"Total cost (steps): {g}")
                print(f"Total number of visited boards: {len(visited)}")
                return

            # Expand neighbors
            for next_state in current_state.get_next_states():
                heuristic = next_state.calculate_heuristic()
                heapq.heappush(priority_queue, (g + 1 + heuristic, g + 1, next_state, path + [current_state]))

        print("No solution found using A*.")
        print(f"Total number of visited boards: {len(visited)}")