"""
Sort an array of 0s, 1s and 2s

Problem Statement: Given an array nums consisting of only 0, 1, or 2. Sort the 
array in non-decreasing order. The sorting must be done in-place, without making 
a copy of the original array.

Approach: Dutch National Flag algorithm using three pointers (low, mid, high).
"""

nums = [1,1,2,0,0]

def sort_array(arr):
    j = 0
    i = 0
    high = len(arr) - 1
    while i <= high:
        if arr[i] == 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1
    return arr

print(sort_array(nums))
