# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]

# getting length of list
length = len(list)

# Iterating the index
# same as 'for i in range(len(list))'
for i in range(length):
	print(list[i])

def topperAB(A,B):
    TopperAB = []
    for a in A:
        for b in B:
            p = 1#first(a)
            q = 1#first(b)
            if p == q:
                TopperAB = TopperAB + a
    return(TopperAB)