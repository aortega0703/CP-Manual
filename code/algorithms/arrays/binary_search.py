def bs_leftmost(q, L):
    l = 0
    r = len(L) - 1
    while l < r:
        m = (l + r) // 2
        if L[m] < q:
            l = m + 1
        else:
            r = m
    return l

def bs_rightmost(q, L):
    l = 0
    r = len(L) - 1
    while l < r:
        m = (l + r) // 2
        if L[m] > q:
            r = m
        else:
            l = m + 1
    return r - 1