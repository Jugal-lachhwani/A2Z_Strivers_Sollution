"""Print Fibonacci Series up to Nth term

Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.
"""


def fibonacci(n):
    if n < 2:
        return n
    if l[n] != 0:
        return l[n]
    l[n] = fibonacci(n-1) + fibonacci(n-2)
    return l[n]

n = 15
l = [0] * n
fibonacci(n-1)