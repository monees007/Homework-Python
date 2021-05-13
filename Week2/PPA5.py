a, b, c = input(), input(), input()


def tobool(x):
    if x == 'True':
        return True
    else:
        return False


a, b, c = tobool(a), tobool(b), tobool(c)

if a:
    if b:
        if c:
            print(True)
        else:
            print(False)
    else:
        print(True)
else:
    if b:
        if c:
            print(True)
        else:
            print(False)
    else:
        if c:
            print(True)
        else:
            print(False)

# Submission Successful! 8 out of 8 private test(s) passed.
