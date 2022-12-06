def delta(D):
    A = k = 0
    for i in range(1, D[-1][0]): # 0 < i < g
        if i == D[k][0]:
            k += 1
        for j in range(i, D[k][1]): # 0 < j < n/g = h
            A |= 1 << i*j # Adds new number
    return A.bit_count()