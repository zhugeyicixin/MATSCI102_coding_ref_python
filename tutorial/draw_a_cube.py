import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Arc as plt_Arc

from utils.stereogram_utils import SimpleCube, Stereogram
from utils.plot_utils import get_fill_range_2D
from utils.plot_utils import draw_cube_stereogram_framework


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def draw_cube_stereogram_1(save_fig=False, show_fig=False):

    # start plot
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )
    areas_to_paint = [
        '4_47_4567',
        '4_45_4567',
        '5_45_4567',
        '5_56_4567',
        '6_56_4567',
        '6_67_4567',
        '7_67_4567',
        '7_47_4567',
        '4_47_2347',
        '4_34_2347',
        '7_47_2347',
        '7_27_2347',
        '7_27_1267',
        '7_67_1267',
        '6_67_1267',
        '6_16_1267',
    ]

    facecolors = plt.colormaps['tab20'].colors[: len(areas_to_paint)]

    # paint on cube
    areas_on_cube = np.array([
        cube_1.get_vertices_of_area(area)
        for area in areas_to_paint
    ])

    ax_1.add_collection3d(
        Poly3DCollection(
            areas_on_cube,
            facecolors=facecolors,
            linewidths=3,
            edgecolors='k',
            alpha=1.0
        )
    )

    # paint on stereogram
    for i, area in enumerate(areas_to_paint):
        xs, y1s, y2s = get_fill_range_2D(
            stereogram_1.get_edges_of_area(area)
        )
        ax_2.fill_between(
            x=xs, y1=y1s, y2=y2s, color=facecolors[i]
        )

    if save_fig:
        plt.savefig('../plots/tutorial/cube_stereogram_1.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2



def draw_cube_stereogram_2(save_fig=False, show_fig=False):

    # start plot
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )
    areas_to_paint = [
        '4_34_0345',
        '4_45_0345',
        '5_45_0345',
        '5_05_0345',
        '5_05_0156',
        '5_56_0156',
        '6_56_0156',
        '6_16_0156',
    ]

    facecolors = plt.colormaps['tab20'].colors[: len(areas_to_paint)]

    # paint on cube
    areas_on_cube = np.array([
        cube_1.get_vertices_of_area(area)
        for area in areas_to_paint
    ])

    ax_1.add_collection3d(
        Poly3DCollection(
            areas_on_cube,
            facecolors=facecolors,
            linewidths=1,
            edgecolors='k',
            alpha=1.0
        )
    )

    # paint on stereogram
    for i, area in enumerate(areas_to_paint):
        xs, y1s, y2s = get_fill_range_2D(
            stereogram_1.get_edges_of_area(area)
        )
        ax_2.fill_between(
            x=xs, y1=y1s, y2=y2s, color=facecolors[i]
        )

    if save_fig:
        plt.savefig('../plots/tutorial/cube_stereogram_2.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2


def draw_cube_stereogram_3(save_fig=False, show_fig=False):

    # start plot
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )
    areas_to_paint = [
        '3_23_2347',
        '3_34_2347',
        '2_23_2347',
        '2_27_2347',
        '2_27_1267',
        '2_12_1267',
        '1_12_1267',
        '1_16_1267',
    ]

    facecolors = plt.colormaps['tab20'].colors[: len(areas_to_paint)]

    # paint on cube
    areas_on_cube = np.array([
        cube_1.get_vertices_of_area(area)
        for area in areas_to_paint
    ])

    ax_1.add_collection3d(
        Poly3DCollection(
            areas_on_cube,
            facecolors=facecolors,
            linewidths=1,
            edgecolors='k',
            alpha=1.0
        )
    )

    # paint on stereogram
    for i, area in enumerate(areas_to_paint):
        xs, y1s, y2s = get_fill_range_2D(
            stereogram_1.get_edges_of_area(area)
        )
        ax_2.fill_between(
            x=xs, y1=y1s, y2=y2s, color=facecolors[i]
        )

    if save_fig:
        plt.savefig('../plots/tutorial/cube_stereogram_3.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2



def draw_cube_stereogram_4(save_fig=False, show_fig=False):

    # start plot
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )
    areas_to_paint = [
        '3_23_0123',
        '3_03_0123',
        '0_03_0123',
        '0_01_0123',
        '1_01_0123',
        '1_12_0123',
        '2_12_0123',
        '2_23_0123',
        '3_34_0345',
        '3_03_0345',
        '0_03_0345',
        '0_05_0345',
        '0_05_0156',
        '0_01_0156',
        '1_01_0156',
        '1_16_0156',
    ]

    facecolors = plt.colormaps['tab20'].colors[: len(areas_to_paint)]

    # paint on cube
    areas_on_cube = np.array([
        cube_1.get_vertices_of_area(area)
        for area in areas_to_paint
    ])

    ax_1.add_collection3d(
        Poly3DCollection(
            areas_on_cube,
            facecolors=facecolors,
            linewidths=1,
            edgecolors='k',
            alpha=1.0
        )
    )

    # paint on stereogram
    for i, area in enumerate(areas_to_paint):
        xs, y1s, y2s = get_fill_range_2D(
            stereogram_1.get_edges_of_area(area)
        )
        ax_2.fill_between(
            x=xs, y1=y1s, y2=y2s, color=facecolors[i]
        )

    if save_fig:
        plt.savefig('../plots/tutorial/cube_stereogram_4.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2



def draw_cube_stereogram_5(save_fig=False, show_fig=False):

    # start plot
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )
    points_to_paint = list(filter(
        lambda x: len(set(x)&{'0', '1', '2', '3'})/len(x) < 1,
        stereogram_1.important_points
    ))

    all_colors = plt.colormaps['tab20'].colors[: len(points_to_paint)]

    # paint on cube
    for i, pt in enumerate(points_to_paint):
        ax_1.plot(
            cube_1.important_points[pt][0],
            cube_1.important_points[pt][1],
            cube_1.important_points[pt][2],
            'X',
            color=all_colors[i],
            markersize=50,
        )

    # paint on stereogram
    for i, pt in enumerate(points_to_paint):
        ax_2.plot(
            stereogram_1.important_points[pt][0],
            stereogram_1.important_points[pt][1],
            'X',
            color=all_colors[i],
            markersize=50,
        )

    if save_fig:
        plt.savefig('../plots/tutorial/cube_stereogram_5.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2



def draw_cube_stereogram_6(save_fig=False, show_fig=False):

    # start plot
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )
    points_to_paint = list(filter(
        lambda x: len(set(x)&{'0', '1', '2', '3'})/len(x) == 1,
        stereogram_1.important_points
    ))

    all_colors = plt.colormaps['tab20'].colors[: len(points_to_paint)]

    # paint on cube
    for i, pt in enumerate(points_to_paint):
        ax_1.plot(
            cube_1.important_points[pt][0],
            cube_1.important_points[pt][1],
            cube_1.important_points[pt][2],
            'o',
            color=all_colors[i],
            markersize=30,
            fillstyle='none',
            markeredgewidth=5,
        )

    # paint on stereogram
    for i, pt in enumerate(points_to_paint):
        ax_2.plot(
            stereogram_1.important_points[pt][0],
            stereogram_1.important_points[pt][1],
            'o',
            color=all_colors[i],
            markersize=30,
            fillstyle='none',
            markeredgewidth=5,
        )

    if save_fig:
        plt.savefig('../plots/tutorial/cube_stereogram_6.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2


if __name__ == '__main__':

    cube_1 = SimpleCube(scale=1)
    stereogram_1 = Stereogram(radius=1)

    # fig, ax_1, ax_2 = draw_cube_stereogram_framework(
    #     cube=cube_1,
    #     stereogram=stereogram_1,
    #     show_fig=True,
    # )

    fig, ax_1, ax_2 = draw_cube_stereogram_1(
        save_fig=True,
        show_fig=True,
    )

    fig, ax_1, ax_2 = draw_cube_stereogram_2(
        save_fig=True,
        show_fig=True,
    )

    fig, ax_1, ax_2 = draw_cube_stereogram_3(
        save_fig=True,
        show_fig=True,
    )

    fig, ax_1, ax_2 = draw_cube_stereogram_4(
        save_fig=True,
        show_fig=True,
    )

    fig, ax_1, ax_2 = draw_cube_stereogram_5(
        save_fig=True,
        show_fig=True,
    )

    fig, ax_1, ax_2 = draw_cube_stereogram_6(
        save_fig=True,
        show_fig=True,
    )