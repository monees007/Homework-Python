def chk1(x, y):
    for i in x:
        for j in y:
            if not -1 <= (i - j) <= 1:
                return False
    return True

def isBlock(l):
    for i in l:
        for j in l:
            if not chk1(i,j):
                return False
    return True
