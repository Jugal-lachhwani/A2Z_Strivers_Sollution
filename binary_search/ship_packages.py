weights = [1, 2, 3, 4, 5]
d = 2

def daysNeeded(weights, capacity):
    days = 1
    currentLoad = 0
    for w in weights:
        if currentLoad + w > capacity:
            days += 1
            currentLoad = w
        else:
            currentLoad += w
    return days


def min_weights(arr, d):
    l = 1
    r = sum(arr)
    ans = sum(arr)
    
    while l <= r:
        mid = (l + r) // 2
        c_d = daysNeeded(arr, mid)
        print(l, r, mid, c_d)
        if c_d <= d:
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1
    return ans

print(min_weights(weights, d))
