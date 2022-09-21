import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon as plt_Polygon
from pprint import pprint

from utils.lattice_utils import get_lattice_2D
from utils.lattice_utils import get_bisector_line
from utils.lattice_utils import get_line_intersection
from utils.lattice_utils import get_polygon_area
from utils.constants import NEAR_ZERO
from utils.plot_utils import fig_from_fig_or_none


def plot_2b(save_fig=False, show_fig=False):
    vec_a1 = np.array((-0.35, -0.61))
    vec_b1 = np.array((0.71, 0.0))
    range_x = (-1.5, 1.5)
    range_y = (-1.5, 1.5)

    lattice_points = get_lattice_2D(
        vec_a=vec_a1,
        vec_b=vec_b1,
        range_x=range_x,
        range_y=range_y,
    )

    fig = plt.figure(
        figsize=(12, 12),
        # constrained_layout=True
    )
    ax = fig.add_subplot(111)

    ax.plot(
        lattice_points[:, 0],
        lattice_points[:, 1],
        linestyle='none',
        marker='o',
        markersize=10,
        # color=color,
    )

    vec_color = 'tab:green'
    ax.arrow(
        0.0,
        0.0,
        vec_a1[0],
        vec_a1[1],
        head_width=0.12,
        head_length=0.2,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_a1[0]-0.1,
        vec_a1[1]-0.1,
        'a$_1$',
        fontsize=36,
        fontweight='bold',
        color=vec_color,
        )

    ax.arrow(
        0.0,
        0.0,
        vec_b1[0],
        vec_b1[1],
        head_width=0.12,
        head_length=0.2,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_b1[0]-0.15,
        vec_b1[1]+0.15,
        'b$_1$',
        fontsize=36,
        fontweight='bold',
        color=vec_color,
        )

    # ax.set_xlabel('x (a$_0$)', size=36)
    # ax.set_ylabel('y (a$_0$)', size=36)
    ax.set_xlim(left=range_x[0]-0.1, right=range_x[1]+0.1)
    ax.set_ylim(bottom=range_y[0]-0.1, top=range_y[1]+0.1)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks(ticks=np.arange(range_x[0], range_x[1]+0.1, 0.5))
    ax.set_yticks(ticks=np.arange(range_y[0], range_y[1]+0.1, 0.5))
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    ax.grid(axis='both', which='major', alpha=0.5)

    plt.tight_layout()
    if save_fig:
        plt.savefig('../plots/hw01/q_2b.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_2c(save_fig=False, show_fig=False):
    vec_a1 = np.array((0., -0.71))
    vec_b1 = np.array((0.71, 0.0))
    range_x = (-1.5, 1.5)
    range_y = (-1.5, 1.5)

    lattice_points = get_lattice_2D(
        vec_a=vec_a1,
        vec_b=vec_b1,
        range_x=range_x,
        range_y=range_y,
    )

    fig = plt.figure(
        figsize=(12, 12),
        # constrained_layout=True
    )
    ax = fig.add_subplot(111)

    ax.plot(
        lattice_points[:, 0],
        lattice_points[:, 1],
        linestyle='none',
        marker='o',
        markersize=10,
        # color=color,
    )

    vec_color = 'tab:green'
    ax.arrow(
        0.0,
        0.0,
        vec_a1[0],
        vec_a1[1],
        head_width=0.12,
        head_length=0.2,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_a1[0]-0.2,
        vec_a1[1]-0.1,
        'a$_2$',
        fontsize=36,
        fontweight='bold',
        color=vec_color,
        )

    ax.arrow(
        0.0,
        0.0,
        vec_b1[0],
        vec_b1[1],
        head_width=0.12,
        head_length=0.2,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_b1[0]-0.15,
        vec_b1[1]+0.15,
        'b$_2$',
        fontsize=36,
        fontweight='bold',
        color=vec_color,
        )

    # ax.set_xlabel('x (a$_0$)', size=36)
    # ax.set_ylabel('y (a$_0$)', size=36)
    ax.set_xlim(left=range_x[0]-0.1, right=range_x[1]+0.1)
    ax.set_ylim(bottom=range_y[0]-0.1, top=range_y[1]+0.1)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks(ticks=np.arange(range_x[0], range_x[1]+0.1, 0.5))
    ax.set_yticks(ticks=np.arange(range_y[0], range_y[1]+0.1, 0.5))
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    ax.grid(axis='both', which='major', alpha=0.5)

    plt.tight_layout()
    if save_fig:
        plt.savefig('../plots/hw01/q_2c.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_2d(save_fig=False, show_fig=False):
    vec_a3 = np.array((0.35, -0.61))
    vec_b3 = np.array((0.71, 0.0))
    range_x = (-1.5, 1.5)
    range_y = (-1.5, 1.5)

    lattice_points = get_lattice_2D(
        vec_a=vec_a3,
        vec_b=vec_b3,
        range_x=range_x,
        range_y=range_y,
    )

    fig = plt.figure(
        figsize=(12, 12),
        # constrained_layout=True
    )
    ax = fig.add_subplot(111)

    ax.plot(
        lattice_points[:, 0],
        lattice_points[:, 1],
        linestyle='none',
        marker='o',
        markersize=10,
        # color=color,
    )

    vec_color = 'tab:green'
    ax.arrow(
        0.0,
        0.0,
        vec_a3[0],
        vec_a3[1],
        head_width=0.12,
        head_length=0.2,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_a3[0]-0.2,
        vec_a3[1]-0.1,
        'a$_3$',
        fontsize=36,
        fontweight='bold',
        color=vec_color,
        )

    ax.arrow(
        0.0,
        0.0,
        vec_b3[0],
        vec_b3[1],
        head_width=0.12,
        head_length=0.2,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_b3[0]-0.15,
        vec_b3[1]+0.15,
        'b$_3$',
        fontsize=36,
        fontweight='bold',
        color=vec_color,
        )

    # ax.set_xlabel('x (a$_0$)', size=36)
    # ax.set_ylabel('y (a$_0$)', size=36)
    ax.set_xlim(left=range_x[0]-0.1, right=range_x[1]+0.1)
    ax.set_ylim(bottom=range_y[0]-0.1, top=range_y[1]+0.1)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks(ticks=np.arange(range_x[0], range_x[1]+0.1, 0.5))
    ax.set_yticks(ticks=np.arange(range_y[0], range_y[1]+0.1, 0.5))
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    ax.grid(axis='both', which='major', alpha=0.5)

    plt.tight_layout()
    if save_fig:
        plt.savefig('../plots/hw01/q_2d.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


if __name__ == '__main__':

    fig, ax = plot_2b(
        save_fig=True,
        show_fig=True,
    )
    fig, ax = plot_2c(
        save_fig=True,
        show_fig=True,
    )
    fig, ax = plot_2d(
        save_fig=True,
        show_fig=True,
    )