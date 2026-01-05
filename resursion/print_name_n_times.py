"""Problem Description: Given an integer N, write a program to print your name N times."""

def print_name(N):
    if N == 0:
        return
    print("Jugal")
    return print_name(N-1)

print_name(6)