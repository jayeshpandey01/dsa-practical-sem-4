# Beginning with an empty binary search tree, Construct binary search tree by inserting the 
# values in the order given. After constructing a binary tree -  
# i. Insert new node  
# ii. Find number of nodes in longest path from root 
# iii. Minimum data value found in the tree  
# iv. Change a tree so that the roles of the left and right pointers are swapped at every 
# node  
# v. Search a value  

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.data:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def find_longest_path(self):
        return self._find_longest_path_recursive(self.root)

    def _find_longest_path_recursive(self, node):
        if node is None:
            return 0
        else:
            left_height = self._find_longest_path_recursive(node.left)
            right_height = self._find_longest_path_recursive(node.right)
            return max(left_height, right_height) + 1

    def minimum_value(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def swap_pointers(self):
        self._swap_pointers_recursive(self.root)

    def _swap_pointers_recursive(self, node):
        if node is not None:
            node.left, node.right = node.right, node.left
            self._swap_pointers_recursive(node.left)
            self._swap_pointers_recursive(node.right)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.data == value:
            return node
        elif value < node.data:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)


# Example usage:

# Constructing a binary search tree
bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)

# i. Insert new node
bst.insert(55)

# ii. Find number of nodes in longest path from root
print("Number of nodes in longest path from root:", bst.find_longest_path())

# iii. Minimum data value found in the tree
print("Minimum data value found in the tree:", bst.minimum_value())

# iv. Change a tree so that the roles of the left and right pointers are swapped at every node
bst.swap_pointers()

# v. Search a value
search_value = 60
result = bst.search(search_value)
if result:
    print(f"Value {search_value} found in the tree.")
else:
    print(f"Value {search_value} not found in the tree.")

