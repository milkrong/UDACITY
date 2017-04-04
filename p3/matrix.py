A = [[1, 2, 3],
     [2, 3, 3],
     [1, 2, 5]]

B = [[1, 2, 3, 5],
     [2, 3, 3, 5],
     [1, 2, 5, 1]]


def shape(M):
    rows = M[:]
    cols = M[:]
    cols = [[row[i] for row in cols] for i in range(len(cols[0]))]
    return rows, cols


def matxRound(M, decPts=4):
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = round(M[i][j], decPts)


def transpose(M):
    M_t = M[:]
    M_t = [[row[i] for row in M_t] for i in range(len(M_t[0]))]
    return M_t


def matxMultiply(A, B):
    if len(A[0]) != len(B):
        return None
    B_t = transpose(B)
    AB = []
    for r in range(len(A)):
        row = [sum([x * y for x, y in zip(A[r], B_t[c])])
               for c in range(len(B_t))]
        AB.append(row)
    return AB


# TODO r1 <--- r1 + r2*scale
# 直接修改参数矩阵，无返回值


def addScaledRow(M, r1, r2, scale):
    M[r1] = [x + scale * y for x, y in zip(M[r1], M[r2])]
    return

# TODO 构造增广矩阵，假设A，b行数相同


def augmentMatrix(A, b):
    Ab = [x + y for x, y in zip(A, b)]
    return Ab


def gj_Solve(A, b, decPts=4, epsilon=1.0e-16):
    Ab = augmentMatrix(A, b)
    A_t = transpose(A)
    for col_index in range(len(A[0])):
        col_under_diag = transpose(A)[col_index][col_index:]
        max_row_index = col_index
        max_value = 
    return None


if __name__ == '__main__':
    rowB, colB = shape(B)
    print(rowB, colB)

    C = [[1.3333, 2.445],
         [1.456, 4.567]]
    matxRound(C, 2)
    print(C)

    print(transpose(B))

    print(matxMultiply(A, B))

    print(matxMultiply(A, C))
