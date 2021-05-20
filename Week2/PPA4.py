x = input()

if len(x) % 2 == 0:
    if x[-1] == '.':
        x = x[0:len(x) - 2]
    else:
        x += '.'

y = x[len(x) // 2 - 1] + x[len(x) // 2] + x[len(x) // 2 + 1]
print(y, end='')

# Submission Successful! 4 out of 4 private test(s) passed.
