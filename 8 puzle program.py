import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def calculate_heuristic(self):
        total_distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_row, goal_col = divmod(self.state[i][j] - 1, 3)
                    total_distance += abs(i - goal_row) + abs(j - goal_col)
        return total_distance

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(node):
    i, j = get_blank_position(node.state)
    neighbors = []

    for action in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + action[0], j + action[1]

        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in node.state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(PuzzleNode(new_state, node, action, node.cost + 1))

    return neighbors

def print_solution(node):
    if node.parent is not None:
        print_solution(node.parent)
        print(f'Move blank {node.action} -> Cost: {node.cost}')
        print_state(node.state)
        print('------------------')
    else:
        print('Initial State:')
        print_state(node.state)
        print('------------------')

def print_state(state):
    for row in state:
        print(row)
    print()

def solve_puzzle(initial_state, goal_state):
    initial_node = PuzzleNode(initial_state)
    goal_node = PuzzleNode(goal_state)

    open_set = [initial_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_node.state:
            print('Goal State Reached!')
            print_solution(current_node)
            return

        closed_set.add(tuple(map(tuple, current_node.state)))

        for neighbor in get_neighbors(current_node):
            if tuple(map(tuple, neighbor.state)) not in closed_set:
                heapq.heappush(open_set, neighbor)

    print('No solution found.')
initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solve_puzzle(initial_state, goal_state)
