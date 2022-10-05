import numpy as np
from matplotlib import pyplot as plt
import matplotlib.path as mpath
from pprint import pprint

from utils.lattice_utils import get_lattice_2D
from utils.plot_utils import fig_from_fig_or_none
from utils.plot_utils import plot_a_point
from utils.plot_utils import plot_a_line


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def plot_framework(
    save_fig=False,
    show_fig=False,
):
    fig = plt.figure(
        figsize=(12, 8.5),
    )
    ax = fig.add_subplot(111)

    image = plt.imread(path_image)
    ax.imshow(
        image,
        extent=[
            -image.shape[1]/2+image_shift_xy[0],
            image.shape[1]/2+image_shift_xy[0],
            -image.shape[0]/2+image_shift_xy[1],
            image.shape[0]/2+image_shift_xy[1],
        ]
    )

    ax.set_xlim(
        left=-image.shape[1] / 2 + image_shift_xy[0],
        right=image.shape[1] / 2 + image_shift_xy[0],
    )
    ax.set_ylim(
        bottom=-image.shape[0] / 2 + image_shift_xy[1],
        top=image.shape[0] / 2 + image_shift_xy[1],
    )
    ax.set_aspect('equal', adjustable='box')

    if not show_axis:
        ax.axis('off')
    else:
        ax.plot(
            [0, 0],
            [-500, 500],
        )
        ax.plot(
            [-500, 500],
            [0, 0],
        )
        origin = np.array((0.0, 0.0))
        edge_vis_config = {}
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

    plt.tight_layout()

    if save_fig:
        plt.savefig('../plots/hw03/q_1_background.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_1a(save_fig=False, show_fig=False):
    # plotting params
    range_a = (-10, 10)
    range_b = (-10, 10)

    lattice_points = get_lattice_2D(
        vec_a=primitive_a,
        vec_b=primitive_b,
        range_a=range_a,
        range_b=range_b,
    )

    fig, ax = plot_framework(
        save_fig=False,
        show_fig=False,
    )
    fig, ax = fig_from_fig_or_none(fig=fig, ax=ax)

    # draw lattice points
    ax.plot(
        lattice_points[:, 0],
        lattice_points[:, 1],
        linestyle='none',
        marker='o',
        markersize=8,
        color='tab:gray',
    )

    if save_fig:
        plt.savefig('../plots/hw03/q_1a.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_1b(save_fig=False, show_fig=False):
    fig, ax = plot_1a(
        save_fig=False,
        show_fig=False,
    )
    fig, ax = fig_from_fig_or_none(fig=fig, ax=ax)

    # add primitive cell
    edge_vis_config = {
        'color': 'tab:gray',
    }
    origin = np.array((0.0, 0.0))
    plot_a_line(
        point_1=origin,
        point_2=primitive_a,
        ax=ax,
        **edge_vis_config,
    )
    plot_a_line(
        point_1=origin,
        point_2=primitive_b,
        ax=ax,
        **edge_vis_config,
    )
    plot_a_line(
        point_1=primitive_a,
        point_2=primitive_a+primitive_b,
        ax=ax,
        **edge_vis_config,
    )
    plot_a_line(
        point_1=primitive_b,
        point_2=primitive_a+primitive_b,
        ax=ax,
        **edge_vis_config,
    )

    # add lattice vectors
    vec_color = 'tab:blue'
    origin = np.array((0.0, 0.0))
    ax.arrow(
        origin[0],
        origin[1],
        primitive_a[0],
        primitive_a[1],
        head_width=18,
        head_length=30,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        primitive_a[0]-120,
        primitive_a[1],
        'a$_1$',
        fontsize=48,
        fontweight='bold',
        color=vec_color,
        )

    ax.arrow(
        origin[0],
        origin[1],
        primitive_b[0],
        primitive_b[1],
        head_width=18,
        head_length=30,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        primitive_b[0]-70,
        primitive_b[1]+25,
        'b$_1$',
        fontsize=48,
        fontweight='bold',
        color=vec_color,
        )

    if save_fig:
        plt.savefig('../plots/hw03/q_1b.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax

def plot_1d(save_fig=False, show_fig=False):
    fig, ax = plot_1a(
        save_fig=False,
        show_fig=False,
    )
    fig, ax = fig_from_fig_or_none(fig=fig, ax=ax)

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
        point_2=vec_a + vec_b,
        ax=ax,
        **edge_vis_config,
    )
    plot_a_line(
        point_1=vec_b,
        point_2=vec_a + vec_b,
        ax=ax,
        **edge_vis_config,
    )

    # add lattice vectors
    vec_color = 'tab:blue'
    origin = np.array((0.0, 0.0))
    ax.arrow(
        origin[0],
        origin[1],
        vec_a[0],
        vec_a[1],
        head_width=18,
        head_length=30,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_a[0] - 120,
        vec_a[1],
        'a$_2$',
        fontsize=48,
        fontweight='bold',
        color=vec_color,
    )

    ax.arrow(
        origin[0],
        origin[1],
        vec_b[0],
        vec_b[1],
        head_width=18,
        head_length=30,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        vec_b[0] - 50,
        vec_b[1] + 15,
        'b$_2$',
        fontsize=48,
        fontweight='bold',
        color=vec_color,
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
        point_2=vec_a,
        ax=ax,
        **mirror_vis_config,
    )
    plot_a_line(
        point_1=origin,
        point_2=vec_b,
        ax=ax,
        **mirror_vis_config,
    )
    plot_a_line(
        point_1=vec_a,
        point_2=vec_a+vec_b,
        ax=ax,
        **mirror_vis_config,
    )
    plot_a_line(
        point_1=vec_b,
        point_2=vec_a+vec_b,
        ax=ax,
        **mirror_vis_config,
    )
    plot_a_line(
        point_1=vec_b/2.0,
        point_2=vec_a+vec_b/2.0,
        ax=ax,
        **mirror_vis_config,
    )
    plot_a_line(
        point_1=vec_a/2.0,
        point_2=vec_a/2.0+vec_b,
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
        point_1=vec_a/4.0,
        point_2=vec_a/4.0+vec_b,
        ax=ax,
        **glide_vis_config,
    )
    plot_a_line(
        point_1=vec_a*3.0/4.0,
        point_2=vec_a*3.0/4.0+vec_b,
        ax=ax,
        **glide_vis_config,
    )
    plot_a_line(
        point_1=vec_b/4.0,
        point_2=vec_a+vec_b/4.0,
        ax=ax,
        **glide_vis_config,
    )
    plot_a_line(
        point_1=vec_b*3.0/4.0,
        point_2=vec_a+vec_b*3.0/4.0,
        ax=ax,
        **glide_vis_config,
    )

    # plot rotation axes
    # Define the ellipse marker.
    circle = mpath.Path.unit_circle()
    verts = np.copy(circle.vertices)
    verts[:, 1] *= 1.618
    # ellipt_marker = mpath.Path(verts, circle.codes)
    ellipt_marker = mpath.Path(verts)

    rotation_vis_config = {
        'color': op_color,
        'linestyle': 'none',
        'marker': ellipt_marker,
        'markersize': 15,
        # 'fillstyle': 'none',
    }
    for pt in [
        origin,
        vec_a/2.0,
        vec_a,
        vec_a/4.0+vec_b/4.0,
        vec_a*3.0/4.0+vec_b/4.0,
        vec_b/2.0,
        vec_a/2.0+vec_b/2.0,
        vec_a+vec_b/2.0,
        vec_a / 4.0 + vec_b*3.0 / 4.0,
        vec_a * 3.0 / 4.0 + vec_b*3.0 / 4.0,
        vec_b,
        vec_a/2.0+vec_b,
        vec_a+vec_b,
    ]:
        plot_a_point(
            point=pt,
            ax=ax,
            **rotation_vis_config,
        )


    if save_fig:
        plt.savefig('../plots/hw03/q_1d.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


if __name__ == '__main__':

    show_axis = False
    path_image = '../rsc/hw03/q1.png'
    image_shift_xy = (3.0, -5.0)
    vec_a = np.array((0, -1.0))*127
    vec_b = np.array((1.0, 0.0))*732
    primitive_a = vec_a
    primitive_b = (-vec_a+vec_b)/2.0

    # fig, ax = plot_framework(
    #     save_fig=True,
    #     show_fig=True,
    # )

    fig, ax = plot_1a(
        save_fig=True,
        show_fig=True,
    )

    fig, ax = plot_1b(
        save_fig=True,
        show_fig=True,
    )

    fig, ax = plot_1d(
        save_fig=True,
        show_fig=True,
    )