class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def minimax(node, depth, is_maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value

    if is_maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


# Example usage:
if __name__ == "__main__":
    # Creating a simple tree structure
    root = Node(3)
    root.children = [Node(5), Node(6), Node(2)]

    root.children[0].children = [Node(9), Node(1)]
    root.children[1].children = [Node(12)]
    root.children[2].children = [Node(8), Node(7)]

    # Define the depth of the search
    depth = 2

    # Applying the Minimax algorithm
    result = minimax(root, depth, True)
    print("Best decision value:", result)
