"""### Quick Sort Algorithm

Problem Statement: Given an array of n integers, sort the array using the Quicksort method.

"""

arr = [4,1,7,9,3,5,6,2,1]

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    m = arr[0]
    b = 1
    for i in range(1,len(arr)):
        if arr[i] <= m:
            arr[b],arr[i] = arr[i],arr[b]
            b+=1
    arr[b-1],arr[0] = arr[0],arr[b-1]
    left = quick_sort(arr[0:b-1])
    right = quick_sort(arr[b:])
    
    return left + [m] + right
            
quick_sort(arr)