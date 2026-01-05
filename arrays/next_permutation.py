"""
next_permutation: find next lexicographically greater permutation

Problem Statement: Given an array Arr[] of integers, rearrange the numbers of 
the given array into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange to the lowest possible 
order (i.e., sorted in ascending order).

Approach: 
1. Find the break point (index where arr[i] > arr[i-1] from right)
2. Find the next greater element and swap
3. Reverse the right half
"""

arr = [2,3,1]

def next_permutation(arr):
    index = -1
    for i in range(len(arr)-1,0,-1):
        if arr[i] > arr[i-1]:
            index = i-1
            break
    if index == -1:
        return arr[::-1]        
    for i in range(len(arr)-1,index,-1):
        if arr[i] > arr[index]:
            arr[i],arr[index] = arr[index],arr[i]
            break
    arr[index + 1:] = reversed(arr[index + 1:])
    return arr

print(next_permutation(arr))
