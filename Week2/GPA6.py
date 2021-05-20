def chksymb(y):
    for i in ['/', "\\", '=', '\"', '\'', ' ']:
        for j in y:
            if i == j:
                return False
    return True


x = str(input())
if 7 < len(x) < 33:
    if x[0].isalnum():
        if chksymb(x):
            print(True, end='')
        else:
            print(False, end='')
else:
    print(False, end='')
# Submission Successful! 5 out of 5 private test(s) passed.
