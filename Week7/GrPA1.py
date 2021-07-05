digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number = input()
for i in number:
    i = int(i)
    print(digits[i])
output = ''
flag = True
for i in number:
    i = int(i)
    if flag:
        output += digits[i]
        flag = False
    else:
        output += digits[i].capitalize()

print(output)

# Submission Successful! 3 out of 3 private test(s) passed.
