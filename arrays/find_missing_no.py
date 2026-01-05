"""### Find the missing number in an array

Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array..
"""

N,arr = 5,[1,2,4,5]

def find_miss_no(N,arr):
    s = set()
    
    for i in arr:
        s.add(i)
    
    for i in range(1,N+1):
        if i not in s:
            return i

find_miss_no(N,arr)