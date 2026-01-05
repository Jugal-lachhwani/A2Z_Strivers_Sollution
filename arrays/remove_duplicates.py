"""### Remove Duplicates in-place from Sorted Array

Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

Examples

Input: arr[]=[1,1,2,2,2,3,3]

Output: [1,2,3,_,_,_,_]

Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.
"""

arr = [1,1,2,2,2,3,3]

def remove_duplicates(arr):
    if not arr:
        return
    non_d = arr[0]
    for i in range(1,len(arr)):
        if arr[i] == non_d:
            arr[i] = "_"
        else:
            non_d = arr[i]
    p = arr[0]
    b = 1
    for i in range(1,len(arr)):
        if arr[i] != "_":
            arr[i],arr[b] = arr[b],arr[i]
            b+=1
        
    return arr

remove_duplicates(arr)        