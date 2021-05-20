n = int(input())
s, i = int((n - 5) / 2), 0
print('*' * n)
while i <= s:
    print('*', ' ' * i, '*', ' ' * (s - i), '*', ' ' * i, '*', sep='')
    i += 1
print('*' * n)
while i >= 0:
    print('*', ' ' * i, '*', ' ' * (s - i), '*', ' ' * i, '*', sep='')
    i += 1
print('*' * n)
