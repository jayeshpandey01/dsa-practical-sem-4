# A Dictionary stores keywords & its meanings. Provide facility for adding new keywords, 
# deleting keywords, updating values of any entry. Provide facility to display whole data 
# sorted in ascending/ Descending order. Also find how many maximum comparisons may 
# require for finding any keyword. Use Height balance tree and find the complexity for 
# finding a keyword 

class AVLNode:
    def __init__(self, keyword, meaning):
        self.keyword = keyword
        self.meaning = meaning
        self.left = None
        self.right = None
        self.height = 1

class AVLDictionary:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        t = x.right

        x.right = y
        y.left = t

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        t = y.left

        y.left = x
        x.right = t

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, node, keyword, meaning):
        if node is None:
            return AVLNode(keyword, meaning)

        if keyword < node.keyword:
            node.left = self.insert(node.left, keyword, meaning)
        elif keyword > node.keyword:
            node.right = self.insert(node.right, keyword, meaning)
        else:
            node.meaning = meaning
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.balance(node)

        if balance > 1:
            if keyword < node.left.keyword:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if keyword > node.right.keyword:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def add_keyword(self, keyword, meaning):
        self.root = self.insert(self.root, keyword, meaning)

    def delete(self, node, keyword):
        if node is None:
            return node

        if keyword < node.keyword:
            node.left = self.delete(node.left, keyword)
        elif keyword > node.keyword:
            node.right = self.delete(node.right, keyword)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.min_value_node(node.right)
            node.keyword = temp.keyword
            node.meaning = temp.meaning
            node.right = self.delete(node.right, temp.keyword)

        if node is None:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.balance(node)

        if balance > 1:
            if self.balance(node.left) >= 0:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if self.balance(node.right) <= 0:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def remove_keyword(self, keyword):
        self.root = self.delete(self.root, keyword)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def update(self, keyword, meaning):
        node = self.find_node(self.root, keyword)
        if node:
            node.meaning = meaning
        else:
            print("Keyword not found")

    def find_node(self, node, keyword):
        if node is None or node.keyword == keyword:
            return node

        if keyword < node.keyword:
            return self.find_node(node.left, keyword)

        return self.find_node(node.right, keyword)

    def inorder_traversal(self, node, sorted_list):
        if node:
            self.inorder_traversal(node.left, sorted_list)
            sorted_list.append((node.keyword, node.meaning))
            self.inorder_traversal(node.right, sorted_list)

    def ascending_order(self):
        sorted_list = []
        self.inorder_traversal(self.root, sorted_list)
        return sorted_list

    def descending_order(self):
        sorted_list = []
        self.inorder_traversal(self.root, sorted_list)
        return sorted_list[::-1]

    def search_keyword(self, keyword):
        comparisons = 0
        current = self.root
        while current:
            comparisons += 1
            if current.keyword == keyword:
                return comparisons
            elif keyword < current.keyword:
                current = current.left
            else:
                current = current.right
        return comparisons


# Example usage:
dictionary = AVLDictionary()
dictionary.add_keyword("apple", "a fruit")
dictionary.add_keyword("banana", "another fruit")
dictionary.add_keyword("zebra", "an animal")
dictionary.add_keyword("cat", "a pet")

print("Ascending order:")
print(dictionary.ascending_order())

print("Descending order:")
print(dictionary.descending_order())

print("Search for 'banana' required", dictionary.search_keyword("banana"), "comparisons.")
print("Search for 'zebra' required", dictionary.search_keyword("zebra"), "comparisons.")

dictionary.remove_keyword("banana")

print("After deleting 'banana', ascending order:")
print(dictionary.ascending_order())
