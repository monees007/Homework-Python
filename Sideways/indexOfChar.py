def allindex(_char, _string):
    l = [0]
    for i in _string:
        if i == _char:
            l += [l[-1]+_string.index(i)]
            _string = _string[_string.index(i) + 1:]
    return l[1:]


print(allindex('e', 'I have many elephant in my lunchbox'))
