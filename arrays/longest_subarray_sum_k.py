"""
Longest Subarray with Sum K

Problem Statement: Given an array of integers and a target sum k, find the 
length of the longest subarray with sum equal to k.

Approach: Use sliding window with two pointers. Expand window by moving j, 
shrink by moving i when sum exceeds k.
"""

arr = [3, 1, 2, 4, 2]
k = 6

def count_subarrs(arr,k):
    cnt = 0
    j = 0
    i = 0
    sum = arr[0]
    maxlen = 0
    while j < len(arr):     
        while i < j and sum > k:
            sum -= arr[i]
            i+=1       
        if sum == k:
            l = j-i
            maxlen = max(l,maxlen)      
        j+=1
        if j < len(arr):
            sum += arr[j]
    return maxlen

print(count_subarrs(arr,k))
