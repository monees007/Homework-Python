# from Week8 import GrPA3
def member(L, x):
    if len(L) == 0:
        return False
    if len(L) == 1:
        return L[0] == x
    return L[0] ==x or member(L[1:], x)

print(member([1,4,3,6,8],6))
