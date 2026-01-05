"""## Rotate array by K elements

Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.
"""

l,k,d = [1, 2, 3, 4, 5, 6, 7], 2 , 'left'

def rotate(l,k,d):
    if not k:
        return l
    if d == 'right':
        l = l[::-1]
        l = l[k-1::-1] + l[:k-1:-1]
    else:
        l = l[k-1::-1] + l[:k-1:-1]
        l = l[::-1]
            
            
    return l

rotate(l,k,d)
