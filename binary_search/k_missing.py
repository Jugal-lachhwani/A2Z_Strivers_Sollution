vec = [4, 7, 9, 10]

def k_missing(arr, k):
    l = 0
    r = len(arr) - 1
    
    while l <= r:
        mid = (l + r) // 2
        mis = arr[mid] - mid + 1
        if mis < k:
            l = mid + 1
        else:
            r = mid - 1
    
    return k + r + 1
