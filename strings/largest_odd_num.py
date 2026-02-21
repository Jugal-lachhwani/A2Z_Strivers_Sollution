s = "0214638"

def largest_odd_num(s):
    start = -1
    for i in range(len(s)):
        if s[i] != "0":
            start = i
            break
    if start == -1:
        return ""
    end = len(s)
    for i in range(len(s)-1,-1,-1):
        if int(s[i]) % 2 != 0:
            end = i
            break
    
    if end == len(s):
        return ""
    
    return s[start:end+1]

print(largest_odd_num(s))
