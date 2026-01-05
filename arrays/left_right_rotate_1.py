"""Left and Right Rotate the Array by One

Problem Statement: Given an integer array nums, rotate the array to the left by one.
"""

arr = [1, 2, 3, 4, 5] 

def left_rotate(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
        
    arr[len(arr) - 1] = temp
    
    return arr

left_rotate(arr)

