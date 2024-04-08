# For given set of elements create skip list. Find the element in the set that is closest to 
# some given value.  (note: Decide the level of element in the list Randomly with some 
# upper limit) 

import random

class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = self.create_node(float('-inf'), max_level)

    def create_node(self, value, level):
        return Node(value, level)

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.head
        for i in range(self.max_level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        level = self.random_level()
        new_node = self.create_node(value, level)
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def find_closest(self, value):
        current = self.head
        for i in range(self.max_level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        return current.forward[0].value if current.forward[0] else None

# Test the implementation
def test_skip_list():
    elements = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    value = 16

    skip_list = SkipList(max_level=3)
    for element in elements:
        skip_list.insert(element)

    closest_element = skip_list.find_closest(value)
    print(f"The element in the set closest to {value} is: {closest_element}")

test_skip_list()

