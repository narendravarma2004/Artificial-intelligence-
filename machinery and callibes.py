from collections import deque

# State representation: [left_m, left_c, boat, right_m, right_c]
# Initial state: [3, 3, 1, 0, 0]
# Final state: [0, 0, 0, 3, 3]

def is_valid(state):
    # Check if any side has negative people or missionaries are outnumbered by cannibals
    if (state[0] < 0 or state[1] < 0 or state[3] < 0 or state[4] < 0 or
        state[0] > 3 or state[1] > 3 or state[3] > 3 or state[4] > 3 or
        (state[0] < state[1] and state[0] > 0) or (state[3] < state[4] and state[3] > 0)):
        return False
    return True

def is_goal(state):
    return state == [0, 0, 0, 3, 3]

def get_successors(state):
    successors = []
    if state[2] == 1:  # Boat is on the left side
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = [state[0] - m, state[1] - c, 0, state[3] + m, state[4] + c]
                    if is_valid(new_state):
                        successors.append(new_state)
    else:  # Boat is on the right side
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = [state[0] + m, state[1] + c, 1, state[3] - m, state[4] - c]
                    if is_valid(new_state):
                        successors.append(new_state)
    return successors

def bfs():
    start_state = [3, 3, 1, 0, 0]
    if is_goal(start_state):
        return [start_state]

    visited = set()
    queue = deque()
    queue.append([start_state, []])

    while queue:
        current_state, path = queue.popleft()
        visited.add(tuple(current_state))

        for successor in get_successors(current_state):
            if tuple(successor) not in visited:
                if is_goal(successor):
                    return path + [current_state, successor]
                queue.append([successor, path + [current_state]])

    return None

def print_solution(solution):
    if solution is None:
        print("No solution exists.")
    else:
        print("Solution:")
        for state in solution:
            print(state[:3], " | ", state[3:])

# Find and print the solution
solution_path = bfs()
print_solution(solution_path)
