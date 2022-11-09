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


def calc_bond_length_rhombus(
    gamma: float,
    sigma: float,
    value_range=100,
):
    A_12 = calc_limit_rhombus(
        gamma=gamma,
        power=6,
        value_range=value_range,
    )
    A_6 = calc_limit_rhombus(
        gamma=gamma,
        power=3,
        value_range=value_range,
    )
    a_0 = (2*A_12/A_6)**(1/6)*sigma
    return a_0


def calc_cohesive_energy_rhombus(
    gamma: float,
    epsilon: float,
    value_range=100,
):
    A_12 = calc_limit_rhombus(
        gamma=gamma,
        power=6,
        value_range=value_range,
    )
    A_6 = calc_limit_rhombus(
        gamma=gamma,
        power=3,
        value_range=value_range,
    )
    energy = epsilon*A_6**2/A_12/2
    return energy


def calc_rhombus_derivative_gamma(
    gamma: float,
    value_range=100,
):
    A_12 = calc_limit_rhombus(
        gamma=gamma,
        power=6,
        value_range=value_range,
    )
    A_6 = calc_limit_rhombus(
        gamma=gamma,
        power=3,
        value_range=value_range,
    )
    sigma_a_6 = A_6/A_12/2.0
    A_1_12 = calc_limit_rhombus(
        gamma=gamma,
        power=7,
        value_range=value_range,
        with_uv=True,
    )
    A_1_6 = calc_limit_rhombus(
        gamma=gamma,
        power=4,
        value_range=value_range,
        with_uv=True,
    )
    result = sigma_a_6*2*A_1_12-A_1_6

    return result


def calc_rhombus_derivative_gamma_2(
    gamma: float,
    value_range=100,
):
    A_14 = calc_limit_rhombus(
        gamma=gamma,
        power=7,
        value_range=value_range,
    )
    A_12 = calc_limit_rhombus(
        gamma=gamma,
        power=6,
        value_range=value_range,
    )
    A_6 = calc_limit_rhombus(
        gamma=gamma,
        power=3,
        value_range=value_range,
    )
    A_1_14 = calc_limit_rhombus(
        gamma=gamma,
        power=8,
        value_range=value_range,
        with_uv=True,
    )
    A_1_12 = calc_limit_rhombus(
        gamma=gamma,
        power=7,
        value_range=value_range,
        with_uv=True,
    )
    A_1_6 = calc_limit_rhombus(
        gamma=gamma,
        power=4,
        value_range=value_range,
        with_uv=True,
    )
    result = A_6/A_14*A_1_14-A_1_6
    # result = A_1_14/A_14
    # result = A_1_6/A_6

    return result


def solve_gamma():
    all_gammas_deg = np.arange(55,125,0.1)
    all_gammas_radian = all_gammas_deg/180*np.pi

    # calculate derivation
    all_dev_gammas = []
    for gamma in all_gammas_radian:
        derivative_gamma = calc_rhombus_derivative_gamma(
            gamma=gamma,
            value_range=30,
        )
        all_dev_gammas.append(derivative_gamma)
    all_dev_gammas = np.array(all_dev_gammas)

    # find gamma
    all_dev_gammas_abs = np.abs(all_dev_gammas)
    all_dev_gammas_abs[all_gammas_deg<100] = np.inf
    index_gamma = np.argmin(all_dev_gammas_abs)
    gamma_deg_opt = all_gammas_deg[index_gamma]
    gamma_rad_opt = all_gammas_radian[index_gamma]

    fig = plt.figure(
        figsize=(12, 10),
    )
    ax = fig.add_subplot(111)

    ax.plot(
        all_gammas_deg,
        all_dev_gammas,
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
    plt.savefig('../plots/hw05/q_1a.png', dpi=300)
    plt.show()

    return gamma_rad_opt



if __name__ == '__main__':

    sigma = 2.74
    epsilon = 0.0031
    gamma = solve_gamma()
    print('gamma', gamma)
    a_0 = calc_bond_length_rhombus(
        gamma=gamma,
        sigma=sigma,
        value_range=30,
    )
    print('a_0', a_0)
    e_coh = calc_cohesive_energy_rhombus(
        gamma=gamma,
        epsilon=epsilon,
        value_range=30,
    )
    print('e_coh', e_coh)