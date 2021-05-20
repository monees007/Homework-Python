x, y = float(input()), float(input())
if x == 0 and y == 0:
    print('Origin', end='')
elif x == 0:
    print('Y-axis', end='')
elif y == 0:
    print('X-axis', end='')
else:
    if x > 0 and y > 0:
        print('I', end='')
    if x > 0 > y:
        print('IV', end='')
    if x < 0 < y:
        print('II', end='')
    if x < 0 and y < 0:
        print('III', end='')
# Submission Successful! 7 out of 7 private test(s) passed.
