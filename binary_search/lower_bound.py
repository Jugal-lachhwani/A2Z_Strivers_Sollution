l = [1, 3]

def lower_bond(arr, target):
    l = 0
    r = len(arr) - 1
    min_ind = len(arr)
    f = False
    while l <= r:
        mid = (r + l) // 2
        x = arr[mid] - target
        if x < 0:
            l = mid + 1
        elif x >= 0:
            min_ind = min(min_ind, mid)
            r = mid - 1
            if x == 0:
                f = True
    l = 0
    r = len(arr) - 1
    max_ind = 0
    while l <= r:
        mid = (r + l) // 2
        x = arr[mid] - target
        if x <= 0:
            max_ind = max(max_ind, mid)
            l = mid + 1
        elif x > 0:
            min_ind = min(min_ind, mid)
            r = mid - 1
    if f:
        return min_ind, max_ind
    else:
        return -1

print(lower_bond(l, 2))
