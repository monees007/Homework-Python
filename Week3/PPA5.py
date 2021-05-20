n = int(input())
o = []
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for z in range(1, n + 1):
            if x ** 4 + y ** 3 == z ** 2:
                print(x, y, z)
# Submission Successful! 2 out of 2 private test(s) passed.
