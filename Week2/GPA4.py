def present(tring, x):
    for i in tring:
        if x == i:
            return True
    return False


output = ''
input = input().lower()

if present(input, 'a'):
    output += 'a'
if present(input, 'e'):
    output += 'e'
if present(input, 'i'):
    output += 'i'
if present(input, 'o'):
    output += 'o'
if present(input, 'u'):
    output += 'u'

print(output, end='')
# Submission Successful! 4 out of 4 private test(s) passed.
