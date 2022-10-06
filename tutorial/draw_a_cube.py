import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Arc as plt_Arc

from utils.stereogram_utils import SimpleCube, Stereogram
from utils.plot_utils import get_fill_range_2D


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def foo():
    vertices = np.zeros([3, 8], dtype=int)
    vertices[0, :] = [1, 7, 5, 8, 2, 4, 6, 3]
    vertices[1, :] = [1, 7, 4, 6, 8, 2, 5, 3]
    vertices[2, :] = [6, 1, 5, 2, 8, 3, 7, 4]
    vertices = vertices - 1  # (adjust the indices by one since python starts with zero indexing)

    # Define an array with dimensions 8 by 3
    # 8 for each vertex
    # -> indices will be vertex1=0, v2=1, v3=2 ...
    # 3 for each coordinate
    # -> indices will be x=0,y=1,z=1
    cube = np.zeros([8, 3])

    # Define x values
    cube[:, 0] = [0, 0, 0, 0, 1, 1, 1, 1]
    # Define y values
    cube[:, 1] = [0, 1, 0, 1, 0, 1, 0, 1]
    # Define z values
    cube[:, 2] = [0, 0, 1, 1, 0, 0, 1, 1]

    # First initialize the fig variable to a figure
    fig = plt.figure()
    # Add a 3d axis to the figure
    ax = fig.add_subplot(111, projection='3d')

    # plotting cube
    # Initialize a list of vertex coordinates for each face
    # faces = [np.zeros([5,3])]*3
    faces = []
    faces.append(np.zeros([5, 3]))
    faces.append(np.zeros([5, 3]))
    faces.append(np.zeros([5, 3]))
    faces.append(np.zeros([5, 3]))
    faces.append(np.zeros([5, 3]))
    faces.append(np.zeros([5, 3]))
    # Bottom face
    faces[0][:, 0] = [0, 0, 1, 1, 0]
    faces[0][:, 1] = [0, 1, 1, 0, 0]
    faces[0][:, 2] = [0, 0, 0, 0, 0]
    # Top face
    faces[1][:, 0] = [0, 0, 1, 1, 0]
    faces[1][:, 1] = [0, 1, 1, 0, 0]
    faces[1][:, 2] = [1, 1, 1, 1, 1]
    # Left Face
    faces[2][:, 0] = [0, 0, 0, 0, 0]
    faces[2][:, 1] = [0, 1, 1, 0, 0]
    faces[2][:, 2] = [0, 0, 1, 1, 0]
    # Left Face
    faces[3][:, 0] = [1, 1, 1, 1, 1]
    faces[3][:, 1] = [0, 1, 1, 0, 0]
    faces[3][:, 2] = [0, 0, 1, 1, 0]
    # front face
    faces[4][:, 0] = [0, 1, 1, 0, 0]
    faces[4][:, 1] = [0, 0, 0, 0, 0]
    faces[4][:, 2] = [0, 0, 1, 1, 0]
    # front face
    faces[5][:, 0] = [0, 1, 1, 0, 0]
    faces[5][:, 1] = [1, 1, 1, 1, 1]
    faces[5][:, 2] = [0, 0, 1, 1, 0]
    # ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='k', alpha=.25))
    ax.add_collection3d(
        Poly3DCollection(
            faces,
            facecolors='cyan',
            # linestyles='none',
            linewidths=1,
            edgecolors='k',
            alpha=.25
        )
    )

    # # plotting lines
    # ax.plot(cube[vertices[0, :], 0], cube[vertices[0, :], 1], cube[vertices[0, :], 2], color='r')
    # ax.plot(cube[vertices[1, :], 0], cube[vertices[1, :], 1], cube[vertices[1, :], 2], color='r')
    # ax.plot(cube[vertices[2, :], 0], cube[vertices[2, :], 1], cube[vertices[2, :], 2], color='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.elev = 10
    ax.azim = 20

    print('ax.elev', ax.elev)
    print('ax.azim', ax.azim)

    plt.show()


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


def draw_cube_stereogram_framework(save_fig=False, show_fig=False):

    # start plot
    fig = plt.figure(
        figsize=(24, 12),
    )
    ax_1 = fig.add_subplot(121, projection='3d')
    ax_2 = fig.add_subplot(122)

    draw_a_cube(
        ax=ax_1,
        cube=cube_1,
    )
    draw_a_stereogram(
        ax=ax_2,
        stereogram=stereogram_1,
    )

    plt.tight_layout()

    if save_fig:
        plt.savefig('../plots/tutorial/cube_stereogram_framework.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2


def draw_cube_stereogram_1(save_fig=False, show_fig=False):

    # start plot
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        save_fig=False,
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
        save_fig=False,
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
        save_fig=False,
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
        save_fig=False,
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
        save_fig=False,
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
        save_fig=False,
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
    #     save_fig=True,
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