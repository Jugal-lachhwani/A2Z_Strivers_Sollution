"""
Rearrange Array Elements by Sign

Problem Statement: There's an array 'A' of size 'N' with an equal number of 
positive and negative elements. Without altering the relative order of positive 
and negative elements, you must return an array of alternately positive and 
negative values.

Approach: Use two pointers (pp for positive positions starting at 0, np for 
negative positions starting at 1) to place elements alternately.
"""

arr = [1,2,-4,-5]
N = 4

def rearrange(arr,n):
    c = [0] * n
    
    pp = 0
    np = 1
    
    for i in range(len(arr)):
        if arr[i] > 0:
            c[pp] = arr[i]
            pp += 2
        else:
            c[np] = arr[i]
            np += 2
    return c

print(rearrange(arr,N))
