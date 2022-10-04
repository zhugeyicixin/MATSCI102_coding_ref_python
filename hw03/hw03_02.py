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

    ax.set_xlabel('x', size=36)
    ax.set_ylabel('y', size=36)
    range_x = np.array((
        -image.shape[1] / 2 + image_shift_xy[0],
        image.shape[1] / 2 + image_shift_xy[0],
    ))
    range_y = np.array((
        -image.shape[0] / 2 + image_shift_xy[1],
        image.shape[0] / 2 + image_shift_xy[1]
    ))
    range_increment_unscaled = 10
    range_x_unscaled = np.trunc(
        range_x/scale_factor/range_increment_unscaled
    )*range_increment_unscaled
    range_y_unscaled = np.trunc(
        range_y/scale_factor/range_increment_unscaled
    )*range_increment_unscaled
    ax.set_xlim(
        left=range_x[0],
        right=range_x[1],
    )
    ax.set_ylim(
        bottom=range_y[0],
        top=range_y[1],
    )
    ax.set_xticks(
        ticks=np.arange(
            range_x_unscaled[0],
            range_x_unscaled[1]+1,
            range_increment_unscaled
        )*scale_factor,
        labels=np.arange(
            range_x_unscaled[0],
            range_x_unscaled[1]+1,
            range_increment_unscaled
        ),
    )
    ax.set_yticks(
        ticks=np.arange(
            range_y_unscaled[0],
            range_y_unscaled[1]+1,
            range_increment_unscaled
        )*scale_factor,
        labels=np.arange(
            range_y_unscaled[0],
            range_y_unscaled[1]+1,
            range_increment_unscaled
        ),
    )
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)
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
        plt.savefig('../plots/hw03/q_2_background.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_2a(save_fig=False, show_fig=False):
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
        vec_a[0] - 100,
        vec_a[1],
        'a',
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
        vec_b[1] + 35,
        'b',
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
    ellipt_marker = mpath.Path(verts, circle.codes)

    rotation_vis_config = {
        'color': op_color,
        'linestyle': 'none',
        'marker': ellipt_marker,
        'markersize': 20,
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
        plt.savefig('../plots/hw03/q_2a.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_2c(save_fig=False, show_fig=False):
    # plotting params
    range_a = (-15, 15)
    range_b = (-15, 15)

    lattice_points = get_lattice_2D(
        vec_a=reciprocal_a,
        vec_b=reciprocal_b,
        range_a=range_a,
        range_b=range_b,
    )

    fig = plt.figure(
        figsize=(12, 8.5),
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
        point_2=reciprocal_a,
        ax=ax,
        **edge_vis_config,
    )
    plot_a_line(
        point_1=origin,
        point_2=reciprocal_b,
        ax=ax,
        **edge_vis_config,
    )
    plot_a_line(
        point_1=reciprocal_a,
        point_2=reciprocal_a + reciprocal_b,
        ax=ax,
        **edge_vis_config,
    )
    plot_a_line(
        point_1=reciprocal_b,
        point_2=reciprocal_a + reciprocal_b,
        ax=ax,
        **edge_vis_config,
    )

    # add lattice vectors
    vec_color = 'tab:blue'
    origin = np.array((0.0, 0.0))
    ax.arrow(
        origin[0],
        origin[1],
        reciprocal_a[0],
        reciprocal_a[1],
        head_width=3,
        head_length=5,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        reciprocal_a[0]-15,
        reciprocal_a[1]-10,
        'a*',
        fontsize=36,
        fontweight='bold',
        color=vec_color,
        )
    ax.arrow(
        origin[0],
        origin[1],
        reciprocal_b[0],
        reciprocal_b[1],
        head_width=3,
        head_length=5,
        linewidth=5,
        facecolor=vec_color,
        edgecolor=vec_color,
        head_starts_at_zero=False,
        length_includes_head=True,
    )
    ax.text(
        reciprocal_b[0],
        reciprocal_b[1] + 5,
        'b*',
        fontsize=36,
        fontweight='bold',
        color=vec_color,
        )

    # add XRD
    vis_config_Cl = {
        'color': 'tab:green',
        'linestyle': 'none',
        'marker': 'x',
        'markersize': 20,
        'markeredgewidth': 3,
    }
    vis_config_Na = {
        'color': 'tab:blue',
        'linestyle': 'none',
        'marker': 'o',
        'fillstyle': 'none',
        'markersize': 20,
        'markeredgewidth': 2,
    }
    for h in range(range_a[0], range_a[1]+1):
        for k in range(range_b[0], range_b[1]+1):
            pt = h*reciprocal_a + k*reciprocal_b
            # reflection for Cl
            if (
                (((h+k) % 2) == 0)
                and (h % 4 != 2)
                and (k % 10 != 5)
            ):
                plot_a_point(
                    point=pt,
                    ax=ax,
                    **vis_config_Cl,
                )
            # reflection for Na
            if (
                (h % 2 == 0)
                and (k % 2 == 0)
            ):
                plot_a_point(
                    point=pt,
                    ax=ax,
                    **vis_config_Na,
                )

    ax.set_xlabel('x', size=32)
    ax.set_ylabel('y', size=32)
    range_x_unscaled = np.array((-3.3, 3.3))
    range_y_unscaled = np.array((-2.5, 2.5))
    range_x = range_x_unscaled*scale_factor
    range_y = range_y_unscaled*scale_factor
    range_increment_unscaled = 1
    range_x_unscaled = np.trunc(
        range_x_unscaled/range_increment_unscaled
    )*range_increment_unscaled
    range_y_unscaled = np.trunc(
        range_y_unscaled/range_increment_unscaled
    )*range_increment_unscaled

    ax.set_xlim(
        left=range_x[0],
        right=range_x[1],
    )
    ax.set_ylim(
        bottom=range_y[0],
        top=range_y[1],
    )
    ax.set_xticks(
        ticks=np.arange(
            range_x_unscaled[0],
            range_x_unscaled[1]+1,
            range_increment_unscaled
        )*scale_factor,
        labels=np.arange(
            range_x_unscaled[0],
            range_x_unscaled[1]+1,
            range_increment_unscaled
        ),
    )
    ax.set_yticks(
        ticks=np.arange(
            range_y_unscaled[0],
            range_y_unscaled[1]+1,
            range_increment_unscaled
        )*scale_factor,
        labels=np.arange(
            range_y_unscaled[0],
            range_y_unscaled[1]+1,
            range_increment_unscaled
        ),
    )
    ax.tick_params(axis='x', which='major', labelsize=26)
    ax.tick_params(axis='y', which='major', labelsize=26)
    ax.set_aspect('equal', adjustable='box')

    plt.tight_layout()

    if save_fig:
        plt.savefig('../plots/hw03/q_2c.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


if __name__ == '__main__':

    show_axis = False
    path_image = '../rsc/hw03/q2.png'
    image_shift_xy = (8.0, 8.0)
    vec_a = np.array((0, -1.0))*242
    vec_b = np.array((1.0, 0.0))*485
    primitive_a = vec_a
    primitive_b = (-vec_a+vec_b)/2.0
    scale_factor = np.linalg.norm(vec_b)/16

    reciprocal_a = (
        np.array((0, -1.0))*scale_factor**2
        *2*np.pi/np.linalg.norm(vec_a)
    )
    reciprocal_b = (
        np.array((1.0, 0.0))*scale_factor**2
        *2*np.pi/np.linalg.norm(vec_b)
    )

    # cross_bc = np.array((vec_b[1], -vec_b[0]))
    # reciprocal_a = (
    #     2*np.pi*scale_factor**2
    #     *cross_bc/np.dot(vec_a, cross_bc)
    # )
    # cross_ca = np.array((-vec_a[1], vec_a[0]))
    # reciprocal_b = (
    #     2 * np.pi * scale_factor ** 2
    #     * cross_ca / np.dot(vec_b, cross_ca)
    # )

    # cross_bc = np.array((primitive_b[1], -primitive_b[0]))
    # reciprocal_a = (
    #     2*np.pi*scale_factor**2
    #     *cross_bc/np.dot(primitive_a, cross_bc)
    # )
    # cross_ca = np.array((-primitive_a[1], primitive_a[0]))
    # reciprocal_b = (
    #     2 * np.pi * scale_factor ** 2
    #     * cross_ca / np.dot(primitive_b, cross_ca)
    # )

    print('scale_factor', scale_factor)
    print('reciprocal_a', reciprocal_a)
    print('reciprocal_b', reciprocal_b)

    # fig, ax = plot_framework(
    #     save_fig=True,
    #     show_fig=True,
    # )

    fig, ax = plot_2a(
        save_fig=True,
        show_fig=True,
    )

    fig, ax = plot_2c(
        save_fig=True,
        show_fig=True,
    )


