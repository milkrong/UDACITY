# TODO r1 <---> r2
# 直接修改参数矩阵，无返回值


def swapRows(M, r1, r2):
    M[r1], M[r2] = M[r2], M[r1]
    return

# TODO r1 <--- r1 * scale， scale!=0
# 直接修改参数矩阵，无返回值


def scaleRow(M, r, scale):
    M[r] = [scale * x for x in M[r]]
    return

# TODO r1 <--- r1 + r2*scale
# 直接修改参数矩阵，无返回值


def addScaledRow(M, r1, r2, scale):
    M[r1] = [x + scale * y for x, y in zip(M[r1], M[r2])]
    return

# TODO 构造增广矩阵，假设A，b行数相同


def augmentMatrix(A, b):
    Ab = [x + y for x, y in zip(A, b)]
    return Ab


# TODO 实现 Gaussain Jordan 方法求解 Ax = b


""" Gaussian Jordan 方法求解 Ax = b.
    参数
        A: 方阵 
        b: 列向量
        decPts: 四舍五入位数，默认为4
        epsilon: 判读是否为0的阈值，默认 1.0e-16
 
    返回列向量 x 使得 Ax = b 
    返回None，如果 A，b 高度不同
    返回None，如果 A 为奇异矩阵
"""


def gj_Solve(A, b, decPts=4, epsilon=1.0e-16):

    return None
