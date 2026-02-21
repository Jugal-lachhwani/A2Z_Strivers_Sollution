s = "(1)+((2))+(((3)))"

def parenthesis_depth(s):
    count = 0
    max_count = -1
    for i in s:
        if i == "(":
            count += 1
            max_count = max(max_count, count)
        elif i == ")":
            count -= 1
    
    return max_count

print(parenthesis_depth(s))
