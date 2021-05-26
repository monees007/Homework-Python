def sum(n):
    return int(n * (n + 1) / 2)


x = 0
for i in range(1, int(input()) + 1):
    x += sum(i)

print(x, end='')

# Submission Successful! 4 out of 4 private test(s) passed.
