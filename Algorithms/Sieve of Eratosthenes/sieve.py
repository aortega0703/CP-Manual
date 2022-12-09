# Set bits are composite while unset bits are prime
def sieve(N):
    prime = 3 #0b11
    p = 2
    while p**2 <= N:
        if prime[p]:
            for kp in range(2*p, N+1, p):
                # Setting bit kp
                prime |= 1 << kp
        p += 2
    return prime