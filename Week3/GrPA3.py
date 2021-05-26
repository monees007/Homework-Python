x = input().lower()
z = ''
for i in x:
    if i.isalpha():
        z += i

y = sorted(z)
print(''.join(y), end='')

# Submission Successful! 4 out of 4 private test(s) passed.
