def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def primes(x):
    z = []
    for i in range(2, x + 1):
        if isprime(i):
            z += [i]
    return z


x = int(input())
y = primes(x)

for i in y:
    if x % i == 0:
        x = x / i
        print(i)
# Submission Successful! 4 out of 4 private test(s) passed
