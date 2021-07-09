"""
Accept a non-empty list of space-separated positive integers as input
from the user and print all numbers in the list which are greater then
the average in non-descending order. The output
format should be a sequence of space-separated integers.
"""
list0=[]
for i in input():
    if i != ' ':
        list0.append(int(i))
sum0, count0 = 0, 0
for i in list0:
    sum0 += i
    count0 += 1
mean0 = sum0 / count0
print(list0)
list1=list0.sort(reverse=True)
print(list1)
for i in list1:
    if i > mean0:
        print(str(i)+' ',end='')