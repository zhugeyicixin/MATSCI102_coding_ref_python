import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.path as mpath
from matplotlib.patches import Arc as plt_Arc

from utils.stereogram_utils import SimpleCube, Stereogram
from utils.plot_utils import draw_cube_stereogram_framework
from utils.plot_utils import draw_stereogram_framework
from utils.plot_utils import plot_a_point, plot_a_line
from utils.lattice_utils import get_coordinate_by_combination
from utils.math_utils import get_polar_coordinate
from utils.math_utils import tensor_transformation


def plot_2a(save_fig=False, show_fig=False):
    fig, ax = draw_stereogram_framework(
        stereogram=stereogram_1,
        show_fig=False,
        fold_3_template=False,
    )

    # plot symmetry element
    symmetry_color = 'tab:green'

    # plot rotation
    # Define the ellipse marker.
    circle = mpath.Path.unit_circle()
    verts = np.copy(circle.vertices)
    verts[:, 1] *= 1.618
    # ellipt_marker = mpath.Path(verts, circle.codes)
    ellipt_marker = mpath.Path(verts)
    symmetry_vis_config_1 = {
        'color': symmetry_color,
        'marker': ellipt_marker,
        'markersize': 45,
    }
    ellipt_marker_2 = ellipt_marker.transformed(
        mpl.transforms.Affine2D().rotate_deg(90)
    )
    symmetry_vis_config_2 = {
        **symmetry_vis_config_1,
        'marker': ellipt_marker_2,
    }
    plot_a_point(
        point=get_polar_coordinate(
            radius=stereogram_1.radius,
            angle=np.pi/2,
        ),
        ax=ax,
        **symmetry_vis_config_2,
    )
    plot_a_point(
        point=get_polar_coordinate(
            radius=stereogram_1.radius,
            angle=np.pi/2+np.pi,
        ),
        ax=ax,
        **symmetry_vis_config_2,
    )

    symmetry_vis_config_3 = {
        'color': symmetry_color,
        'marker': '^',
        'markersize': 50,
    }
    plot_a_point(
        point=stereogram_1.important_points['4'],
        ax=ax,
        **symmetry_vis_config_3,
    )

    if save_fig:
        plt.savefig('../plots/quiz/q_2a.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_2a_solution(save_fig=False, show_fig=False):
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )

    # plotting params
    points_to_paint = [
        {
            'combination': {
                '4': 5.0 / 12.0,
                '45': 5.0 / 12.0,
                '0345': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '4': 5.0 / 12.0,
                '47': 5.0 / 12.0,
                '4567': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '4': 5.0 / 12.0,
                '34': 5.0 / 12.0,
                '2347': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '0': 5.0 / 12.0,
                '03': 5.0 / 12.0,
                '0345': 2.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '0': 5.0 / 12.0,
                '05': 5.0 / 12.0,
                '0156': 2.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '0': 5.0 / 12.0,
                '01': 5.0 / 12.0,
                '0123': 2.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '6': 5.0 / 12.0,
                '56': 5.0 / 12.0,
                '4567': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '6': 5.0 / 12.0,
                '16': 5.0 / 12.0,
                '0156': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '6': 5.0 / 12.0,
                '67': 5.0 / 12.0,
                '1267': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '2': 5.0 / 12.0,
                '12': 5.0 / 12.0,
                '1267': 2.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '2': 5.0 / 12.0,
                '23': 5.0 / 12.0,
                '0123': 2.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '2': 5.0 / 12.0,
                '27': 5.0 / 12.0,
                '2347': 2.0 / 12.0,
            },
            'above_equatorial': False,
        },

    ]

    # paint on cube
    cube_pt_above_vis_config = {
        'marker': 'X',
        'color': 'black',
        'markersize': 25,
    }
    cube_pt_below_vis_config = {
        'marker': 'o',
        'fillstyle': 'none',
        'markeredgewidth': 5,
        'color': 'black',
        'markersize': 25,
    }
    for i, pt in enumerate(points_to_paint):
        if pt['above_equatorial']:
            vis_config = cube_pt_above_vis_config
        else:
            vis_config = cube_pt_below_vis_config
        plot_a_point(
            point=get_coordinate_by_combination(
                pt_coeffs=pt['combination'],
                ref_points=cube_1.important_points,
            ),
            ax=ax_1,
            **vis_config,
        )

    # paint on stereogram
    stereo_pt_above_vis_config = {
        'marker': 'X',
        'color': 'black',
        'markersize': 25,
    }
    stereo_pt_below_vis_config = {
        'marker': 'o',
        'fillstyle': 'none',
        'markeredgewidth': 5,
        'color': 'black',
        'markersize': 30,
    }
    for i, pt in enumerate(points_to_paint):
        if pt['above_equatorial']:
            vis_config = stereo_pt_above_vis_config
        else:
            vis_config = stereo_pt_below_vis_config
        plot_a_point(
            point=get_coordinate_by_combination(
                pt_coeffs=pt['combination'],
                ref_points=stereogram_1.important_points,
            ),
            ax=ax_2,
            **vis_config,
        )

    # plot symmetry element
    symmetry_color = 'tab:green'

    # plot rotation
    # Define the ellipse marker.
    circle = mpath.Path.unit_circle()
    verts = np.copy(circle.vertices)
    verts[:, 1] *= 1.618
    # ellipt_marker = mpath.Path(verts, circle.codes)
    ellipt_marker = mpath.Path(verts)
    symmetry_vis_config_1 = {
        'color': symmetry_color,
        'marker': ellipt_marker,
        'markersize': 45,
    }
    ellipt_marker_2 = ellipt_marker.transformed(
        mpl.transforms.Affine2D().rotate_deg(90)
    )
    symmetry_vis_config_2 = {
        **symmetry_vis_config_1,
        'marker': ellipt_marker_2,
    }
    plot_a_point(
        point=get_polar_coordinate(
            radius=stereogram_1.radius,
            angle=np.pi/2,
        ),
        ax=ax_2,
        **symmetry_vis_config_2,
    )
    plot_a_point(
        point=get_polar_coordinate(
            radius=stereogram_1.radius,
            angle=np.pi/2+np.pi,
        ),
        ax=ax_2,
        **symmetry_vis_config_2,
    )

    symmetry_vis_config_3 = {
        'color': symmetry_color,
        'marker': '^',
        'markersize': 50,
    }
    plot_a_point(
        point=stereogram_1.important_points['4'],
        ax=ax_2,
        **symmetry_vis_config_3,
    )

    symmetry_color_2 = 'tab:orange'
    symmetry_vis_config_4 = {
        'color': symmetry_color_2,
        'marker': '^',
        'markersize': 50,
    }
    plot_a_point(
        point=stereogram_1.important_points['5'],
        ax=ax_2,
        **symmetry_vis_config_4,
    )
    plot_a_point(
        point=stereogram_1.important_points['6'],
        ax=ax_2,
        **symmetry_vis_config_4,
    )
    plot_a_point(
        point=stereogram_1.important_points['7'],
        ax=ax_2,
        **symmetry_vis_config_4,
    )

    symmetry_vis_config_5 = {
        'color': symmetry_color_2,
        'marker': ellipt_marker,
        'markersize': 45,
    }
    plot_a_point(
        point=stereogram_1.important_points['2347'],
        ax=ax_2,
        **symmetry_vis_config_5,
    )
    plot_a_point(
        point=stereogram_1.important_points['0156'],
        ax=ax_2,
        **symmetry_vis_config_5,
    )
    plot_a_point(
        point=stereogram_1.important_points['4567'],
        ax=ax_2,
        **symmetry_vis_config_5,
    )

    if save_fig:
        plt.savefig('../plots/quiz/q_2a_2.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2


def calc_2b():
    a_1 = np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, -1],
    ])
    a_2 = np.array([
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, -1],
    ])
    a_3 = np.array([
        [0, -1, 0],
        [0, 0, 1],
        [-1, 0, 0],
    ])

    print('a_1')
    tensor_transformation(a_1)

    print('a_2')
    tensor_transformation(a_2)

    print('a_3')
    tensor_transformation(a_3)


if __name__ == '__main__':

    cube_1 = SimpleCube(scale=1)
    stereogram_1 = Stereogram(radius=1)

    fig, ax = plot_2a(
        save_fig=True,
        show_fig=True,
    )

    fig, ax_1, ax_2 = plot_2a_solution(
        save_fig=True,
        show_fig=True,
    )

    calc_2b()