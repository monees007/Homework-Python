def box(h, p, b):
    if (h * h) == (p * p) + (b * b):
        print('YES', end='')
    else:
        print('NO', end='')


a, b, c = int(input()), int(input()), int(input())
if a < b:
    if b < c:
        box(c, a, b)
    else:
        box(b, a, c)
if a > b:
    if a > c:
        box(a, b, c)
    else:
        box(c, a, b)

# Submission Successful! 5 out of 5 private test(s) passed.
