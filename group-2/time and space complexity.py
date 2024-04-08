# Convert given binary tree into threaded binary tree. Analyze time and space complexity 
# of the algorithm.  

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.threaded = False

def morris_traversal(root):
    if not root:
        return
    
    current = root
    while current:
        if not current.left:
            # If no left child, process current node and move to right
            print(current.data, end=" ")
            current = current.right
        else:
            # Find the in-order predecessor of current
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right

            # Make current as right child of its in-order predecessor
            if not pre.right:
                pre.right = current
                current = current.left
            else:
                # Revert the changes made in the 'if' block
                pre.right = None
                print(current.data, end=" ")
                current = current.right

def convert_to_threaded_binary_tree(root):
    morris_traversal(root)

# Example usage:

# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Convert the binary tree into a threaded binary tree
convert_to_threaded_binary_tree(root)

