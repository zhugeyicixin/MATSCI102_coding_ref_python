import numpy as np
from pprint import pprint
from matplotlib import pyplot as plt

from utils.constants import hbar, m_e, k_B, J_to_eV, eV_to_J, ang_to_m

__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def plot_1a(save_fig=False, show_fig=False):
    nv_over_N = 3*(dl_over_l - da_over_a)
    print('nv_over_N')
    for x in nv_over_N:
        print('{:,.3e}'.format(x))

    ln_nv_over_N = np.log(nv_over_N[nv_over_N>0])
    T_reciprocal = 1/T[nv_over_N>0]

    k_fit, b_fit = np.polyfit(T_reciprocal, ln_nv_over_N, deg=1)
    y_fit = k_fit*T_reciprocal + b_fit

    hv_fit = -k_fit*k_B
    sv_fit = b_fit*k_B

    print('k_fit', k_fit)
    print('b_fit', b_fit)
    print('y_fit', y_fit)
    print('hv_fit', hv_fit, hv_fit*J_to_eV)
    print('sv_fit', sv_fit, sv_fit*J_to_eV)

    fig = plt.figure(
        figsize=(12, 8),
        # constrained_layout=True
    )
    ax = fig.add_subplot(111)

    ax.plot(
        T_reciprocal*1e3,
        ln_nv_over_N,
        marker='*',
        markersize=30,
        linestyle='none',
        # linewidth=5,
        color='tab:blue',
    )

    ax.plot(
        T_reciprocal*1e3,
        y_fit,
        # marker='*',
        # markersize=10,
        linestyle='--',
        linewidth=5,
        color='tab:red',
    )

    #
    ax.set_xlabel('1000/T (1/K)', size=36)
    ax.set_ylabel('$\ln(n_v/N)$', size=36)
    # ax.set_xlim(plot_range)
    # ax.set_ylim(bottom=-0.7, top=2.2)
    # ax.set_xticks(ticks=[])
    # ax.set_yticks(ticks=[])
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    # ax.set_frame_on(False)

    plt.tight_layout()
    if save_fig:
        plt.savefig('../plots/hw08/q_1a.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


if __name__ == '__main__':
    T = 273.15 + np.array([
        300,
        320,
        340,
        360,
        380,
        400,
        420,
        440,
        460,
        480,
        500,
        520,
        540,
        560,
        580,
        600,
        620,
        640,
    ])
    da_over_a = np.array([
        0.00722,
        0.00778,
        0.00833,
        0.00889,
        0.00946,
        0.01006,
        0.01068,
        0.01130,
        0.01190,
        0.01251,
        0.01313,
        0.01377,
        0.01444,
        0.01511,
        0.01581,
        0.01652,
        0.01725,
        0.01800,
    ])
    dl_over_l = np.array([
        0.00722,
        0.00778,
        0.00833,
        0.00889,
        0.00946,
        0.01006,
        0.01067,
        0.01130,
        0.01192,
        0.01256,
        0.01320,
        0.01386,
        0.01455,
        0.01523,
        0.01594,
        0.01670,
        0.01749,
        0.01827,
    ])

    plot_1a(
        save_fig=True,
        show_fig=True,
    )