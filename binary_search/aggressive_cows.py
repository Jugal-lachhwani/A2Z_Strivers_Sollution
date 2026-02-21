arr = [0, 3, 4, 7, 10]
k = 4

def find_min_stalls(arr, k, mid):
    c_k = 1
    last_pos = arr[0]
    for i in range(1, len(arr)):
        if abs(arr[i] - last_pos) >= mid:
            c_k += 1
            last_pos = arr[i]
    return c_k >= k


def aggresive_cows(arr, k):
    l = 0
    r = len(arr)
    min_dist = max(arr)
    
    while l <= r:
        mid = (l + r) // 2
        can_place = find_min_stalls(arr, k, mid)
        if can_place:
            l = mid + 1
            min_dist = mid
        else:
            r = mid - 1
    return min_dist

print(aggresive_cows(arr, k))
