
def test(list0,presenceA,presenceStar):
    for i in range(len(list0)):
        if list0[i] == 'a':
            presenceA += 1
        if list0[i] == "*":
            presenceStar += 1
        if isinstance(list0[i],list):
            findMe2(list0[i],presenceA,presenceStar)
    return presenceA,presenceStar

def findMe(list0):
    presenceA = 0
    presenceStar = 0
    return findMe2(list0,presenceA,presenceStar)

def findMe2(list0,presenceA,presenceStar):
    presenceA,presenceStar=test(list0,presenceA,presenceStar)
    if presenceA > 0 and presenceStar > 0:
        return True
    else:
        print(presenceA,presenceStar)

findMe([['a', 'z'], ['b'], ['c'], [['d'], [[5], ['*'], []], [], ['j']]])
