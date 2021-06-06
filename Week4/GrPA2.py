opend = 0
nesting = 0
maxnext = 1
y = input()
for x in y:
    if x == '(':
        opend += 1
        nesting += 1
    if x == ')':
        if maxnext < nesting:
            maxnext = nesting
        nesting = 0
        opend -= 1

if opend != 0 or y.index(')') < y.index('('):
    print('Not matched', end='')
else:
    print(maxnext, end='')

# Submission Successful! 3 out of 3 private test(s) passed.
