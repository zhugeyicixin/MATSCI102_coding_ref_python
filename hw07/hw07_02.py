import numpy as np
from matplotlib import pyplot as plt


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def atom_orbital_1(x, scale=1., shift=0.):
    y = np.exp(-np.abs(scale*(x-shift)))*scale
    return y

def plot_2b_1(save_fig=False, show_fig=False):

    num_points = 1001
    atom_range = np.linspace(-x_range, x_range, num_points)
    atom_range_1 = center_1 + atom_range
    orbit_atom_1 = atom_orbital_1(
        x=atom_range_1,
        scale=atom_scale_1,
        shift=center_1,
    )
    atom_range_2 = center_2 + atom_range
    orbit_atom_2 = atom_orbital_1(
        x=atom_range_2,
        scale=atom_scale_2,
        shift=center_2
    )

    fig = plt.figure(
        figsize=(12, 8),
        # constrained_layout=True
    )
    ax = fig.add_subplot(111)

    ax.plot(
        atom_range_1,
        orbit_atom_1,
        linewidth=5,
        color='tab:red',
    )
    ax.plot(
        atom_range_2,
        orbit_atom_2,
        linewidth=5,
        color='tab:blue',
    )
    ax.plot(
        plot_range,
        [0, 0],
        linewidth=1,
        color='black',
    )
    ax.text(
        center_1-0.25,
        0,
        '1',
        fontsize=36,
        fontweight='bold',
        color='tab:red',
        )
    ax.text(
        center_2-0.25,
        0,
        '2',
        fontsize=36,
        fontweight='bold',
        color='tab:blue',
    )

    #
    # ax.set_xlabel('x (a$_0$)', size=36)
    # ax.set_ylabel('y (a$_0$)', size=36)
    ax.set_xlim(plot_range)
    ax.set_ylim(bottom=-0.7, top=2.2)
    ax.set_xticks(ticks=[])
    ax.set_yticks(ticks=[])
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    ax.set_frame_on(False)

    plt.tight_layout()
    if save_fig:
        plt.savefig('../plots/hw07/q_2b_1.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_2b_2(save_fig=False, show_fig=False):

    c_1 = 2./np.sqrt(5)
    c_2 = 1./np.sqrt(5)

    num_points = 1001
    atom_range = np.linspace(
        center_1-x_range,
        center_2+x_range,
        num_points,
    )
    orbit_atom_1 = atom_orbital_1(
        x=atom_range,
        scale=atom_scale_1,
        shift=center_1,
    )
    orbit_atom_2 = atom_orbital_1(
        x=atom_range,
        scale=atom_scale_2,
        shift=center_2
    )
    orbit_bonding = c_1*orbit_atom_1 + c_2*orbit_atom_2

    fig = plt.figure(
        figsize=(12, 8),
        # constrained_layout=True
    )
    ax = fig.add_subplot(111)

    ax.plot(
        atom_range,
        orbit_bonding,
        linewidth=5,
        color='tab:green',
    )
    # ax.plot(
    #     atom_range,
    #     orbit_atom_1,
    #     linewidth=5,
    #     color='tab:red',
    # )
    # ax.plot(
    #     atom_range,
    #     orbit_atom_2,
    #     linewidth=5,
    #     color='tab:blue',
    # )
    ax.plot(
        plot_range,
        [0, 0],
        linewidth=1,
        color='black',
    )
    ax.text(
        center_1-0.25,
        0,
        '1',
        fontsize=36,
        fontweight='bold',
        color='tab:red',
        )
    ax.text(
        center_2-0.25,
        0,
        '2',
        fontsize=36,
        fontweight='bold',
        color='tab:blue',
        )

    #
    # ax.set_xlabel('x (a$_0$)', size=36)
    # ax.set_ylabel('y (a$_0$)', size=36)
    ax.set_xlim(plot_range)
    ax.set_ylim(bottom=-0.7, top=2.2)
    ax.set_xticks(ticks=[])
    ax.set_yticks(ticks=[])
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    ax.set_frame_on(False)

    plt.tight_layout()
    if save_fig:
        plt.savefig('../plots/hw07/q_2b_2.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_2b_3(save_fig=False, show_fig=False):

    c_1 = -1./np.sqrt(5)
    c_2 = 2./np.sqrt(5)

    num_points = 1001
    atom_range = np.linspace(
        center_1-x_range,
        center_2+x_range,
        num_points,
        )
    orbit_atom_1 = atom_orbital_1(
        x=atom_range,
        scale=atom_scale_1,
        shift=center_1,
    )
    orbit_atom_2 = atom_orbital_1(
        x=atom_range,
        scale=atom_scale_2,
        shift=center_2
    )
    orbit_bonding = c_1*orbit_atom_1 + c_2*orbit_atom_2

    fig = plt.figure(
        figsize=(12, 8),
        # constrained_layout=True
    )
    ax = fig.add_subplot(111)

    ax.plot(
        atom_range,
        orbit_bonding,
        linewidth=5,
        color='tab:cyan',
    )
    # ax.plot(
    #     atom_range,
    #     orbit_atom_1,
    #     linewidth=5,
    #     color='tab:red',
    # )
    # ax.plot(
    #     atom_range,
    #     orbit_atom_2,
    #     linewidth=5,
    #     color='tab:blue',
    # )
    ax.plot(
        plot_range,
        [0, 0],
        linewidth=1,
        color='black',
    )
    ax.text(
        center_1-0.25,
        0,
        '1',
        fontsize=36,
        fontweight='bold',
        color='tab:red',
        )
    ax.text(
        center_2-0.25,
        0,
        '2',
        fontsize=36,
        fontweight='bold',
        color='tab:blue',
        )

    #
    # ax.set_xlabel('x (a$_0$)', size=36)
    # ax.set_ylabel('y (a$_0$)', size=36)
    ax.set_xlim(plot_range)
    ax.set_ylim(bottom=-1.2, top=2.2)
    ax.set_xticks(ticks=[])
    ax.set_yticks(ticks=[])
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    ax.set_frame_on(False)

    plt.tight_layout()
    if save_fig:
        plt.savefig('../plots/hw07/q_2b_3.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax



def plot_2c(save_fig=False, show_fig=False):

    energy_level_length = 1
    E_1 = -4
    E_2 = -2
    E_m = -3-np.sqrt(5)
    E_p = -3+np.sqrt(5)

    fig = plt.figure(
        figsize=(12, 8),
        # constrained_layout=True
    )
    ax = fig.add_subplot(111)

    ax.plot(
        [center_1-energy_level_length, center_1],
        [E_1, E_1, ],
        linewidth=5,
        color='tab:red',
    )
    ax.plot(
        [center_2, center_2+energy_level_length],
        [E_2, E_2, ],
        linewidth=5,
        color='tab:blue',
    )
    ax.plot(
        [
            center_1+center_2-energy_level_length/2,
            center_1+center_2+energy_level_length/2,
        ],
        [E_m, E_m, ],
        linewidth=5,
        color='tab:green',
    )
    ax.plot(
        [
            center_1+center_2-energy_level_length/2,
            center_1+center_2+energy_level_length/2,
        ],
        [E_p, E_p, ],
        linewidth=5,
        color='tab:cyan',
    )
    ax.plot(
        [
            center_1,
            (center_1+center_2-energy_level_length)/2,
        ],
        [E_1, E_p, ],
        linewidth=3,
        linestyle='--',
        color='tab:red',
    )
    ax.plot(
        [
            center_1,
            (center_1+center_2-energy_level_length)/2,
            ],
        [E_1, E_m, ],
        linewidth=3,
        linestyle='--',
        color='tab:red',
    )
    ax.plot(
        [
            center_2,
            (center_1+center_2+energy_level_length)/2,
            ],
        [E_2, E_p, ],
        linewidth=3,
        linestyle='--',
        color='tab:blue',
    )
    ax.plot(
        [
            center_2,
            (center_1+center_2+energy_level_length)/2,
            ],
        [E_2, E_m, ],
        linewidth=3,
        linestyle='--',
        color='tab:blue',
    )
    ax.text(
        center_1-1,
        E_1-0.35,
        'E$_1$=-4 eV',
        fontsize=28,
        color='tab:red',
    )
    ax.text(
        center_2,
        E_2-0.35,
        'E$_2$=-2 eV',
        fontsize=28,
        color='tab:blue',
    )
    ax.text(
        (center_1+center_2)/2-0.5,
        E_m-0.35,
        'E$^-$=-5.236 eV',
        fontsize=28,
        color='tab:green',
    )
    ax.text(
        (center_1+center_2)/2-0.5,
        E_p+0.15,
        'E$^+$=-0.764 eV',
        fontsize=28,
        color='tab:cyan',
        )

    #
    # ax.set_xlabel('x (a$_0$)', size=36)
    # ax.set_ylabel('y (a$_0$)', size=36)
    # ax.set_xlim(plot_range)
    # ax.set_ylim(bottom=-0.7, top=2.2)
    ax.set_xticks(ticks=[])
    ax.set_yticks(ticks=[])
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    ax.set_frame_on(False)

    plt.tight_layout()
    if save_fig:
        plt.savefig('../plots/hw07/q_2c.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


if __name__ == '__main__':

    center_1 = -2.0
    center_2 = 2.0
    atom_scale_1 = 2
    atom_scale_2 = 1
    x_range = 1.5
    plot_range = (
        center_1 - x_range - 2,
        center_2 + x_range + 2,
    )

    fig, ax = plot_2b_1(
        save_fig=True,
        show_fig=True,
    )
    fig, ax = plot_2b_2(
        save_fig=True,
        show_fig=True,
    )
    fig, ax = plot_2b_3(
        save_fig=True,
        show_fig=True,
    )
    fig, ax = plot_2c(
        save_fig=True,
        show_fig=True,
    )
