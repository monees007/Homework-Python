def listToDict(list0):
    dictionary = {}
    for i in range(len(list0)):
        dictionary[i] = {}
        for j in range(len(list0[i])):
            dictionary[i][j] = list0[i][j]
    return dictionary


def dictToList(dictionary):
    list0 = []
    x = 0
    y = 0
    for i in dictionary:
        if x < i:
            x = i
        for j in dictionary[i]:
            if y < j:
                y = j
    for i in range(0, x + 1):
        list0.append([])
        for j in range(0, y + 1):
            list0[i].append(0)
    for i in dictionary:
        for j in dictionary[i]:
            list0[i][j] = dictionary[i][j]
    return list0
# Submission Successful! 6 out of 6 private test(s) passed.
# non-recursive method
