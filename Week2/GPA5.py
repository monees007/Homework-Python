def sv(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(letter.lower(), )


i, f, p1, d1, p2, d2 = 0, True, input(), input(), input(), input()
if d1[-4:] > d2[-4:]:
    print(p1, end='')
elif d1[-4:] < d2[-4:]:
    print(p2, end='')
else:
    if d1[3:5] > d2[3:5]:
        print(p1, end='')
    elif d1[3:5] < d2[3:5]:
        print(p2, end='')
    else:
        if d1[0:2] > d2[0:2]:
            print(p1, end='')
        elif d1[0:2] < d2[0:2]:
            print(p2, end='')
        else:
            while f:
                f = False
                if sv(p1[i]) < sv(p2[i]):
                    print(p1, end='')
                elif sv(p1[i]) > sv(p2[i]):
                    print(p2, end='')
                else:
                    i += 1
                    f = True
# Submission Successful! 4 out of 4 private test(s) passed.
