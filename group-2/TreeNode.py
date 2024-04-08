# A book consists of chapters, chapters consist of sections and sections consist of 
# subsections. Construct a tree and print the nodes. Find the time and space requirements 
# of your method.  

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_expression_tree(prefix_expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in reversed(prefix_expression):
        if char in operators:
            node = TreeNode(char)
            node.left = stack.pop()
            node.right = stack.pop()
            stack.append(node)
        else:
            stack.append(TreeNode(char))

    return stack.pop()

def postorder_traversal(root):
    result = []
    stack = []
    current = root

    while True:
        while current:
            if current.right:
                stack.append(current.right)
            stack.append(current)
            current = current.left

        if not stack:
            break

        current = stack.pop()

        if current.right and stack and current.right == stack[-1]:
            stack.pop()
            stack.append(current)
            current = current.right
        else:
            result.append(current.value)
            current = None

    return result

def delete_tree(root):
    if root:
        delete_tree(root.left)
        delete_tree(root.right)
        root = None

# Prefix expression
prefix_expression = "+--a*bc/def"

# Construct expression tree
expression_tree = construct_expression_tree(prefix_expression)

# Traverse the expression tree using postorder traversal (non-recursive)
postorder_result = postorder_traversal(expression_tree)
print("Postorder Traversal:", ''.join(postorder_result))

# Delete the entire tree
delete_tree(expression_tree)

