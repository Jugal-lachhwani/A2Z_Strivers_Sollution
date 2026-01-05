"""### Count Maximum Consecutive One's in the array

Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array..
"""

arr = [1, 1, 0, 1, 1, 1,1,1,0,0,1,1]

def count_con_1(arr):
    count = 0
    max_count = 0
    for i in arr:
        if i == 1:
            count += 1
            max_count = max(max_count,count)
        else:
            count = 0
            
    return max_count

count_con_1(arr)