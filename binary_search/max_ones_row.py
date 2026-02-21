mat = [[0, 1, 1], [0, 0, 1], [0, 0, 0], [1, 1, 1]]

def minimum_ones(mat):
    n = len(mat)
    m = len(mat[0])
    count1 = 0
    idx = -1
    for i in range(n):
        l = 0
        r = m - 1
        while l <= r:
            mid = (l + r) // 2
            if mat[i][mid] == 1:
                if (m - mid) > count1:
                    count1 = m - mid
                    idx = i
                r = mid - 1
            else:
                l = mid + 1
    return idx

print(minimum_ones(mat))
