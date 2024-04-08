# Given sequence k = k1 <k2 < … <kn of n sorted keys, with a search probability pi for each 
# key ki . Build the Binary search tree that has the least search cost given the access 
# probability for each key?  

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def optimal_bst(keys, probabilities):
    n = len(keys)
    cost = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        cost[i][i] = probabilities[i]

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            min_cost = float('inf')
            total_prob = sum(probabilities[i:j + 1])

            for k in range(i, j + 1):
                c = total_prob + (cost[i][k - 1] if k > i else 0) + (cost[k + 1][j] if k < j else 0)
                if c < min_cost:
                    min_cost = c
                    root = k
            cost[i][j] = min_cost

    root = construct_tree(keys, 0, n - 1, cost)
    return root


def construct_tree(keys, start, end, cost):
    if start > end:
        return None

    min_cost = float('inf')
    root_index = -1

    for i in range(start, end + 1):
        if cost[start][end] < min_cost:
            min_cost = cost[start][end]
            root_index = i

    root = Node(keys[root_index])

    root.left = construct_tree(keys, start, root_index - 1, cost)
    root.right = construct_tree(keys, root_index + 1, end, cost)

    return root


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.key)
        inorder_traversal(root.right)


# Example usage:
keys = [10, 12, 20, 25]
probabilities = [0.34, 0.32, 0.12, 0.22]

root = optimal_bst(keys, probabilities)

print("Inorder traversal of constructed BST:")
inorder_traversal(root)
