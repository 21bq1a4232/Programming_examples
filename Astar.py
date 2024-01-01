import heapq

# Define the goal state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # Represents blocks arranged in order

# Define the possible moves for the blank space
moves = {
    0: (1, 3),
    1: (0, 2, 4),
    2: (1, 5),
    3: (0, 4, 6),
    4: (1, 3, 5, 7),
    5: (2, 4, 8),
    6: (3, 7),
    7: (4, 6, 8),
    8: (5, 7)
}

# Define the Manhattan distance heuristic function
def heuristic(state):
    return sum(abs(i // 3 - (state[i] - 1) // 3) + abs(i % 3 - (state[i] - 1) % 3) for i in range(9) if state[i] != 0)

# Define the A* algorithm function
def solve_puzzle(initial_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (heuristic(initial_state), 0, initial_state))  # Enqueue initial state with priority based on heuristic and cost

    while open_list:
        _, cost, current_state = heapq.heappop(open_list)  # Dequeue state with lowest priority
        if current_state == goal_state:
            return cost

        closed_set.add(current_state)

        blank_index = current_state.index(0)
        for move in moves[blank_index]:
            new_state = list(current_state)
            new_state[blank_index], new_state[move] = new_state[move], new_state[blank_index]
            if tuple(new_state) not in closed_set:
                new_cost = cost + 1
                priority = new_cost + heuristic(new_state)
                heapq.heappush(open_list, (priority, new_cost, tuple(new_state)))
    return -1
initial_state = (1, 0, 3, 4, 2, 5, 7, 8, 6)  # Initial arrangement of blocks
minimum_moves = solve_puzzle(initial_state)
if minimum_moves != -1:
    print("Minimum number of moves required:", minimum_moves)
else:
    print("No solution found for the given initial state.")