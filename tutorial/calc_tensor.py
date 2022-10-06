import itertools

from sympy import MatrixSymbol, Matrix
import numpy as np


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def tensor_transformation(matrix_a):
    s_1 = MatrixSymbol('X', 3, 3)
    a = Matrix(matrix_a)
    s_2 = a@s_1@(a.T)
    for i,j in itertools.product(*[range(x) for x in s_2.shape]):
        print((i,j), s_2[i,j])
        # for m in range(3):
        #     for n in range(3):
        #         c = matrix_a[i,m]*matrix_a[j,n]
        #         if c!=0:
        #             print('+{}X[{},{}]'.format(c,m,n), end=' ')
        # print()
    return s_2


if __name__ == '__main__':
    a = np.array([
        [1, 0, 0],
        [0,-1, 0],
        [0, 0, 1],
    ])
    tensor_transformation(a)