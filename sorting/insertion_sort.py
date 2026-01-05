"""
In each iteration, select an element from the unsorted part of the array using an outer loop.

Place this selected element in its correct position within the sorted part of the array.
Use an inner loop to shift the remaining elements, if necessary, to accommodate the selected element. This involves shifting elements by one position until the selected element can be placed in the correct position.

Continue this process until the entire array is sorted.
"""

for i in range(1,len(l)):
    while i > 0 and l[i] < l[i-1]:
        (l[i-1],l[i]) = (l[i],l[i-1])
        i -= 1
print(l)