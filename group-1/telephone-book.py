# Consider telephone book database of N clients. Make use of a hash table implementation 
# to quickly look up client‘s telephone number.  Make use of two collision handling 
# techniques and compare them using number of comparisons required to find a set of 
# telephone numbers

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # Example hash function: simple modulo division
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = ListNode(key, value)
        else:
            node = self.table[index]
            while node.next:
                node = node.next
            node.next = ListNode(key, value)

    def search(self, key):
        index = self.hash_function(key)
        node = self.table[index]
        comparisons = 1
        while node:
            if node.key == key:
                return node.value, comparisons
            node = node.next
            comparisons += 1
        return None, comparisons

def test_collision_handling(technique):
    # Initialize hash table
    hash_table = HashTable(100)

    # Insert some entries
    entries = {"John": "12345", "Alice": "67890", "Bob": "54321", "Eve": "98765"}
    for key, value in entries.items():
        hash_table.insert(key, value)

    # Search for all entries and count comparisons
    total_comparisons = 0
    for key in entries.keys():
        value, comparisons = hash_table.search(key)
        print(f"Key: {key}, Value: {value}, Comparisons: {comparisons}")
        total_comparisons += comparisons

    print(f"Total comparisons using {technique}: {total_comparisons}")

# Test using separate chaining
print("Separate Chaining:")
test_collision_handling("Separate Chaining")

# Test using open addressing (linear probing)
print("\nOpen Addressing (Linear Probing):")
test_collision_handling("Open Addressing (Linear Probing)")

