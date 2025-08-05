from collections import deque

def solve_8_puzzle_bfs(initial_state):
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]

        blank_index = current_state.index(0)
        row, col = divmod(blank_index, 3)
        moves = []
        if row > 0:
            moves.append((-1, 0))
        if row < 2:
            moves.append((1, 0))
        if col > 0:
            moves.append((0, -1))
        if col < 2:
            moves.append((0, 1))

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            new_blank_index = new_row * 3 + new_col
            new_state_list = list(current_state)
            new_state_list[blank_index], new_state_list[new_blank_index] = \
                new_state_list[new_blank_index], new_state_list[blank_index]
            new_state = tuple(new_state_list)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [current_state]))

    return None  # <-- moved here
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

if __name__ == "__main__":
    initial_puzzle = (1, 2, 3, 0, 4, 6, 7, 5, 8)  # Test with any solvable state
    solution_path = solve_8_puzzle_bfs(initial_puzzle)

    if solution_path:
        print("solution found")
        for i, state in enumerate(solution_path):
            print(f"\nstep {i}:")
            print_puzzle(state)
    else:
        print("no solution found")

