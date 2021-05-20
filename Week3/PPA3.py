def is_prime(x):
    """
    print sum of all prime numbers till input
    """
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True


y = int(input())
o, p = 0, []
for i in range(2, y + 1):
    if is_prime(i):
        o += i
print(o, end='')

# Submission Successful! 3 out of 3 private test(s) passed.
