"""### Sum of first N Natural Numbers

Problem Statement: Given a number ‘N’, find out the sum of the first N natural numbers .
"""

def sum_nums(N,sum):
    if N < 1:
        return sum
    sum += N
    return sum_nums(N-1,sum)
    
sum_nums(6,0)