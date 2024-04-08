# Read the marks obtained by students of second year in an online examination of 
# particular subject. Find out maximum and minimum marks obtained in that subject. Use 
# heap data structure. Analyze the algorithm.

import heapq

def find_max_min_marks(marks):
    max_heap = []
    min_heap = []

    # Insert marks into both max-heap and min-heap
    for mark in marks:
        heapq.heappush(max_heap, -mark)  # Use negative to simulate max-heap behavior
        heapq.heappush(min_heap, mark)

    # Get maximum and minimum marks
    max_mark = -heapq.heappop(max_heap)
    min_mark = heapq.heappop(min_heap)

    return max_mark, min_mark

# Example usage:
marks = [90, 85, 92, 88, 78, 95, 80]
max_mark, min_mark = find_max_min_marks(marks)
print("Maximum mark:", max_mark)
print("Minimum mark:", min_mark)
