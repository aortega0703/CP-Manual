# Set bits are composite while unset bits are prime
def sieve(N):
    prime = 3 #0b11
    # Check divisibility by 2 separately
    p = 3
    while p**2 <= N:
        if prime[p]:
            # Skips all even numbers
            for kp in range(3*p, N+1, 2*p):
                # Setting bit kp
                prime |= 1 << kp
        p += 2
    return prime