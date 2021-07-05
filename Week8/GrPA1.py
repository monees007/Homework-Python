list0 = []


def reverse(list1):
    global list0
    list0 = [list1.pop(0)] + list0
    while len(list1) > 0:
        reverse(list1)
    return list0

# Submission Successful! 4 out of 4 private test(s) passed.