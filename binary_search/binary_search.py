l = [1, 4, 7, 8, 12]

def binary_search(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (r - l) // 2
        if arr[mid] > target:
            r = mid - 1
        elif target > arr[mid]:
            l = mid + 1
        else:
            return mid
    return -1

print(binary_search(l, 1))
