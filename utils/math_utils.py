import numpy as np
import itertools
from sympy import MatrixSymbol, Matrix


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def get_polar_coordinate(radius: float, angle: float):
    """

    :param radius:
    :param angle: in radians
    :return:
    """
    return np.array((
        radius*np.cos(angle), radius*np.sin(angle)
    ))


def tensor_transformation(matrix_a):
    s_1 = MatrixSymbol('X', 3, 3)
    a = Matrix(matrix_a)
    s_2 = a@s_1@(a.T)
    # s_2 = (a.T)@s_1@a
    for i,j in itertools.product(*[range(x) for x in s_2.shape]):
        print((i,j), s_2[i,j])
        # for m in range(3):
        #     for n in range(3):
        #         c = matrix_a[i,m]*matrix_a[j,n]
        #         if c!=0:
        #             print('+{}X[{},{}]'.format(c,m,n), end=' ')
        # print()
    return s_2
