T = int(input())
if 0 > T or T >= 24:
    print('INVALID', end='')
elif 0 <= T <= 5:
    print('NIGHT', end='')
elif 6 <= T <= 11:
    print('MORNING', end='')
elif 12 <= T <= 17:
    print('AFTERNOON', end='')
elif 18 <= T <= 23:
    print('EVENING', end='')
# Submission Successful! 5 out of 5 private test(s) passed.
