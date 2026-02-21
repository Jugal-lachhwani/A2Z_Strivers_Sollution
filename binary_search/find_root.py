n = 26

def find_root(n, o):
    l = 1
    r = n
    while l <= r:
        mid = (r + l) // 2
        num = mid ** o
        print("l=", l, "r=", r, "mid=", mid)
        if num > n:
            r = mid - 1
        elif num < n:
            l = mid + 1
        else:
            return mid
    return -1

print(find_root(n, 3))
