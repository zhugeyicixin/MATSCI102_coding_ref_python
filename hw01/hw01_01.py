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


def plot_1a(save_fig=False, show_fig=False):

    range_x = (-8, 8)
    range_y = (-8, 8)

    lattice_points = get_lattice_2D(
        vec_a=vec_a,
        vec_b=vec_b,
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

    ax.set_xlabel('x', size=36)
    ax.set_ylabel('y', size=36)
    ax.set_xlim(left=range_x[0]-0.5, right=range_x[1]+0.5)
    ax.set_ylim(bottom=range_y[0]-0.5, top=range_y[1]+0.5)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks(ticks=np.arange(range_x[0], range_x[1]+1, 2))
    ax.set_yticks(ticks=np.arange(range_y[0], range_y[1]+1, 2))
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    ax.grid(axis='both', which='major', alpha=0.5)

    ax.invert_yaxis()

    plt.tight_layout()
    if save_fig:
        plt.savefig('../plots/hw01/q_1a.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_1b(save_fig=False, show_fig=False):
    fig, ax = plot_1a(
        save_fig=False,
        show_fig=False,
    )
    fig, ax = fig_from_fig_or_none(fig=fig, ax=ax)

    vec_color = 'tab:green'
    ax.arrow(
        0.0,
        0.0,
        vec_a[0],
        vec_a[1],
        head_width=0.3,
        head_length=0.5,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_a[0]-1,
        vec_a[1]+0.3,
        'a',
        fontsize=28,
        fontweight='bold',
        color=vec_color,
    )

    ax.arrow(
        0.0,
        0.0,
        vec_b[0],
        vec_b[1],
        head_width=0.3,
        head_length=0.5,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_b[0]-1,
        vec_b[1],
        'b',
        fontsize=28,
        fontweight='bold',
        color=vec_color,
        )

    point_color = 'tab:orange'
    ax.plot(
        0,
        0,
        linestyle='none',
        marker='o',
        markersize=10,
        color=point_color,
    )
    ax.text(
        0-1,
        0-0.3,
        '00',
        fontsize=28,
        color=point_color,
        )

    vec_1 = vec_a-vec_b
    ax.plot(
        vec_1[0],
        vec_1[1],
        linestyle='none',
        marker='o',
        markersize=10,
        color=point_color,
    )
    ax.text(
        vec_1[0]-1.0,
        vec_1[1]-0.3,
        '$1\\overline{1}$',
        fontsize=28,
        color=point_color,
    )

    # ax.invert_yaxis()

    if save_fig:
        plt.savefig('../plots/hw01/q_1b.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_1c(save_fig=False, show_fig=False):
    fig, ax = plot_1a(
        save_fig=False,
        show_fig=False,
    )
    fig, ax = fig_from_fig_or_none(fig=fig, ax=ax)

    # old vec
    vec_color = 'tab:green'
    ax.arrow(
        0.0,
        0.0,
        vec_a[0],
        vec_a[1],
        head_width=0.3,
        head_length=0.5,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_a[0]-1,
        vec_a[1]+0.3,
        'a',
        fontsize=28,
        fontweight='bold',
        color=vec_color,
        )

    ax.arrow(
        0.0,
        0.0,
        vec_b[0],
        vec_b[1],
        head_width=0.3,
        head_length=0.5,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_b[0]-1,
        vec_b[1],
        'b',
        fontsize=28,
        fontweight='bold',
        color=vec_color,
        )

    # new vec
    vec_a2 = -vec_b
    vec_b2 = vec_a + vec_b
    vec_color = 'tab:purple'
    ax.arrow(
        0.0,
        0.0,
        vec_a2[0],
        vec_a2[1],
        head_width=0.3,
        head_length=0.5,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_a2[0]-0.5,
        vec_a2[1]-0.3,
        'a\'',
        fontsize=28,
        fontweight='bold',
        color=vec_color,
        )

    ax.arrow(
        0.0,
        0.0,
        vec_b2[0],
        vec_b2[1],
        head_width=0.3,
        head_length=0.5,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_b2[0]+0.3,
        vec_b2[1]+0.1,
        'b\'',
        fontsize=28,
        fontweight='bold',
        color=vec_color,
        )

    # ax.invert_yaxis()

    if save_fig:
        plt.savefig('../plots/hw01/q_1c.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax



def plot_1d(save_fig=False, show_fig=False):
    fig, ax = plot_1a(
        save_fig=False,
        show_fig=False,
    )
    fig, ax = fig_from_fig_or_none(fig=fig, ax=ax)

    # get bisector lines
    bisector_lines = []
    near_points = np.array([
        [1, 0],
        [1, 1],
        [0, 1],
        [-1, 1],
        [-1, 0],
        [-1, -1],
        [0, -1],
        [1, -1],
    ])
    near_points = near_points@np.stack([vec_a, vec_b])
    for p in near_points:
        bisector_lines.append(get_bisector_line(
            point_end=p,
        ))
    bisector_lines = np.array(bisector_lines)

    # get intersect points
    intersection_points = []
    for line_1, line_2 in zip(
        bisector_lines[[0, 2, 3, 4, 6, 7, ]],
        bisector_lines[[2, 3, 4, 6, 7, 0, ]],
    ):
        intersection_points.append(get_line_intersection(
            line_1,
            line_2
        ))
    intersection_points = np.array(intersection_points)

    # calculate area of primitive cell
    print('area 1',
        get_polygon_area(intersection_points))

    print('area 2', get_polygon_area([
        vec_a,
        vec_a+vec_b,
        vec_b,
        [0, 0],
    ]))

    # plot
    line_color = 'tab:brown'
    for line in bisector_lines:
        ax.plot(
            line[:, 0],
            line[:, 1],
            linestyle='-',
            linewidth=1,
            color=line_color,
            alpha=0.5,
        )

    point_color = 'tab:orange'
    for p in intersection_points:
        ax.plot(
            p[0],
            p[1],
            linestyle='none',
            marker='o',
            markersize=10,
            color=point_color,
        )
    ax.add_patch(plt_Polygon(
        intersection_points,
        color=point_color,
        alpha=0.3,
    ))

    # ax.invert_yaxis()

    if save_fig:
        plt.savefig('../plots/hw01/q_1d.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


if __name__ == '__main__':

    vec_a = np.array((1.5, 1.11))
    vec_b = np.array((1.5, -1.41))

    fig, ax = plot_1a(
        save_fig=True,
        show_fig=True,
    )
    fig, ax = plot_1b(
        save_fig=True,
        show_fig=True,
    )
    fig, ax = plot_1c(
        save_fig=True,
        show_fig=True,
    )
    fig, ax = plot_1d(
        save_fig=True,
        show_fig=True,
    )
