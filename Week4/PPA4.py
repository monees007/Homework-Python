"""
Accept a non-empty list of space-separated positive integers as input
from the user and print all numbers in the list which are greater then
the average in non-descending order. The output
format should be a sequence of space-separated integers.
"""
list0 = input().split(' ')
list0.sort()
list1, sum0 = [], 0
for i in list0:
    list1.append(int(i))
    sum0 += int(i)
max0 = sum0 / len(list1)
for i in list1:
    if (i > max0) and (list1.index(i) < len(list1) - 1):
        print(i, end=' ')
    elif (i > max0) and (list1.index(i) == (len(list1) - 1)):
        print(i)
