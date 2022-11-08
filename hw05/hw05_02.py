import numpy as np
from matplotlib import pyplot as plt

__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def calc_limit_rhombus(
    gamma: float,
    power: float,
    value_range=100,
    with_uv=False,
):
    """

    :param gamma: angle between a and b vectors. Unit: Radian
    :param power:
    :param value_range:
    :return:
    """
    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v = np.meshgrid(u_, v_, indexing='ij')

    result = u**2 + v**2 + 2*u*v*np.cos(gamma)
    result = result.flatten()

    effective_indices = result.nonzero()
    result = result[effective_indices]
    result = np.power(result, power)
    if with_uv:
        uv_term = (u*v).flatten()
        uv_term = uv_term[effective_indices]
        result = uv_term/result
    else:
        result = 1.0/result

    result = np.sum(result)

    return result


def calc_limit_1(
    power: float,
    value_range=100,
    with_uv=False,
):
    """

    :param gamma: angle between a and b vectors. Unit: Radian
    :param power:
    :param value_range:
    :return:
    """
    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v = np.meshgrid(u_, v_, indexing='ij')

    result = u**2 + v**2 + 2*u*v
    result = result.flatten()

    effective_indices = result.nonzero()
    result = result[effective_indices]
    result = np.power(result, power)
    if with_uv:
        uv_term = (u*v).flatten()
        uv_term = uv_term[effective_indices]
        result = uv_term*result

    result = np.sum(result)

    return result

def calc_limit_2(
    power: float,
    value_range=100,
    with_uv=False,
):
    """

    :param gamma: angle between a and b vectors. Unit: Radian
    :param power:
    :param value_range:
    :return:
    """
    u = np.arange(-value_range, value_range+1, dtype=float)

    result = u**2

    effective_indices = result.nonzero()
    result = result[effective_indices]
    result = np.power(result, power)
    if with_uv:
        uv_term = u[effective_indices]
        result = uv_term*result

    result = np.sum(result)

    return result

def f_n(
    n: int,
    m=1,
    value_range=100,
):
    A_n = calc_limit_1(
        power=n,
        value_range=value_range,
    )
    A_1_n = calc_limit_1(
        power=n-m,
        value_range=value_range,
        with_uv=True,
    )
    # result = A_6/A_14*A_1_14-A_1_6
    # result = A_1_14/A_14
    result = A_1_n/A_n

    return result


if __name__ == '__main__':

    all_ns = []
    all_fs = []
    for n in np.arange(-7, 7, 0.1):
        all_ns.append(n)
        all_fs.append(f_n(
            n=n,
            m=1,
            value_range=30,
        ))
        print('n', n)
        print(all_fs[-1])
        print()


    fig = plt.figure(
        figsize=(12, 10),
    )
    ax = fig.add_subplot(111)

    ax.plot(
        all_ns,
        all_fs,
        linewidth=5,
    )

    ax.set_xlabel('$\gamma$ (°)', size=36)
    ax.set_ylabel('$f(\gamma)$', size=36)
    # ax.set_xlim(left=-5, right=5)
    # ax.set_ylim(bottom=-5, top=5)
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    ax.grid(axis='both', which='major', alpha=0.5)

    plt.tight_layout()
    plt.show()

