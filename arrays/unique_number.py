"""
Find the number that appears once, and the other numbers twice

Problem Statement: Given a non-empty array of integers arr, every element 
appears twice except for one. Find that single one.

Approach: Use XOR operation. XOR of two same numbers is 0, and XOR of a number 
with 0 is the number itself. So XORing all numbers will cancel out duplicates.
"""

arr = [2,2,1,3,4,3,4]

def uni_num(arr):
    xor = 0
    for i in arr:
        xor ^= i
    return xor

print(uni_num(arr))
