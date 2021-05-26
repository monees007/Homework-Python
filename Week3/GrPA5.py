def four(x):
    for i in range(10):
        if x.count(x[i]) < 8:
            return True
        else:
            return False


def three(x):
    a = 0
    for i in range(1, len(x)):
        if x[i] == x[i - 1]:
            a += 1
            if a > 7:
                return False
        else:
            a = 0
    return True


x = input()
if int(x[0]) in range(6, 10):
    if len(x) == 10:
        if four(x):
            if three(x):
                if x.isdigit():
                    print('valid', end='')
                else:print('invalid', end='')
            else:print('invalid', end='')
        else:print('invalid', end='')
    else:print('invalid', end='')
else:print('invalid', end='')

# Submission Successful! 6 out of 6 private test(s) passed.

