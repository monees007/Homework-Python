de = [100, 50, 10, 5, 2, 1]
a = int(input())
den = {}
for x in de:
    den[x] = a // x
    a %= x
print(den)
