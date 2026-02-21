l = [1, 5, 6]

def upper_bond(arr, target):
    l = 0
    r = len(arr) - 1
    max_idx = 0
    while l <= r:
        mid = (r + l) // 2
        x = arr[mid] - target
        if x >= 0:
            max_idx = max(max_idx, mid)
            l = mid + 1
        else:
            r = mid - 1
    return max_idx

print(upper_bond(l, 2))
