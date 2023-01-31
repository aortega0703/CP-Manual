# N must be odd and > 2, if unsure check those cases
def miller_test(N):
    s = 0
    d = N-1
    while d % 2 == 0: # n-1 = d * 2^s
        s += 1
        d //= 2
    # For unknown (or unbounded) values of n, use
    # a = [2, min(n-2, 2 * ln(n)^2))]
    # If a is chosen randomly it becomes the Miller-Rabin test
    for a in [2, 3, 5, 7]:
        x = a**d % N
        for _ in range(s):
            y = x**2 % N
            # nontrivial square root of 1 modulo n
            if y == 1 and x != 1 and x != N-1:
                # Can be replaced with gcd(x - 1, N)
                # to return a divisor of N
                return False
            x = y
        if y != 1:
            return False
    return True
