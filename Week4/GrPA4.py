x = input()
matrix = []
while x != '':
    matrix += [x.split()]
    x = input()

rotation, row = [], []
r, c = len(matrix), len(matrix[1])

for i in range(1,r+1):
    for j in range(1,c+1):
        print(matrix[r - i][c - j], sep=' ')
#     rotation += [row]
#     row = []
#
# for i in range
