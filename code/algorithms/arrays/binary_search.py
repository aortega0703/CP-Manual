def bs(q, L):
    l = 0
    r = len(L) - 1
    while l <= r:
        m = (l + r) // 2
        if L[m] == q:
            return m
        elif L[m] < q:
            l = m + 1
        else:
            r = m - 1
    return -1