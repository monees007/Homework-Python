max0 = ''
def max_element(list0):
    global max0
    if not isinstance(max0, str) == isinstance(list0[0], str):
        max0 = list0[0]
    if max0 < list0[0]:
        max0 = list0.pop(0)
    else:
        list0.remove(list0[0])
    while len(list0) > 0:
        max_element(list0)
    return max0
# Submission Successful! 4 out of 4 private test(s) passed.
