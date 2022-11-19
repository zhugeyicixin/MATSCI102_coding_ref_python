import numpy as np


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def calc_limit_cubic(power, value_range=100):
    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)
    w_ = np.arange(-value_range, value_range+1, dtype=float)

    # u_ = np.arange(0, value_range+1, dtype=float)
    # v_ = np.arange(0, value_range+1, dtype=float)
    # w_ = np.arange(0, value_range+1, dtype=float)

    u, v, w = np.meshgrid(u_, v_, w_, indexing='ij')
    # u, v = np.meshgrid(u_, v_, indexing='ij')
    # print('u_', u_)
    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    result = u**2 + v**2 + w**2
    # result = u**2 + v**2
    result = result.flatten()

    # print('result', result)
    # print('np.sum(result)', np.sum(result))

    result = result[result.nonzero()]
    result = np.power(result, power)
    result = 1.0/result
    # result[np.isinf(result)] = 0
    result = np.sum(result)

    return result


def calc_limit_FCC(power, value_range=100):
    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)
    w_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v, w = np.meshgrid(u_, v_, w_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    result = ((u+v)**2 + (v+w)**2 + (w+u)**2)/4
    result = result.flatten()
    result = result[result.nonzero()]
    result = np.power(result, power)
    result = 1.0/result
    result = np.sum(result)

    return result


def calc_limit_NaCl(power, value_range=100):
    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)
    w_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v, w = np.meshgrid(u_, v_, w_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    result = ((u+v+1)**2 + (v+w+1)**2 + (w+u+1)**2)/4
    result = result.flatten()
    result = result[result.nonzero()]
    result = np.power(result, power)
    result = 1.0/result
    result = np.sum(result)

    return result


def calc_limit_NaCl_2(power, value_range=100):
    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)
    w_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v, w = np.meshgrid(u_, v_, w_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    # result = ((u+v+1)**2 + (v+w+1)**2 + (w+u-1)**2)/4
    result = ((u+v)**2 + (v+w)**2 + (w+u+1)**2)/4
    result = result.flatten()
    result = result[result.nonzero()]
    result = np.power(result, power)
    result = 1.0/result
    result = np.sum(result)

    return result


def calc_Madelung_NaCl(value_range=100):
    """
    Seems not correct? Why?

    :param value_range:
    :return:
    """

    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)
    w_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v, w = np.meshgrid(u_, v_, w_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    A_1 = ((u+v)**2 + (v+w)**2 + (w+u)**2)/4
    A_1 = A_1.flatten()
    A_1 = np.power(A_1, 0.5)
    A_1 = 1.0 / A_1
    A_1[np.isinf(A_1)] = 0.0

    A_2 = ((u+v+1)**2 + (v+w+1)**2 + (w+u+1)**2)/4
    # A_2 = ((u+v)**2 + (v+w)**2 + (w+u+1)**2)/4
    A_2 = A_2.flatten()
    A_2 = np.power(A_2, 0.5)
    A_2 = 1.0 / A_2

    result = A_1 - A_2
    result = np.sum(result)

    return result


def calc_Madelung_KCl_2D(value_range=100):
    """
    Seems not correct? Why?

    :param value_range:
    :return:
    """

    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v = np.meshgrid(u_, v_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    A_1 = (u**2 + v**2)
    A_1 = A_1.flatten()
    A_1 = np.power(A_1, 0.5)
    A_1 = 1.0 / A_1
    A_1[np.isinf(A_1)] = 0.0

    # A_2 = ((u+v+1)**2 + (v+w+1)**2 + (w+u+1)**2)/4
    A_2 = ((u+0.5)**2 + (v+0.5)**2 )
    A_2 = A_2.flatten()
    A_2 = np.power(A_2, 0.5)
    A_2 = 1.0 / A_2

    result = A_1 - A_2
    result = np.sum(result)

    return result


def calc_Madelung_KCl_2D_2(value_range=100):
    """
    Seems not correct? Why?

    :param value_range:
    :return:
    """

    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v = np.meshgrid(u_, v_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    A_1 = (-1.0)**(u+v)/np.sqrt(u**2 + v**2)
    A_1 = A_1.flatten()
    A_1[np.isinf(A_1)] = 0.0

    result = np.sum(A_1)

    return result





def calc_LJ_KCl_2D(value_range=100):
    """
    Seems not correct? Why?

    :param value_range:
    :return:
    """

    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v = np.meshgrid(u_, v_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    A_1 = (u**2 + v**2)
    A_1 = A_1.flatten()
    A_1 = np.power(A_1, 6)
    A_1 = 1.0 / A_1
    A_1[np.isinf(A_1)] = 0.0

    # A_2 = ((u+v+1)**2 + (v+w+1)**2 + (w+u+1)**2)/4
    A_2 = ((u+0.5)**2 + (v+0.5)**2 )
    A_2 = A_2.flatten()
    A_2 = np.power(A_2, 6)
    A_2 = 1.0 / A_2

    result = A_1 + A_2
    result = np.sum(result)

    return result


def calc_LJ_KCl_2D_2(value_range=100):
    """
    Seems not correct? Why?

    :param value_range:
    :return:
    """

    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v = np.meshgrid(u_, v_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    A_1 = 1.0/(u**2 + v**2)**6
    A_1 = A_1.flatten()
    A_1[np.isinf(A_1)] = 0.0

    result = np.sum(A_1)

    return result


def calc_bond_length_cubic(sigma):
    A_12 = calc_limit_cubic(power=6, value_range=30)
    A_6 = calc_limit_cubic(power=3, value_range=30)
    a_0 = (2*A_12/A_6)**(1/6)*sigma
    return a_0


def calc_bond_length_FCC(sigma):
    A_12 = calc_limit_FCC(power=6, value_range=30)
    A_6 = calc_limit_FCC(power=3, value_range=30)
    # lattice parameter
    a_0 = (2 * A_12 / A_6) ** (1 / 6) * sigma
    # nearest distance
    d_nn = a_0 / np.sqrt(2)
    return d_nn


if __name__ == '__main__':

    # for r in [1, 2, 3, 5, 10, 20, 30]:
    #     result = calc_limit_cubic(power=6, value_range=r)
    #     print('r', r, result)
    # print()
    #
    # for r in [1, 2, 3, 5, 10, 20, 30]:
    #     result = calc_limit_cubic(power=3, value_range=r)
    #     print('r', r, result)
    # print()
    #
    # for r in [1, 2, 3, 5, 10, 20, 30]:
    #     result = calc_limit_FCC(power=6, value_range=r)
    #     print('r', r, result)
    # print()
    #
    # for r in [1, 2, 3, 5, 10, 20, 30]:
    #     result = calc_limit_FCC(power=3, value_range=r)
    #     print('r', r, result)
    # print()

    # for r in [1, 2, 3, 5, 10, 20, 30]:
    #     result = calc_limit_NaCl(power=6, value_range=r)
    #     print('r', r, result)
    # print()
    #
    # for r in [1, 2, 3, 5, 10, 20, 30]:
    #     result = calc_limit_NaCl_2(power=6, value_range=r)
    #     print('r', r, result)
    # print()
    #
    # for r in [1, 2, 3, 5, 10, 20, 30]:
    #     result = calc_limit_NaCl(power=3, value_range=r)
    #     print('r', r, result)
    # print()
    #
    # for r in [1, 2, 3, 5, 10, 20, 30]:
    #     result = calc_limit_NaCl_2(power=3, value_range=r)
    #     print('r', r, result)
    # print()

    # for s in [2.74, 3.40, 3.65, 3.98]:
    #     bond = calc_bond_length_cubic(sigma=s)
    #     print('bond', bond)
    # print()
    #
    # for s in [2.74, 3.40, 3.65, 3.98]:
    #     bond = calc_bond_length_FCC(sigma=s)
    #     print('bond', bond)
    # print()

    # for r in [1, 2, 3, 5, 10, 20, 30, 50, 100, ]:
    #     result_1 = calc_Madelung_NaCl(value_range=r)
    #     print('r', r, result_1/2,)
    # print()

    # for r in [1, 2, 3, 5, 10, 20, 30, 50, 100, 500, 1000, 5000, 10000]:
    #     result_1 = calc_Madelung_KCl_2D(value_range=r)
    #     result_2 = calc_Madelung_KCl_2D_2(value_range=r)
    #     print('r', r, result_1/np.sqrt(2), result_2)
    # print()

    for r in [1, 2, 3, 5, 10, 20, 30, 50, 100, ]:
        result_1 = calc_LJ_KCl_2D(value_range=r)
        result_2 = calc_LJ_KCl_2D_2(value_range=r)
        print('r', r, result_1, result_2*2**6)
    print()
