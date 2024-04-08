# Read for the formulas in propositional calculus. Write a function that reads such a 
# formula and creates its binary tree representation. What is the complexity of your 
# function? 



class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parse_formula(formula):
    index = 0
    return _parse_expression(formula, index)

def _parse_expression(formula, index):
    node = None
    while index < len(formula):
        char = formula[index]
        if char == ' ':
            index += 1
            continue
        elif char == '(':
            index += 1
            sub_expression, index = _parse_expression(formula, index)
            node = sub_expression
        elif char == ')':
            return node, index + 1
        elif char.isalpha():
            node = TreeNode(char)
            index += 1
        elif char in ['&', '|', '!']:
            node = TreeNode(char)
            index += 1
            node.left, index = _parse_expression(formula, index)
            node.right, index = _parse_expression(formula, index)
            return node, index
    return node, index

def print_tree(root, level=0):
    if root is not None:
        print("  " * level + root.value)
        print_tree(root.left, level + 1)
        print_tree(root.right, level + 1)

# Example usage:

# Formula in propositional calculus
formula = "(A & (B | !C))"

# Create binary tree representation
root = parse_formula(formula)

# Print the tree
print("Binary Tree Representation:")
print_tree(root)

