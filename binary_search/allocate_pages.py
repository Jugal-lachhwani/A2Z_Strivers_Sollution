l = [25, 46, 28, 49, 24]
m = 4

def can_allocate(l, m, mid):
    sum_pages = 0
    m = m - 1
    for pages in l:
        sum_pages += pages
        if sum_pages > mid:
            m -= 1
            sum_pages = pages
    return m >= 0


def find_min_pages(arr, m):
    if m > len(arr):
        return -1
    l = min(arr)
    r = sum(arr)
    min_page = max(arr)
    while l <= r:
        mid = (l + r) // 2
        if can_allocate(arr, m, mid):
            min_page = mid
            r = mid - 1
        else:
            l = mid + 1
    return min_page

print(find_min_pages(l, m))
