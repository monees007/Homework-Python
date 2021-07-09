import string

dictionary={'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}
for i in range(10):
    dictionary[str(i)]=str(9-i)
list0,list1=[],[]
for i in string.ascii_uppercase:
    list0.append(i)
    list1=[i]+list1
for i in range(len(list0)):
    dictionary[list0[i]]=list1[i]
s=input()
o=''
for i in s:
    if i==' ':
        o+='_'
    elif i in dictionary:
        o+=dictionary[i]
    else:
        o+=i
print(o)
# 