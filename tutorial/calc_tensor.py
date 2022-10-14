import itertools

from sympy import MatrixSymbol, Matrix
import numpy as np

from utils.math_utils import tensor_transformation

__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


if __name__ == '__main__':
    # a = np.array([
    #     [1, 0, 0],
    #     [0,-1, 0],
    #     [0, 0, 1],
    # ])
    a = np.array([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
    ])
    # a = np.array([
    #     [-1, 0, 0],
    #     [0, -1, 0],
    #     [0, 0, -1],
    # ])
    tensor_transformation(a)