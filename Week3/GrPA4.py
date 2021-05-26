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


x = input()
y = primes(len(x))
for i in y:
    print(x[i])

# Submission Successful! 3 out of 3 private test(s) passed.