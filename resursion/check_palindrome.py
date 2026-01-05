"""
Check if the given String is Palindrome or not

Problem Statement: Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.
"""

str = "ABCDCBA"

def check_palindrome(st):
    if len(st) < 2:
        return True
    if st[0] != st[len(st)-1]:
        return False
    return check_palindrome(st[1:(len(st)-1)])

print(check_palindrome(str))