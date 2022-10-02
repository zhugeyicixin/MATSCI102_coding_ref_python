import numpy as np
from matplotlib import pyplot as plt
from pprint import pprint

from utils.lattice_utils import get_lattice_2D
from utils.plot_utils import fig_from_fig_or_none
from utils.plot_utils import plot_a_point
from utils.plot_utils import plot_a_line


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def plot_2a(save_fig=False, show_fig=False):
    # plotting params
    range_a = (-5, 5)
    range_b = (-5, 5)

    lattice_points = get_lattice_2D(
        vec_a=vec_a,
        vec_b=vec_b,
        range_a=range_a,
        range_b=range_b,
    )

    fig = plt.figure(
        figsize=(12, 12),
    )
    ax = fig.add_subplot(111)

    # draw lattice points
    ax.plot(
        lattice_points[:, 0],
        lattice_points[:, 1],
        linestyle='none',
        marker='o',
        markersize=8,
        color='tab:gray',
    )

    # add primitive cell
    edge_vis_config = {
        'color': 'tab:gray',
    }
    origin = np.array((0.0, 0.0))
    plot_a_line(
        point_1=origin,
        point_2=vec_a,
        ax=ax,
        **edge_vis_config,
    )
    plot_a_line(
        point_1=origin,
        point_2=vec_b,
        ax=ax,
        **edge_vis_config,
    )
    plot_a_line(
        point_1=vec_a,
        point_2=vec_a+vec_b,
        ax=ax,
        **edge_vis_config,
    )
    plot_a_line(
        point_1=vec_b,
        point_2=vec_a+vec_b,
        ax=ax,
        **edge_vis_config,
    )

    # add lattice vectors
    vec_color = 'tab:green'
    origin = np.array((0.0, 0.0))
    ax.arrow(
        origin[0],
        origin[1],
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
        vec_a[0]-0.5,
        vec_a[1],
        'a',
        fontsize=28,
        fontweight='bold',
        color=vec_color,
        )

    ax.arrow(
        origin[0],
        origin[1],
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
        vec_b[0]-0.5,
        vec_b[1]+0.3,
        'b',
        fontsize=28,
        fontweight='bold',
        color=vec_color,
        )

    ax.set_xlabel('x', size=36)
    ax.set_ylabel('y', size=36)
    # ax.set_xlim(left=-7, right=7)
    # ax.set_ylim(bottom=-7, top=7)
    ax.set_xlim(left=-5, right=5)
    ax.set_ylim(bottom=-5, top=5)
    ax.set_aspect('equal', adjustable='box')
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
    ax.grid(axis='both', which='major', alpha=0.5)

    plt.tight_layout()
    if save_fig:
        plt.savefig('../plots/hw02/q_2a.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_2b(save_fig=False, show_fig=False):
    # init
    # cell params
    site_1 = np.array((1.0/3.0, 2.0/3.0))
    site_2 = np.array((2.0/3.0, 1.0/3.0))
    edge_1_1 = np.array((2.0/3.0, 1.0/3.0))
    edge_1_2 = np.array((1.0/3.0, 2.0/3.0))
    edge_2_1 = np.array((2.0/3.0, 1.0/3.0))
    edge_2_2 = np.array((1.0/3.0, -1.0/3.0))
    edge_3_1 = np.array((2.0/3.0, 1.0/3.0))
    edge_3_2 = np.array((4.0/3.0, 2.0/3.0))
    # plotting params
    range_a = (-5, 5)
    range_b = (-5, 5)

    # math transformation
    vec_cell = np.stack([vec_a, vec_b])
    site_1 = site_1 @ vec_cell
    site_2 = site_2 @ vec_cell
    edge_1_1 = edge_1_1 @ vec_cell
    edge_1_2 = edge_1_2 @ vec_cell
    edge_2_1 = edge_2_1 @ vec_cell
    edge_2_2 = edge_2_2 @ vec_cell
    edge_3_1 = edge_3_1 @ vec_cell
    edge_3_2 = edge_3_2 @ vec_cell

    # loop to get array of points
    lattice_points = get_lattice_2D(
        vec_a=vec_a,
        vec_b=vec_b,
        range_a=range_a,
        range_b=range_b,
    )
    site_1_points = site_1 + lattice_points
    site_2_points = site_2 + lattice_points
    edge_1_1_points = edge_1_1 + lattice_points
    edge_1_2_points = edge_1_2 + lattice_points
    edge_2_1_points = edge_2_1 + lattice_points
    edge_2_2_points = edge_2_2 + lattice_points
    edge_3_1_points = edge_3_1 + lattice_points
    edge_3_2_points = edge_3_2 + lattice_points

    fig, ax = plot_2a(
        save_fig=False,
        show_fig=False,
    )
    fig, ax = fig_from_fig_or_none(fig=fig, ax=ax)

    # plot edges
    edge_vis_config = {
        'color': 'tab:purple',
    }
    for i in range(len(edge_1_1_points)):
        plot_a_line(
            point_1=edge_1_1_points[i],
            point_2=edge_1_2_points[i],
            ax=ax,
            **edge_vis_config,
        )

    for i in range(len(edge_2_1_points)):
        plot_a_line(
            point_1=edge_2_1_points[i],
            point_2=edge_2_2_points[i],
            ax=ax,
            **edge_vis_config,
        )

    for i in range(len(edge_3_1_points)):
        plot_a_line(
            point_1=edge_3_1_points[i],
            point_2=edge_3_2_points[i],
            ax=ax,
            **edge_vis_config,
        )

    # plot points
    atom_color = 'tab:blue'
    ax.plot(
        site_1_points[:, 0],
        site_1_points[:, 1],
        linestyle='none',
        marker='o',
        markersize=15,
        color=atom_color,
    )
    ax.text(
        (site_1-vec_a-vec_b)[0]+0.2,
        (site_1-vec_a-vec_b)[1],
        'B',
        fontsize=28,
        fontweight='bold',
        color=atom_color,
    )

    atom_color = 'tab:orange'
    ax.plot(
        site_2_points[:, 0],
        site_2_points[:, 1],
        linestyle='none',
        marker='o',
        markersize=15,
        color=atom_color,
    )
    ax.text(
        (site_2-vec_a-vec_b)[0]-0.7,
        (site_2-vec_a-vec_b)[1]-0.3,
        'N',
        fontsize=28,
        fontweight='bold',
        color=atom_color,
    )

    # plot symmetry operations
    op_color = 'black'
    origin = np.array((0.0, 0.0))

    # plot mirrors
    mirror_vis_config = {
        'color': op_color,
        'linewidth': 5,
    }
    plot_a_line(
        point_1=origin,
        point_2=vec_a + vec_b/2,
        ax=ax,
        **mirror_vis_config,
    )
    plot_a_line(
        point_1=origin,
        point_2=vec_a/2 + vec_b,
        ax=ax,
        **mirror_vis_config,
    )
    plot_a_line(
        point_1=vec_a,
        point_2=vec_b,
        ax=ax,
        **mirror_vis_config,
    )
    plot_a_line(
        point_1=vec_a + vec_b,
        point_2=vec_b/2,
        ax=ax,
        **mirror_vis_config,
    )

    # plot gliding planes
    glide_vis_config = {
        'color': op_color,
        'linestyle': '--',
        'linewidth': 3,
    }
    plot_a_line(
        point_1=vec_a/2,
        point_2=vec_b/2,
        ax=ax,
        **glide_vis_config,
    )
    plot_a_line(
        point_1=vec_a + vec_b/2,
        point_2=vec_a/2 + vec_b,
        ax=ax,
        **glide_vis_config,
    )
    plot_a_line(
        point_1=vec_a/2,
        point_2=vec_a + vec_b/4,
        ax=ax,
        **glide_vis_config,
    )
    plot_a_line(
        point_1=vec_b/4,
        point_2=vec_a + vec_b*3/4,
        ax=ax,
        **glide_vis_config,
    )
    plot_a_line(
        point_1=vec_b*3/4,
        point_2=vec_a/2 + vec_b,
        ax=ax,
        **glide_vis_config,
    )
    plot_a_line(
        point_1=vec_a*3/4,
        point_2=vec_a + vec_b/2,
        ax=ax,
        **glide_vis_config,
    )
    plot_a_line(
        point_1=vec_a/4,
        point_2=vec_a*3/4 + vec_b,
        ax=ax,
        **glide_vis_config,
    )
    plot_a_line(
        point_1=vec_b/2,
        point_2=vec_a/4 + vec_b,
        ax=ax,
        **glide_vis_config,
    )

    # plot rotation axes
    rotation_vis_config = {
        'color': op_color,
        'linestyle': 'none',
        'marker': '^',
        'markersize': 30,
    }
    plot_a_point(
        point=origin,
        ax=ax,
        **rotation_vis_config,
    )
    plot_a_point(
        point=vec_a,
        ax=ax,
        **rotation_vis_config,
    )
    plot_a_point(
        point=vec_b,
        ax=ax,
        **rotation_vis_config,
    )
    plot_a_point(
        point=vec_a+vec_b,
        ax=ax,
        **rotation_vis_config,
    )
    plot_a_point(
        point=vec_a*2/3+vec_b/3,
        ax=ax,
        **rotation_vis_config,
    )
    plot_a_point(
        point=vec_a/3+vec_b*2/3,
        ax=ax,
        **rotation_vis_config,
    )

    if save_fig:
        plt.savefig('../plots/hw02/q_2b.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


if __name__ == '__main__':

    vec_a = np.array((-0.5, -np.sqrt(3)/2))*2.5
    vec_b = np.array((1.0, 0.0))*2.5

    fig, ax = plot_2a(
        save_fig=True,
        show_fig=True,
    )

    fig, ax = plot_2b(
        save_fig=True,
        show_fig=True,
    )

