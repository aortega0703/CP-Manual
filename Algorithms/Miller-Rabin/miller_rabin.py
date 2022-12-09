def miller_rabin(N):
    if N == 2:
        return True
    if N % 2 == 0 or N < 2:
        return False
    
    s = 0
    d = N-1
    while d % 2 == 0: # n-1 = d * 2^s
        s += 1
        d //= 2
    # For unknown (or unbounded) values of n, use
    # a = [2, min(n − 2, floor(2*ln(n)^2))]
    for a in [2, 3, 5, 7, 11, 13, 17]:
        x = a**d % N
        for _ in range(s):
            y = x**2 % N
            # nontrivial square root of 1 modulo n
            if y == 1 and x != 1 and x != N-1:
                return False
            x = y
        if y != 1:
            return False
    return True
