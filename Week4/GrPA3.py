x, l = input(), []
while x != '':
    l += [int(x)]
    x = input()

l.sort()
o = []
for i in l:
    for j in l:
        for k in l:
            if i + j == k:
                if not [i, j] in o:
                    o += [[i, j]]

s = ''
for i in o:
    for j in i:
        s = s + ' ' + str(j)
    print(s[1:])
    s = ''
