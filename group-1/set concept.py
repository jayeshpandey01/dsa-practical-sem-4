# To create ADT that implement the "set" concept.  
# a. Add (newElement) -Place a value into the set  
# b. Remove (element) Remove the value  
# c. Contains (element) Return true if element is in collection  
# d. Size () Return number of values in collection Iterator () Return an iterator used to loop 
# over collection  
# e. Intersection of two sets  
# f. Union of two sets  
# g. Difference between two sets  
# h.Subset 


class SetADT:
    def __init__(self):
        self.elements = []

    def add(self, new_element):
        if new_element not in self.elements:
            self.elements.append(new_element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def contains(self, element):
        return element in self.elements

    def size(self):
        return len(self.elements)

    def iterator(self):
        return iter(self.elements)

    def intersection(self, other_set):
        intersection_set = SetADT()
        for element in self.elements:
            if element in other_set.elements:
                intersection_set.add(element)
        return intersection_set

    def union(self, other_set):
        union_set = SetADT()
        for element in self.elements:
            union_set.add(element)
        for element in other_set.elements:
            union_set.add(element)
        return union_set

    def difference(self, other_set):
        difference_set = SetADT()
        for element in self.elements:
            if element not in other_set.elements:
                difference_set.add(element)
        return difference_set

    def subset(self, other_set):
        for element in self.elements:
            if element not in other_set.elements:
                return False
        return True

# Test the implementation
def test_set_adt():
    set1 = SetADT()
    set1.add(1)
    set1.add(2)
    set1.add(3)

    set2 = SetADT()
    set2.add(3)
    set2.add(4)
    set2.add(5)

    print("Set 1:", list(set1.iterator()))
    print("Set 2:", list(set2.iterator()))

    print("Intersection:", list(set1.intersection(set2).iterator()))
    print("Union:", list(set1.union(set2).iterator()))
    print("Difference:", list(set1.difference(set2).iterator()))

    print("Set 1 is subset of Set 2:", set1.subset(set2))
    print("Set 2 is subset of Set 1:", set2.subset(set1))

test_set_adt()

