# Implement all the functions of a dictionary (ADT) using hashing and handle collisions 
# using chaining with / without replacement.  
# Data: Set of (key, value) pairs, Keys are mapped to values, Keys must be comparable, Keys 
# must be unique  
# Standard Operations: Insert(key, value), Find(key), Delete(key)  

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)

    def find(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        previous = None
        while current is not None:
            if current.key == key:
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next

class ChainingHashTableWithReplacement(ChainingHashTable):
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            # Replace the value if key already exists
            current = self.table[index]
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            # If key doesn't exist, insert at the end of the chain
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node

# Test the implementations
def test_chaining():
    # Test without replacement
    print("Testing Chaining Hash Table without replacement:")
    hash_table = ChainingHashTable(10)
    hash_table.insert("apple", 10)
    hash_table.insert("banana", 20)
    hash_table.insert("orange", 30)

    print("Find 'apple':", hash_table.find("apple"))
    print("Find 'banana':", hash_table.find("banana"))
    print("Find 'orange':", hash_table.find("orange"))

    hash_table.delete("banana")
    print("Find 'banana' after deletion:", hash_table.find("banana"))

def test_chaining_with_replacement():
    # Test with replacement
    print("\nTesting Chaining Hash Table with replacement:")
    hash_table = ChainingHashTableWithReplacement(10)
    hash_table.insert("apple", 10)
    hash_table.insert("banana", 20)
    hash_table.insert("orange", 30)

    print("Find 'apple':", hash_table.find("apple"))
    print("Find 'banana':", hash_table.find("banana"))
    print("Find 'orange':", hash_table.find("orange"))

    # Inserting duplicate key should replace the existing value
    hash_table.insert("banana", 40)
    print("Find 'banana' after replacement:", hash_table.find("banana"))

test_chaining()
test_chaining_with_replacement()

