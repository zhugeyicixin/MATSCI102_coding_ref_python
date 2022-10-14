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


def plot_3a(save_fig=False, show_fig=False):
    fig, ax_1, ax_2 = draw_cube_stereogram_framework(
        cube=cube_1,
        stereogram=stereogram_1,
        show_fig=False,
    )

    # plotting params
    points_to_paint = [
        {
            'combination': {
                '4': 3.0 / 12.0,
                '45': 4.0 / 12.0,
                '0345': 5.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '5': 3.0 / 12.0,
                '45': 4.0 / 12.0,
                '0345': 5.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '5': 3.0 / 12.0,
                '56': 4.0 / 12.0,
                '0156': 5.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '6': 3.0 / 12.0,
                '56': 4.0 / 12.0,
                '0156': 5.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '6': 3.0 / 12.0,
                '67': 4.0 / 12.0,
                '1267': 5.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '7': 3.0 / 12.0,
                '67': 4.0 / 12.0,
                '1267': 5.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '7': 3.0 / 12.0,
                '47': 4.0 / 12.0,
                '2347': 5.0 / 12.0,
            },
            'above_equatorial': True,
        },
        {
            'combination': {
                '4': 3.0 / 12.0,
                '47': 4.0 / 12.0,
                '2347': 5.0 / 12.0,
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
    plot_a_line(
        point_1=stereogram_1.important_points['05'],
        point_2=stereogram_1.important_points['27'],
        ax=ax_2,
        **symmetry_vis_config_3,
    )
    plot_a_line(
        point_1=stereogram_1.important_points['16'],
        point_2=stereogram_1.important_points['34'],
        ax=ax_2,
        **symmetry_vis_config_3,
    )

    # plot rotation
    symmetry_vis_config_2 = {
        'color': symmetry_color,
        'marker': 's',
        'markersize': 50,
    }
    plot_a_point(
        point=stereogram_1.important_points['4567'],
        ax=ax_2,
        **symmetry_vis_config_2,
    )

    if save_fig:
        plt.savefig('../plots/hw04/q_3a.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax_1, ax_2


if __name__ == '__main__':

    cube_1 = SimpleCube(scale=1)
    stereogram_1 = Stereogram(radius=1)

    fig, ax_1, ax_2 = plot_3a(
        save_fig=True,
        show_fig=True,
    )

