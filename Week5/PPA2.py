def newmat(x, y):
    nmat = []
    for i in range(x):
        nmat += [[]]
        for j in range(y):
            nmat[i] += [0]
    return nmat


def transpose(mat):
    r_in_mat = len(mat)
    c_in_mat = len(mat[0])
    nmat = newmat(c_in_mat, r_in_mat)

    for i in range(r_in_mat):
        for j in range(c_in_mat):
            nmat[j][i] = mat[i][j]
    return nmat

# Submission Successful! 2 out of 2 private test(s) passed.
