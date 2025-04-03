def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return False
    return True

def lpf(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if isPrime(i):
                if isPrime(n/i):
                    return(n/i)
                else:
                    return(lpf(n/i))

n = 600851475143
print(lpf(n))