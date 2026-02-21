l = [3, 3, 5, 5]

def greatest_and_smallest(arr, target):
    l = 0
    r = len(arr) - 1
    max_ind = len(arr)
    while l <= r:
        mid = (r + l) // 2
        x = arr[mid] - target
        if x > 0:
            max_ind = min(max_ind, mid)
            r = mid - 1
        elif x == 0:
            return arr[mid], arr[mid]
        else:
            l = mid + 1
    if max_ind == len(arr):
        return arr[max_ind - 1], -1
    if max_ind > 0:
        return arr[max_ind - 1], arr[max_ind]
    return -1, arr[max_ind]

print(greatest_and_smallest(l, 0))
