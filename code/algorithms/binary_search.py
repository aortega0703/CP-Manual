def bs(q, arr):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == q:
            return m + 1
        elif arr[m] < q:
            l = m + 1
        else:
            r = m - 1
    return -1