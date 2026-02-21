import math

N = [25, 12, 8, 14, 19]
h = 5

def calculate_k(arr, num):
    sum = 0
    for i in arr:
        sum += math.ceil(i / num)
    return sum


def koko(arr, h):
    l = 0
    r = max(arr)
    k = max(arr)
    
    while l <= r:
        mid = (l + r) // 2
        h_curr = calculate_k(arr, mid)
        print(l, r, mid, h_curr, k)
        if h_curr <= h:
            r = mid - 1
            k = min(k, mid)
        else:
            l = mid + 1
    return k


print(koko(N, h))
