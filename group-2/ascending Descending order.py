# A Dictionary stores keywords & its meanings. Provide facility for adding new keywords, 
# deleting keywords, updating values of any entry. Provide facility to display whole data 
# sorted in ascending/ Descending order. Also find how many maximum comparisons may 
# require for finding any keyword. Use Binary Search Tree for implementation.  


class TreeNode:
    def __init__(self, keyword, meaning):
        self.keyword = keyword
        self.meaning = meaning
        self.left = None
        self.right = None

class DictionaryBST:
    def __init__(self):
        self.root = None

    def insert(self, keyword, meaning):
        self.root = self._insert_recursive(self.root, keyword, meaning)

    def _insert_recursive(self, node, keyword, meaning):
        if not node:
            return TreeNode(keyword, meaning)
        if keyword < node.keyword:
            node.left = self._insert_recursive(node.left, keyword, meaning)
        elif keyword > node.keyword:
            node.right = self._insert_recursive(node.right, keyword, meaning)
        else:
            node.meaning = meaning
        return node

    def delete(self, keyword):
        self.root = self._delete_recursive(self.root, keyword)

    def _delete_recursive(self, node, keyword):
        if not node:
            return node

        if keyword < node.keyword:
            node.left = self._delete_recursive(node.left, keyword)
        elif keyword > node.keyword:
            node.right = self._delete_recursive(node.right, keyword)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            successor = self._min_value_node(node.right)
            node.keyword = successor.keyword
            node.meaning = successor.meaning
            node.right = self._delete_recursive(node.right, successor.keyword)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def update(self, keyword, meaning):
        node = self._search_recursive(self.root, keyword)
        if node:
            node.meaning = meaning

    def search(self, keyword):
        node = self._search_recursive(self.root, keyword)
        return node.meaning if node else None

    def _search_recursive(self, node, keyword):
        while node:
            if keyword == node.keyword:
                return node
            elif keyword < node.keyword:
                node = node.left
            else:
                node = node.right
        return None

    def inorder_traversal(self):
        sorted_keywords = []
        self._inorder_traversal_recursive(self.root, sorted_keywords)
        return sorted_keywords

    def _inorder_traversal_recursive(self, node, sorted_keywords):
        if node:
            self._inorder_traversal_recursive(node.left, sorted_keywords)
            sorted_keywords.append((node.keyword, node.meaning))
            self._inorder_traversal_recursive(node.right, sorted_keywords)

    def max_comparisons(self):
        return self._max_comparisons_recursive(self.root)

    def _max_comparisons_recursive(self, node):
        if not node:
            return 0
        return 1 + max(self._max_comparisons_recursive(node.left), self._max_comparisons_recursive(node.right))


# Example usage:

# Create a dictionary
dictionary = DictionaryBST()

# Add keywords and meanings
dictionary.insert("apple", "a fruit")
dictionary.insert("banana", "another fruit")
dictionary.insert("carrot", "a vegetable")

# Update a keyword meaning
dictionary.update("apple", "a delicious fruit")

# Delete a keyword
dictionary.delete("banana")

# Display sorted data
sorted_data = dictionary.inorder_traversal()
print("Sorted data (Ascending Order):", sorted_data)

# Display sorted data in descending order
sorted_data_descending = sorted(sorted_data, reverse=True)
print("Sorted data (Descending Order):", sorted_data_descending)

# Find maximum comparisons
max_comparisons = dictionary.max_comparisons()
print("Maximum comparisons:", max_comparisons)

