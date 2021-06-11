def is_magic(mat):
    magic = 0
    for i in mat[0]:
        magic += i
    # magic
    # for sum of one row
    for i in mat:
        # entry in one row
        sum_of_row = 0
        for j in i:
            sum_of_row += j
        if sum_of_row != magic:
            return 'NO'
    # for sums of one column
    for i in range(len(mat)):  # this gives column id
        sum_of_column = 0
        for j in mat:
            sum_of_column += j[i]
        if sum_of_column != magic:
            return 'NO'
    # for || diagonals
    sum_of_diagonals = 0
    for i in range(len(mat)):
        sum_of_diagonals += mat[i][i]
    if sum_of_diagonals != magic:
        return 'NO'
    # for |- diagonal:
    sum_of_diagonals = 0
    for i in range(len(mat) - 1, -1, -1):
        sum_of_diagonals += mat[i][i]
    if sum_of_diagonals != magic:
        return 'NO'
    return 'YES'

# Submission Successful! 3 out of 3 private test(s) passed.
