"""
Longest Consecutive Sequence in an Array

Problem Statement: Given an array nums of n integers. Return the length of the 
longest sequence of consecutive integers. The integers in this sequence can 
appear in any order.

Approach: Use a set to store all elements. For each element, check if it's the 
start of a sequence (i-1 not in set), then count consecutive elements.
"""

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  

def long_con_sum(arr):
    st = set()
    max_cnt = 0
    for i in arr:
        st.add(i)
    for i in arr:
        cnt = 1
        if i-1 not in st:
           while i+1 in st:      
                cnt += 1
                i+=1
        max_cnt = max(cnt,max_cnt)
    return max_cnt

print(long_con_sum(nums))
