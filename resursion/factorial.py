"""### Factorial of a Number : Iterative and Recursive

Problem Statement: Given a number X,  print its factorial.

To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.

Note: X  is always a positive number. 
"""

def factorial(N):
    if N < 2:
        return 1
    return N*factorial(N-1)

print(factorial(5))