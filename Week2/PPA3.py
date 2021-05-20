x1, y1, x2, y2, x3 = float(input()), float(input()), float(input()), float(input()), float(input())
if x2 == x1:
    print('Vertical Line', end='')
else:
    y3 = (((x3 - x1) * (y2 - y1)) / (x2 - x1)) + y1
    print(y3)
    m = (y2 - y1) / (x2 - x1)
    if m == 0:
        print('Horizontal Line', end='')
    elif m > 0:
        print('Positive Slope', end='')
    elif m < 0:
        print('Negative Slope', end='')
# Submission Successful! 4 out of 4 private test(s) passed.
