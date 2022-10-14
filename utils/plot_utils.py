from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import Arc as plt_Arc
from typing import (
    Union,
    Optional,
    List,
)
import numpy as np

from utils.stereogram_utils import SimpleCube, Stereogram
from utils.math_utils import get_polar_coordinate


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def fig_from_fig_or_none(
    fig: Optional[plt.Figure] = None,
    ax: Optional[plt.Axes] = None,
):
    if (ax is None) and (fig is None):
        fig = plt.figure(figsize=(12, 10), constrained_layout=True)
        ax = fig.add_subplot(111)
    elif (ax is None) and (fig is not None):
        fig = plt.figure(fig.number)
        ax = plt.gca()
    else:
        pass
    return fig, ax


def plot_a_point(
    point: np.ndarray,
    ax: plt.Axes,
    **kwargs,
):
    ax.plot(
        *point,
        **kwargs,
    )


def plot_a_line(
    point_1: np.ndarray,
    point_2: np.ndarray,
    ax: plt.Axes,
    **kwargs,
):
    # ax.plot(
    #     [point_1[0], point_2[0]],
    #     [point_1[1], point_2[1]],
    #     **kwargs,
    # )
    points = np.stack([point_1, point_2], axis=-1)
    ax.plot(
        *points,
        **kwargs,
    )


def plot_a_cell(
    starting_point: np.ndarray,
    vec_a: np.ndarray,
    vec_b: np.ndarray,
    ax: plt.Axes,
    **kwargs,
):
    plot_a_line(
        point_1=starting_point,
        point_2=starting_point+vec_a,
        ax=ax,
        **kwargs,
    )
    plot_a_line(
        point_1=starting_point,
        point_2=starting_point+vec_b,
        ax=ax,
        **kwargs,
    )
    plot_a_line(
        point_1=starting_point+vec_a,
        point_2=starting_point+vec_a+vec_b,
        ax=ax,
        **kwargs,
    )
    plot_a_line(
        point_1=starting_point+vec_b,
        point_2=starting_point+vec_a+vec_b,
        ax=ax,
        **kwargs,
    )


def get_fill_range_2D(curves: List[np.ndarray]):
    """

    :param curves:
    :return:
    """
    pts = np.concatenate(curves)
    mapping_x_range = {}
    for pt in pts:
        if pt[0] not in mapping_x_range:
            mapping_x_range[pt[0]] = {
                'min': pt[1],
                'max': pt[1],
            }
        if pt[1] < mapping_x_range[pt[0]]['min']:
            mapping_x_range[pt[0]]['min'] = pt[1]
        if pt[1] > mapping_x_range[pt[0]]['max']:
            mapping_x_range[pt[0]]['max'] = pt[1]

    pts_clean = sorted(
        mapping_x_range.items(),
        key=lambda pt: pt[0]
    )
    xs = [pt[0] for pt in pts_clean]
    y1s = [pt[1]['min'] for pt in pts_clean]
    y2s = [pt[1]['max'] for pt in pts_clean]

    return xs, y1s, y2s


def draw_a_cube(
    ax: plt.Axes,
    cube: SimpleCube,
):
    ax.add_collection3d(
        Poly3DCollection(
            cube.cube_back_faces,
            facecolors='white',
            linewidths=1.0,
            edgecolors='k',
            alpha=.0
        )
    )

    ax.add_collection3d(
        Poly3DCollection(
            cube.cube_front_faces,
            facecolors='white',
            linewidths=3.0,
            edgecolors='k',
            alpha=0.0,
        )
    )

    ax.elev = 10
    ax.azim = 20
    ax.axis('off')


def draw_a_stereogram(
    ax: plt.Axes,
    stereogram: Stereogram,
    fold_3_template=False,
):
    vis_config = {
        'color': 'tab:blue',
        'linestyle': (0, (10, 10)),
        'linewidth': 2,
    }
    circle_1 = plt.Circle(
        (0.0, 0.0),
        radius=stereogram.radius,
        fill=False,
        **vis_config,
    )
    ax.add_patch(circle_1)

    if fold_3_template:
        plot_a_line(
            point_1=get_polar_coordinate(
                radius=stereogram.radius,
                angle=np.pi / 6,
            ),
            point_2=get_polar_coordinate(
                radius=stereogram.radius,
                angle=np.pi * 7 / 6,
            ),
            ax=ax,
            **vis_config,
        )
        plot_a_line(
            point_1=get_polar_coordinate(
                radius=stereogram.radius,
                angle=-np.pi / 6,
            ),
            point_2=get_polar_coordinate(
                radius=stereogram.radius,
                angle=-np.pi * 7 / 6,
            ),
            ax=ax,
            **vis_config,
        )
    else:
        arc_1 = plt_Arc(
            (stereogram.pos_arc, 0.0),
            width=2*stereogram.radius_arc,
            height=2*stereogram.radius_arc,
            angle=180-stereogram.angle_arc/2,
            theta1=0,
            theta2=stereogram.angle_arc,
            **vis_config,
        )
        ax.add_patch(arc_1)

        arc_2 = plt_Arc(
            (-stereogram.pos_arc, 0.0),
            width=2*stereogram.radius_arc,
            height=2*stereogram.radius_arc,
            angle=-stereogram.angle_arc/2,
            theta1=0,
            theta2=stereogram.angle_arc,
            **vis_config,
        )
        ax.add_patch(arc_2)

        arc_3 = plt_Arc(
            (0.0, stereogram.pos_arc),
            width=2*stereogram.radius_arc,
            height=2*stereogram.radius_arc,
            angle=-90-stereogram.angle_arc/2,
            theta1=0,
            theta2=stereogram.angle_arc,
            **vis_config,
        )
        ax.add_patch(arc_3)

        arc_4 = plt_Arc(
            (0.0, -stereogram.pos_arc),
            width=2*stereogram.radius_arc,
            height=2*stereogram.radius_arc,
            angle=90-stereogram.angle_arc/2,
            theta1=0,
            theta2=stereogram.angle_arc,
            **vis_config,
        )
        ax.add_patch(arc_4)

        ax.plot(
            [-stereogram.radius, stereogram.radius],
            [0.0, 0.0],
            **vis_config,
        )
        ax.plot(
            [0.0, 0.0],
            [-stereogram.radius, stereogram.radius],
            **vis_config,
        )
        ax.plot(
            [-stereogram.radius*np.cos(np.pi/4), stereogram.radius*np.cos(np.pi/4)],
            [-stereogram.radius*np.sin(np.pi/4), stereogram.radius*np.sin(np.pi/4)],
            **vis_config,
        )
        ax.plot(
            [-stereogram.radius*np.cos(np.pi*3/4), stereogram.radius*np.cos(np.pi*3/4)],
            [-stereogram.radius*np.sin(np.pi*3/4), stereogram.radius*np.sin(np.pi*3/4)],
            **vis_config,
        )

    ax.set_xlim(
        left=-stereogram.radius*1.1,
        right=stereogram.radius*1.1,
    )
    ax.set_ylim(
        bottom=-stereogram.radius*1.1,
        top=stereogram.radius*1.1,
    )
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')


def draw_cube_stereogram_framework(
    cube: SimpleCube,
    stereogram: Stereogram,
    show_fig=False
):
    # start plot
    fig = plt.figure(
        figsize=(24, 12),
    )
    ax_1 = fig.add_subplot(121, projection='3d')
    ax_2 = fig.add_subplot(122)

    draw_a_cube(
        ax=ax_1,
        cube=cube,
    )
    draw_a_stereogram(
        ax=ax_2,
        stereogram=stereogram,
    )

    plt.tight_layout()

    if show_fig:
        plt.show()

    return fig, ax_1, ax_2



def draw_stereogram_framework(
    stereogram: Stereogram,
    show_fig=False,
    fold_3_template=False,
):
    # start plot
    fig = plt.figure(
        figsize=(12, 12),
    )
    ax_2 = fig.add_subplot(111)

    draw_a_stereogram(
        ax=ax_2,
        stereogram=stereogram,
        fold_3_template=fold_3_template,
    )

    plt.tight_layout()

    if show_fig:
        plt.show()

    return fig, ax_2


