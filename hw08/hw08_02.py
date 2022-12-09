import numpy as np
from matplotlib import pyplot as plt

from utils.constants import hbar, m_e, k_B, J_to_eV, eV_to_J, ang_to_m

__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'

def f_KP(
    E,
    a,
    b,
    V_0,
):
    """

    :param E: unit J
    :param a: unit m
    :param b: unit m
    :param V_0: unit J
    :return:
    """
    def f_cosh_beta_b(E_input):
        E_1 = E_input[V_0 - E_input >= 0]
        beta_1 = np.sqrt(2 * m_e * (V_0 - E_1) / hbar ** 2)
        result_1 = np.cosh(beta_1*b)

        E_2 = E_input[V_0 - E_input < 0]
        # imaginary part
        beta_2 = np.sqrt(2 * m_e * (E_2 - V_0) / hbar ** 2)
        result_2 = np.cos(beta_2*b)

        return np.concatenate([result_1, result_2], axis=-1)

    def f_beta_square(E_input):
        return 2*m_e*(V_0-E_input)/hbar**2

    def f_sinh_beta_b_over_beta(E_input):
        E_1 = E_input[V_0 - E_input > 0]
        beta_1 = np.sqrt(2 * m_e * (V_0 - E_1) / hbar ** 2)
        result_1 = np.sinh(beta_1 * b)/beta_1

        E_2 = E_input[V_0 - E_input == 0.0]
        result_2 = b*np.ones_like(E_2)

        E_3 = E_input[V_0 - E_input < 0]
        # imaginary part
        beta_3 = np.sqrt(2 * m_e * (E_3 - V_0) / hbar ** 2)
        result_3 = np.sin(beta_3 * b)/beta_3

        return np.concatenate([result_1, result_2, result_3], axis=-1)

    def f_cos_alpha_a(E_input):
        E_1 = E_input[E_input < 0]
        alpha_1 = np.sqrt(- 2 * m_e * E_1 / hbar ** 2)
        result_1 = np.cosh(alpha_1*a)

        E_2 = E_input[E_input >= 0]
        # imaginary part
        alpha_2 = np.sqrt(2 * m_e * E_2 / hbar ** 2)
        result_2 = np.cos(alpha_2*a)

        return np.concatenate([result_1, result_2], axis=-1)

    def f_alpha_square(E_input):
        return 2*m_e*E_input/hbar**2

    def f_sin_alpha_a_over_alpha(E_input):
        E_1 = E_input[E_input < 0]
        # imaginary part
        alpha_1 = np.sqrt(-2 * m_e * E_1 / hbar ** 2)
        result_1 = np.sinh(alpha_1*a)/alpha_1

        E_2 = E_input[E_input == 0.0]
        result_2 = b*np.ones_like(E_2)

        E_3 = E_input[E_input > 0]
        alpha_3 = np.sqrt(2 * m_e * E_3 / hbar ** 2)
        result_3 = np.sin(alpha_3 * a)/alpha_3

        return np.concatenate([result_1, result_2, result_3], axis=-1)

    y = (
        f_cos_alpha_a(E)*f_cosh_beta_b(E)
        + (f_beta_square(E)-f_alpha_square(E))/2
        * f_sin_alpha_a_over_alpha(E)
        *f_sinh_beta_b_over_beta(E)
    )

    # alpha = np.sqrt(2*m_e*E)/hbar
    # beta = np.sqrt(2*m_e*(V_0 - E))/hbar
    # print('beta', beta)
    # y = (
    #     np.cos(alpha*a)*np.cosh(beta*b)
    #     + (beta**2-alpha**2)/2/alpha/beta*np.sin(alpha*a)*np.sinh(beta*b)
    # )

    return y


def find_intersection(E, y):
    y_1 = np.abs(y)-1.0
    y_2 = y_1[:-1]*y_1[1:]
    y_3 = y_2 < 0
    return E[:-1][y_3]


def plot_2a(save_fig=False, show_fig=False):
    step = 0.0001*eV_to_J
    # step = 0.1*eV_to_J
    # E = np.arange(0, V_0+step, step)
    # E = np.arange(0, V_0, step)
    E = np.arange(step, 100*V_0, step)
    y = f_KP(
        E=E,
        a=a,
        b=b,
        V_0=V_0,
    )
    print('y', y)
    E_crossing = find_intersection(E, y)
    print('E_crossing', len(E_crossing), E_crossing*J_to_eV)

    fig = plt.figure(
        figsize=(12, 8),
        # constrained_layout=True
    )
    ax = fig.add_subplot(111)

    ax.plot(
        E*J_to_eV,
        y,
        linewidth=5,
        color='tab:red',
    )

    for x in E_crossing:
        ax.plot(
            np.array([x, x])*J_to_eV,
            [-1.0, 1.0],
            linestyle='-.',
            linewidth=1,
            color='tab:green',
        )

    ax.plot(
        [0, E[-1]*J_to_eV],
        [1.0, 1.0],
        linestyle='--',
        linewidth=3,
        color='black',
    )

    ax.plot(
        [0, E[-1]*J_to_eV],
        [-1.0, -1.0],
        linestyle='--',
        linewidth=3,
        color='black',
    )

    #
    ax.set_xlabel('E (eV)', size=36)
    ax.set_ylabel('f(E)', size=36)
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=-2.0, top=2.0)
    # ax.set_xticks(ticks=[])
    # ax.set_yticks(ticks=[])
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    # ax.set_frame_on(False)

    plt.tight_layout()
    if save_fig:
        plt.savefig('../plots/hw08/q_2a.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


if __name__ == '__main__':
    a = 0.5*ang_to_m
    # a = 50*ang_to_m
    # b = 0.25*ang_to_m
    b = 0.25*ang_to_m
    V_0 = 13.6*eV_to_J

    plot_2a(
        save_fig=True,
        show_fig=True,
    )