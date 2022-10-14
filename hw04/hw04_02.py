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


def plot_2a(save_fig=False, show_fig=False):
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )

    # plotting params
    points_to_paint = [
        {
            'combination': {
                '4': 8.0 / 12.0,
                '47': 2.0 / 12.0,
                '4567': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '3': 8.0 / 12.0,
                '23': 2.0 / 12.0,
                '0123': 2.0 / 12.0,
            },
            'above_equatorial': False,
        },

        {
            'combination': {
                '7': 8.0 / 12.0,
                '47': 2.0 / 12.0,
                '4567': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '2': 8.0 / 12.0,
                '23': 2.0 / 12.0,
                '0123': 2.0 / 12.0,
            },
            'above_equatorial': False,
        },

        {
            'combination': {
                '6': 8.0 / 12.0,
                '56': 2.0 / 12.0,
                '4567': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '1': 8.0 / 12.0,
                '01': 2.0 / 12.0,
                '0123': 2.0 / 12.0,
            },
            'above_equatorial': False,
        },

        {
            'combination': {
                '5': 8.0 / 12.0,
                '56': 2.0 / 12.0,
                '4567': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '0': 8.0 / 12.0,
                '01': 2.0 / 12.0,
                '0123': 2.0 / 12.0,
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

    # plot mirror
    symmetry_vis_config_3 = {
        'color': symmetry_color,
        'linewidth': 10,
    }
    plot_a_line(
        point_1=stereogram_1.important_points['0156'],
        point_2=stereogram_1.important_points['2347'],
        ax=ax_2,
        **symmetry_vis_config_3,
    )
    plot_a_line(
        point_1=stereogram_1.important_points['1267'],
        point_2=stereogram_1.important_points['0345'],
        ax=ax_2,
        **symmetry_vis_config_3,
    )
    circle_1 = plt.Circle(
        (0.0, 0.0),
        radius=stereogram_1.radius,
        fill=False,
        **symmetry_vis_config_3,
    )
    ax_2.add_patch(circle_1)

    # plot rotation
    # Define the ellipse marker.
    circle = mpath.Path.unit_circle()
    verts = np.copy(circle.vertices)
    verts[:, 1] *= 1.618
    # ellipt_marker = mpath.Path(verts, circle.codes)
    ellipt_marker = mpath.Path(verts)
    symmetry_vis_config_2 = {
        'color': symmetry_color,
        'marker': ellipt_marker,
        'markersize': 45,
    }
    for i in range(2):
        tmp_angle = np.pi*i/2
        tmp_marker = ellipt_marker.transformed(
            mpl.transforms.Affine2D().rotate_deg(tmp_angle/np.pi*180)
        )
        tmp_vis_config = {
            **symmetry_vis_config_2,
            'marker': tmp_marker,
        }
        plot_a_point(
            point=get_polar_coordinate(
                radius=stereogram_1.radius,
                angle=tmp_angle,
            ),
            ax=ax_2,
            **tmp_vis_config,
        )
        plot_a_point(
            point=get_polar_coordinate(
                radius=stereogram_1.radius,
                angle=tmp_angle+np.pi,
            ),
            ax=ax_2,
            **tmp_vis_config,
        )
    plot_a_point(
        point=stereogram_1.important_points['4567'],
        ax=ax_2,
        **symmetry_vis_config_2,
    )

    if save_fig:
        plt.savefig('../plots/hw04/q_2a.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2


def plot_2b(save_fig=False, show_fig=False):
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )

    # plotting params
    points_to_paint = [
        {
            'combination': {
                '4': 6.0 / 12.0,
                '34': 3.0 / 12.0,
                '0345': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '4': 6.0 / 12.0,
                '45': 3.0 / 12.0,
                '0345': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '4': 6.0 / 12.0,
                '45': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '4': 6.0 / 12.0,
                '47': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '4': 6.0 / 12.0,
                '47': 3.0 / 12.0,
                '2347': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '4': 6.0 / 12.0,
                '34': 3.0 / 12.0,
                '2347': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },

        {
            'combination': {
                '0': 6.0 / 12.0,
                '03': 3.0 / 12.0,
                '0345': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '0': 6.0 / 12.0,
                '05': 3.0 / 12.0,
                '0345': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '0': 6.0 / 12.0,
                '05': 3.0 / 12.0,
                '0156': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '0': 6.0 / 12.0,
                '01': 3.0 / 12.0,
                '0156': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '0': 6.0 / 12.0,
                '01': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '0': 6.0 / 12.0,
                '03': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },

        {
            'combination': {
                '6': 6.0 / 12.0,
                '56': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '6': 6.0 / 12.0,
                '56': 3.0 / 12.0,
                '0156': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '6': 6.0 / 12.0,
                '16': 3.0 / 12.0,
                '0156': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '6': 6.0 / 12.0,
                '16': 3.0 / 12.0,
                '1267': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '6': 6.0 / 12.0,
                '67': 3.0 / 12.0,
                '1267': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '6': 6.0 / 12.0,
                '67': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },

        {
            'combination': {
                '2': 6.0 / 12.0,
                '23': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '2': 6.0 / 12.0,
                '12': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '2': 6.0 / 12.0,
                '12': 3.0 / 12.0,
                '1267': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '2': 6.0 / 12.0,
                '27': 3.0 / 12.0,
                '1267': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '2': 6.0 / 12.0,
                '27': 3.0 / 12.0,
                '2347': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '2': 6.0 / 12.0,
                '23': 3.0 / 12.0,
                '2347': 3.0 / 12.0,
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

    # plot mirror
    symmetry_vis_config_1 = {
        'color': symmetry_color,
        'linewidth': 10,
    }
    plot_a_line(
        point_1=stereogram_1.important_points['05'],
        point_2=stereogram_1.important_points['27'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )
    plot_a_line(
        point_1=stereogram_1.important_points['16'],
        point_2=stereogram_1.important_points['34'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )
    arc_1 = plt_Arc(
        (stereogram_1.pos_arc, 0.0),
        width=2*stereogram_1.radius_arc,
        height=2*stereogram_1.radius_arc,
        angle=180-stereogram_1.angle_arc/2,
        theta1=0,
        theta2=stereogram_1.angle_arc,
        **symmetry_vis_config_1,
    )
    ax_2.add_patch(arc_1)

    arc_2 = plt_Arc(
        (-stereogram_1.pos_arc, 0.0),
        width=2*stereogram_1.radius_arc,
        height=2*stereogram_1.radius_arc,
        angle=-stereogram_1.angle_arc/2,
        theta1=0,
        theta2=stereogram_1.angle_arc,
        **symmetry_vis_config_1,
    )
    ax_2.add_patch(arc_2)

    arc_3 = plt_Arc(
        (0.0, stereogram_1.pos_arc),
        width=2*stereogram_1.radius_arc,
        height=2*stereogram_1.radius_arc,
        angle=-90-stereogram_1.angle_arc/2,
        theta1=0,
        theta2=stereogram_1.angle_arc,
        **symmetry_vis_config_1,
    )
    ax_2.add_patch(arc_3)

    arc_4 = plt_Arc(
        (0.0, -stereogram_1.pos_arc),
        width=2*stereogram_1.radius_arc,
        height=2*stereogram_1.radius_arc,
        angle=90-stereogram_1.angle_arc/2,
        theta1=0,
        theta2=stereogram_1.angle_arc,
        **symmetry_vis_config_1,
    )
    ax_2.add_patch(arc_4)

    # plot rotation
    symmetry_vis_config_2 = {
        'color': symmetry_color,
        'marker': '^',
        'markersize': 50,
    }
    plot_a_point(
        point=stereogram_1.important_points['4'],
        ax=ax_2,
        **symmetry_vis_config_2,
    )
    plot_a_point(
        point=stereogram_1.important_points['5'],
        ax=ax_2,
        **symmetry_vis_config_2,
    )
    plot_a_point(
        point=stereogram_1.important_points['6'],
        ax=ax_2,
        **symmetry_vis_config_2,
    )
    plot_a_point(
        point=stereogram_1.important_points['7'],
        ax=ax_2,
        **symmetry_vis_config_2,
    )

    # plot rotoinversion
    symmetry_vis_config_3 = {
        'markeredgecolor': symmetry_color,
        'marker': 's',
        'fillstyle': 'full',
        'color': 'white',
        'markerfacecoloralt': 'white',
        'markeredgewidth': 5,
        'markersize': 50,
    }
    # plot rotation axes
    # Define the ellipse marker.
    circle = mpath.Path.unit_circle()
    verts = np.copy(circle.vertices)
    verts[:, 1] *= 1.618
    # ellipt_marker = mpath.Path(verts, circle.codes)
    ellipt_marker = mpath.Path(verts)
    ellipt_marker = ellipt_marker.transformed(
        mpl.transforms.Affine2D().rotate_deg(-45)
    )
    symmetry_vis_config_4 = {
        'color': symmetry_color,
        'marker': ellipt_marker,
        'markersize': 45,
    }
    plot_a_point(
        point=stereogram_1.important_points['4567'],
        ax=ax_2,
        **symmetry_vis_config_3,
    )
    plot_a_point(
        point=stereogram_1.important_points['4567'],
        ax=ax_2,
        **symmetry_vis_config_4,
    )
    plot_a_point(
        point=stereogram_1.important_points['0156'],
        ax=ax_2,
        **symmetry_vis_config_3,
    )
    plot_a_point(
        point=stereogram_1.important_points['0156'],
        ax=ax_2,
        **symmetry_vis_config_4,
    )
    plot_a_point(
        point=stereogram_1.important_points['2347'],
        ax=ax_2,
        **symmetry_vis_config_3,
    )
    plot_a_point(
        point=stereogram_1.important_points['2347'],
        ax=ax_2,
        **symmetry_vis_config_4,
    )
    plot_a_point(
        point=stereogram_1.important_points['0345'],
        ax=ax_2,
        **symmetry_vis_config_3,
    )
    plot_a_point(
        point=stereogram_1.important_points['0345'],
        ax=ax_2,
        **symmetry_vis_config_4,
    )
    plot_a_point(
        point=stereogram_1.important_points['1267'],
        ax=ax_2,
        **symmetry_vis_config_3,
    )
    plot_a_point(
        point=stereogram_1.important_points['1267'],
        ax=ax_2,
        **symmetry_vis_config_4,
    )

    if save_fig:
        plt.savefig('../plots/hw04/q_2b.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2



def plot_2c(save_fig=False, show_fig=False):
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )

    # plotting params
    points_to_paint = [
        {
            'combination': {
                '4': 6.0 / 12.0,
                '45': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '4': 6.0 / 12.0,
                '47': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '5': 6.0 / 12.0,
                '56': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '5': 6.0 / 12.0,
                '45': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '6': 6.0 / 12.0,
                '56': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '6': 6.0 / 12.0,
                '67': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '7': 6.0 / 12.0,
                '47': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '7': 6.0 / 12.0,
                '67': 3.0 / 12.0,
                '4567': 3.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '3': 6.0 / 12.0,
                '03': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '3': 6.0 / 12.0,
                '23': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '0': 6.0 / 12.0,
                '01': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '0': 6.0 / 12.0,
                '03': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '1': 6.0 / 12.0,
                '01': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '1': 6.0 / 12.0,
                '12': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '2': 6.0 / 12.0,
                '23': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '2': 6.0 / 12.0,
                '12': 3.0 / 12.0,
                '0123': 3.0 / 12.0,
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

    # plot mirror
    symmetry_vis_config_1 = {
        'color': symmetry_color,
        'linewidth': 10,
    }
    plot_a_line(
        point_1=stereogram_1.important_points['0156'],
        point_2=stereogram_1.important_points['2347'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )
    plot_a_line(
        point_1=stereogram_1.important_points['1267'],
        point_2=stereogram_1.important_points['0345'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )
    plot_a_line(
        point_1=stereogram_1.important_points['05'],
        point_2=stereogram_1.important_points['27'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )
    plot_a_line(
        point_1=stereogram_1.important_points['16'],
        point_2=stereogram_1.important_points['34'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )
    circle_1 = plt.Circle(
        (0.0, 0.0),
        radius=stereogram_1.radius,
        fill=False,
        **symmetry_vis_config_1,
    )
    ax_2.add_patch(circle_1)

    # plot rotation
    # Define the ellipse marker.
    circle = mpath.Path.unit_circle()
    verts = np.copy(circle.vertices)
    verts[:, 1] *= 1.618
    # ellipt_marker = mpath.Path(verts, circle.codes)
    ellipt_marker = mpath.Path(verts)
    symmetry_vis_config_2 = {
        'color': symmetry_color,
        'marker': ellipt_marker,
        'markersize': 45,
    }
    for i in range(4):
        tmp_angle = np.pi*i/4
        tmp_marker = ellipt_marker.transformed(
            mpl.transforms.Affine2D().rotate_deg(tmp_angle/np.pi*180)
        )
        tmp_vis_config = {
            **symmetry_vis_config_2,
            'marker': tmp_marker,
        }
        plot_a_point(
            point=get_polar_coordinate(
                radius=stereogram_1.radius,
                angle=tmp_angle,
            ),
            ax=ax_2,
            **tmp_vis_config,
        )
        plot_a_point(
            point=get_polar_coordinate(
                radius=stereogram_1.radius,
                angle=tmp_angle+np.pi,
            ),
            ax=ax_2,
            **tmp_vis_config,
        )

    symmetry_vis_config_3 = {
        'color': symmetry_color,
        'marker': 's',
        'markersize': 50,
    }
    plot_a_point(
        point=stereogram_1.important_points['4567'],
        ax=ax_2,
        **symmetry_vis_config_3,
    )

    if save_fig:
        plt.savefig('../plots/hw04/q_2c.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2


def plot_2d(save_fig=False, show_fig=False):
    fig, ax = draw_stereogram_framework(
        stereogram=stereogram_1,
        show_fig=False,
        fold_3_template=True,
    )

    # plotting params
    radius_factor = 5/6
    angle_offset = np.pi*3/48
    points_to_paint = [
        {
            'polar': {
                'radius': stereogram_1.radius*radius_factor,
                'angle': np.pi/6-angle_offset,
            },
            'above_equatorial': True,
        },
        {
            'polar': {
                'radius': stereogram_1.radius*radius_factor,
                'angle': np.pi/6+angle_offset,
            },
            'above_equatorial': True,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi / 2 - angle_offset,
            },
            'above_equatorial': True,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi / 2 + angle_offset,
            },
            'above_equatorial': True,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi*5 / 6 - angle_offset,
            },
            'above_equatorial': True,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 5 / 6 + angle_offset,
            },
            'above_equatorial': True,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 7 / 6 - angle_offset,
            },
            'above_equatorial': True,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 7 / 6 + angle_offset,
            },
            'above_equatorial': True,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 6 / 4 - angle_offset,
            },
            'above_equatorial': True,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 6 / 4 + angle_offset,
            },
            'above_equatorial': True,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 11 / 6 - angle_offset,
            },
            'above_equatorial': True,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 11 / 6 + angle_offset,
            },
            'above_equatorial': True,
        },

        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi / 6 - angle_offset,
            },
            'above_equatorial': False,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi / 6 + angle_offset,
            },
            'above_equatorial': False,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi / 2 - angle_offset,
            },
            'above_equatorial': False,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi / 2 + angle_offset,
            },
            'above_equatorial': False,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 5 / 6 - angle_offset,
            },
            'above_equatorial': False,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 5 / 6 + angle_offset,
            },
            'above_equatorial': False,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 7 / 6 - angle_offset,
            },
            'above_equatorial': False,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 7 / 6 + angle_offset,
            },
            'above_equatorial': False,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 6 / 4 - angle_offset,
            },
            'above_equatorial': False,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 6 / 4 + angle_offset,
            },
            'above_equatorial': False,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 11 / 6 - angle_offset,
            },
            'above_equatorial': False,
        },
        {
            'polar': {
                'radius': stereogram_1.radius * radius_factor,
                'angle': np.pi * 11 / 6 + angle_offset,
            },
            'above_equatorial': False,
        },
    ]

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
            point=get_polar_coordinate(
                radius=pt['polar']['radius'],
                angle=pt['polar']['angle'],
            ),
            ax=ax,
            **vis_config,
        )

    # plot symmetry element
    symmetry_color = 'tab:green'

    # plot mirror
    symmetry_vis_config_1 = {
        'color': symmetry_color,
        'linewidth': 10,
    }
    for i in range(6):
        tmp_angle = np.pi*i/6
        plot_a_line(
            point_1=get_polar_coordinate(
                radius=stereogram_1.radius,
                angle=tmp_angle,
            ),
            point_2=get_polar_coordinate(
                radius=stereogram_1.radius,
                angle=tmp_angle+np.pi,
            ),
            ax=ax,
            **symmetry_vis_config_1,
        )
    circle_1 = plt.Circle(
        (0.0, 0.0),
        radius=stereogram_1.radius,
        fill=False,
        **symmetry_vis_config_1,
    )
    ax.add_patch(circle_1)

    # plot rotation
    # Define the ellipse marker.
    circle = mpath.Path.unit_circle()
    verts = np.copy(circle.vertices)
    verts[:, 1] *= 1.618
    # ellipt_marker = mpath.Path(verts, circle.codes)
    ellipt_marker = mpath.Path(verts)
    symmetry_vis_config_2 = {
        'color': symmetry_color,
        'marker': ellipt_marker,
        'markersize': 45,
    }
    for i in range(6):
        tmp_angle = np.pi*i/6
        tmp_marker = ellipt_marker.transformed(
            mpl.transforms.Affine2D().rotate_deg(tmp_angle/np.pi*180)
        )
        tmp_vis_config = {
            **symmetry_vis_config_2,
            'marker': tmp_marker,
        }
        plot_a_point(
            point=get_polar_coordinate(
                radius=stereogram_1.radius,
                angle=tmp_angle,
            ),
            ax=ax,
            **tmp_vis_config,
        )
        plot_a_point(
            point=get_polar_coordinate(
                radius=stereogram_1.radius,
                angle=tmp_angle+np.pi,
            ),
            ax=ax,
            **tmp_vis_config,
        )

    symmetry_vis_config_3 = {
        'color': symmetry_color,
        'marker': 'h',
        'markersize': 100,
    }
    plot_a_point(
        point=stereogram_1.important_points['4567'],
        ax=ax,
        **symmetry_vis_config_3,
    )

    if save_fig:
        plt.savefig('../plots/hw04/q_2d.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


if __name__ == '__main__':

    cube_1 = SimpleCube(scale=1)
    stereogram_1 = Stereogram(radius=1)

    fig, ax_1, ax_2 = plot_2a(
        save_fig=True,
        show_fig=True,
    )

    fig, ax_1, ax_2 = plot_2b(
        save_fig=True,
        show_fig=True,
    )

    fig, ax_1, ax_2 = plot_2c(
        save_fig=True,
        show_fig=True,
    )

    fig, ax = plot_2d(
        save_fig=True,
        show_fig=True,
    )