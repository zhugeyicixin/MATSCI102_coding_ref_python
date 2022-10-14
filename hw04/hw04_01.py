import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.path as mpath

from utils.stereogram_utils import SimpleCube, Stereogram
from utils.plot_utils import draw_cube_stereogram_framework
from utils.plot_utils import plot_a_point, plot_a_line
from utils.lattice_utils import get_coordinate_by_combination


def plot_1a(save_fig=False, show_fig=False):
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )

    # plotting params
    points_to_paint = [
        {
            'combination': {
                '3': 2.0 / 3.0,
                '34': 3.0 / 12.0,
                '0345': 1.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '4': 2.0 / 3.0,
                '47': 3.0 / 12.0,
                '4567': 1.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '2': 2.0 / 3.0,
                '23': 3.0 / 12.0,
                '0123': 1.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '7': 2.0 / 3.0,
                '27': 3.0 / 12.0,
                '1267': 1.0 / 12.0,
            },
            'above_equatorial': True,
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
        'markersize': 25,
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

    # plot rotaional axis
    symmetry_vis_config_1 = {
        'color': symmetry_color,
        'marker': 's',
        'markersize': 50,
    }
    plot_a_point(
        point=stereogram_1.important_points['0156'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )
    plot_a_point(
        point=stereogram_1.important_points['2347'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )

    if save_fig:
        plt.savefig('../plots/hw04/q_1a.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2


def plot_1b(save_fig=False, show_fig=False):
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )

    # plotting params
    points_to_paint = [
        {
            'combination': {
                '4': 2.0 / 3.0,
                '34': 3.0 / 12.0,
                '2347': 1.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '2': 2.0 / 3.0,
                '27': 3.0 / 12.0,
                '2347': 1.0 / 12.0,
            },
            'above_equatorial': False,
        },
        {
            'combination': {
                '6': 2.0 / 3.0,
                '56': 3.0 / 12.0,
                '0156': 1.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '0': 2.0 / 3.0,
                '01': 3.0 / 12.0,
                '0156': 1.0 / 12.0,
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
        'markersize': 25,
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

    # plot rotoinversion
    symmetry_vis_config_1 = {
        'color': symmetry_color,
        'marker': 's',
        'fillstyle': 'none',
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
    symmetry_vis_config_2 = {
        'color': symmetry_color,
        'marker': ellipt_marker,
        'markersize': 45,
    }
    plot_a_point(
        point=stereogram_1.important_points['0156'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )
    plot_a_point(
        point=stereogram_1.important_points['0156'],
        ax=ax_2,
        **symmetry_vis_config_2,
    )
    plot_a_point(
        point=stereogram_1.important_points['2347'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )
    plot_a_point(
        point=stereogram_1.important_points['2347'],
        ax=ax_2,
        **symmetry_vis_config_2,
    )

    if save_fig:
        plt.savefig('../plots/hw04/q_1b.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2


def plot_1c(save_fig=False, show_fig=False):
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
                '34': 5.0 / 12.0,
                '2347': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '0': 5.0 / 12.0,
                '05': 5.0 / 12.0,
                '0345': 2.0 / 12.0,
            },
            'above_equatorial': False,
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
                '7': 5.0 / 12.0,
                '27': 5.0 / 12.0,
                '1267': 2.0 / 12.0,
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
        'markersize': 25,
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

    # # plot mirror
    # symmetry_vis_config_3 = {
    #     'color': symmetry_color,
    #     'linewidth': 10,
    # }
    # plot_a_line(
    #     point_1=stereogram_1.important_points['0156'],
    #     point_2=stereogram_1.important_points['2347'],
    #     ax=ax_2,
    #     **symmetry_vis_config_3,
    # )

    # plot rotoinversion
    symmetry_vis_config_1 = {
        'color': symmetry_color,
        'marker': 's',
        'fillstyle': 'none',
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
    symmetry_vis_config_2 = {
        'color': symmetry_color,
        'marker': ellipt_marker,
        'markersize': 45,
    }
    plot_a_point(
        point=stereogram_1.important_points['4567'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )
    plot_a_point(
        point=stereogram_1.important_points['4567'],
        ax=ax_2,
        **symmetry_vis_config_2,
    )

    if save_fig:
        plt.savefig('../plots/hw04/q_1c.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2


def plot_1d(save_fig=False, show_fig=False):
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
                '6': 8.0 / 12.0,
                '67': 2.0 / 12.0,
                '1267': 2.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '2': 8.0 / 12.0,
                '27': 2.0 / 12.0,
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
        'markersize': 25,
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

    # # plot mirror
    # symmetry_vis_config_3 = {
    #     'color': symmetry_color,
    #     'linewidth': 10,
    # }
    # plot_a_line(
    #     point_1=stereogram_1.important_points['0156'],
    #     point_2=stereogram_1.important_points['2347'],
    #     ax=ax_2,
    #     **symmetry_vis_config_3,
    # )

    # plot rotation
    symmetry_vis_config_1 = {
        'color': symmetry_color,
        'marker': '^',
        'markersize': 50,
    }
    plot_a_point(
        point=stereogram_1.important_points['7'],
        ax=ax_2,
        **symmetry_vis_config_1,
    )

    if save_fig:
        plt.savefig('../plots/hw04/q_1d.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2


if __name__ == '__main__':

    cube_1 = SimpleCube(scale=1)
    stereogram_1 = Stereogram(radius=1)

    fig, ax_1, ax_2 = plot_1a(
        save_fig=True,
        show_fig=True,
    )

    fig, ax_1, ax_2 = plot_1b(
        save_fig=True,
        show_fig=True,
    )

    fig, ax_1, ax_2 = plot_1c(
        save_fig=True,
        show_fig=True,
    )

    fig, ax_1, ax_2 = plot_1d(
        save_fig=True,
        show_fig=True,
    )