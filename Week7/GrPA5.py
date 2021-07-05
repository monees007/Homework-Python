def collatz(n):
    '''
    :param n: integers
    :return: integers
    '''
    if n % 2 == 0:
        y = n / 2
    else:
        y = 3 * n + 1
    return y


def collatz_repeat(n):
    count = 0
    while n != 1:
        count += 1
        n = collatz(n)
    return count

# Submission Successful! 4 out of 4 private test(s) passed.
