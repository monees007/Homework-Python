def merge(d1, d2, priority):
    for key in d1:
        if not (key in d2) or priority == 'first':
            d2[key] = d1[key]
    return d2
