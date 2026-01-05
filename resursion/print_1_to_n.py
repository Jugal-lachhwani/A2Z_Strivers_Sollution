"""### Print 1 to N using Recursion

Problem Description: Given an integer N, write a program to print numbers from 1 to N.
"""

def print_no(N):
    if N < 1:
        return
    print_no(N-1)
    print(N)

print_no(6)