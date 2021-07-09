openers = ['(', '{', '[']
closure = [')', '}', ']']
opened =['']
closed =['']
s = input()
f=0
for char in s:
    if char in openers:
        opened.append(char)
    if char in closure:
        closed.append(char)
print(opened)
print(closed)
for i in range(1,len(opened)+1):
    if opened[i]!=closed[-i]:
        print(False)
        break
    else:
        print(True)
