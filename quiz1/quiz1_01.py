import numpy as np
from matplotlib import pyplot as plt
from pprint import pprint

from utils.lattice_utils import get_lattice_2D
from utils.plot_utils import fig_from_fig_or_none
from utils.plot_utils import plot_a_point
from utils.plot_utils import plot_a_line
from utils.plot_utils import plot_a_cell
import sympy
from sympy.vector import CoordSys3D


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def plot_graphene_framework(save_fig=False, show_fig=False):
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
    range_a = (-10, 10)
    range_b = (-10, 10)

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

    fig = plt.figure(
        figsize=(12, 12),
    )
    ax = fig.add_subplot(111)

    # plot edges
    edge_vis_config = {
        'color': 'tab:gray',
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
    ax.plot(
        site_2_points[:, 0],
        site_2_points[:, 1],
        linestyle='none',
        marker='o',
        markersize=15,
        color=atom_color,
    )

    ax.set_xlim(left=-5, right=5)
    ax.set_ylim(bottom=-4, top=6)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    plt.tight_layout()

    if save_fig:
        plt.savefig('../plots/quiz/q_framework.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def plot_1a(save_fig=False, show_fig=False):
    # init
    # cell params
    site_1 = np.array((1.0/3.0, 2.0/3.0))
    site_2 = np.array((2.0/3.0, 1.0/3.0))

    # math transformation
    vec_cell = np.stack([vec_a, vec_b])
    site_1 = site_1 @ vec_cell
    site_2 = site_2 @ vec_cell


    fig, ax = plot_graphene_framework(
        save_fig=False,
        show_fig=False,
    )
    fig, ax = fig_from_fig_or_none(fig=fig, ax=ax)

    # # add primitive cell 1
    # cell_vis_config = {
    #     'color': 'tab:red',
    # }
    # plot_a_cell(
    #     starting_point=np.array((0.0, 0.0)),
    #     vec_a=vec_a,
    #     vec_b=vec_b,
    #     ax=ax,
    #     **cell_vis_config,
    # )

    # add primitive cell 2
    cell_vis_config = {
        'color': 'tab:purple',
        'linewidth': 5,
    }
    starting_point=site_1-vec_a*5-vec_b*3
    plot_a_cell(
        starting_point=starting_point,
        vec_a=vec_a+vec_b,
        vec_b=vec_b,
        ax=ax,
        **cell_vis_config,
    )
    ax.text(
        starting_point[0]+0.1,
        starting_point[1]+0.2,
        '(II)',
        fontsize=28,
        fontweight='bold',
        color=cell_vis_config['color'],
    )

    # add cell 3
    cell_vis_config = {
        'color': 'tab:orange',
        'linewidth': 5,
    }
    starting_point=site_1-vec_a*5-vec_b*6
    plot_a_cell(
        starting_point=starting_point,
        vec_a=(vec_a-vec_b)/3,
        vec_b=vec_b,
        ax=ax,
        **cell_vis_config,
    )
    ax.text(
        starting_point[0]+0.1,
        starting_point[1]+0.2,
        '(I)',
        fontsize=28,
        fontweight='bold',
        color=cell_vis_config['color'],
        )

    # add cell 4
    cell_vis_config = {
        'color': 'tab:green',
        'linewidth': 5,
    }
    starting_point=site_1-vec_a*5+vec_b
    plot_a_cell(
        starting_point=starting_point,
        vec_a=(vec_a-vec_b),
        vec_b=(vec_a+2*vec_b)/3,
        ax=ax,
        **cell_vis_config,
    )
    ax.text(
        starting_point[0]-0.8,
        starting_point[1]+0.2,
        '(III)',
        fontsize=28,
        fontweight='bold',
        color=cell_vis_config['color'],
        )

    # add cell 5
    cell_vis_config = {
        'color': 'tab:cyan',
        'linewidth': 5,
    }
    starting_point = site_2-vec_b*4
    plot_a_cell(
        starting_point=starting_point,
        vec_a=(vec_a*2/3+vec_b/3),
        vec_b=(vec_b-vec_a)/3,
        ax=ax,
        **cell_vis_config,
    )
    ax.text(
        starting_point[0]-0.3,
        starting_point[1]+0.5,
        '(IV)',
        fontsize=28,
        fontweight='bold',
        color=cell_vis_config['color'],
        )

    # add cell 6
    cell_vis_config = {
        'color': 'tab:olive',
        'linewidth': 5,
    }
    starting_point = site_1-vec_b*1
    plot_a_cell(
        starting_point=starting_point,
        vec_a=(vec_a-vec_b),
        vec_b=(vec_a+vec_b*2),
        ax=ax,
        **cell_vis_config,
    )
    ax.text(
        starting_point[0]+0.1,
        starting_point[1]+0.2,
        '(V)',
        fontsize=28,
        fontweight='bold',
        color=cell_vis_config['color'],
        )

    # # add lattice vectors
    # vec_color = cell_vis_config['color']
    # ax.arrow(
    #     starting_point[0],
    #     starting_point[1],
    #     (vec_a-vec_b)[0],
    #     (vec_a-vec_b)[1],
    #     head_width=0.3,
    #     head_length=0.5,
    #     linewidth=5,
    #     facecolor=vec_color,
    #     edgecolor=vec_color,
    #     head_starts_at_zero=False,
    #     length_includes_head=True,
    # )
    # ax.text(
    #     (starting_point+vec_a-vec_b)[0]-0.4,
    #     (starting_point+vec_a-vec_b)[1]+0.1,
    #     'a',
    #     fontsize=36,
    #     fontweight='bold',
    #     color=vec_color,
    #     )
    #
    # ax.arrow(
    #     starting_point[0],
    #     starting_point[1],
    #     (vec_a+vec_b*2)[0],
    #     (vec_a+vec_b*2)[1],
    #     head_width=0.3,
    #     head_length=0.5,
    #     linewidth=5,
    #     facecolor=vec_color,
    #     edgecolor=vec_color,
    #     head_starts_at_zero=False,
    #     length_includes_head=True,
    # )
    # ax.text(
    #     (starting_point+vec_a+vec_b*2)[0]+0.1,
    #     (starting_point+vec_a+vec_b*2)[1]+0.1,
    #     'b',
    #     fontsize=36,
    #     fontweight='bold',
    #     color=vec_color,
    #     )

    # add cell 7
    cell_vis_config = {
        'color': 'tab:brown',
        'linewidth': 5,
    }
    starting_point = site_2-vec_a*2+vec_b*2
    plot_a_cell(
        starting_point=starting_point,
        vec_a=(vec_a*2+vec_b),
        vec_b=(vec_a*3+vec_b*2),
        ax=ax,
        **cell_vis_config,
    )
    ax.text(
        starting_point[0]+0.2,
        starting_point[1]-0.5,
        '(VI)',
        fontsize=28,
        fontweight='bold',
        color=cell_vis_config['color'],
        )

    if save_fig:
        plt.savefig('../plots/quiz/q_1a.png', dpi=300)
    if show_fig:
        plt.show()

    return fig, ax


def calc_1b():
    # bond_length_2 = 1.42
    # bond_length_2 = 1
    # vec_a_2 = (vec_a - vec_b)*bond_length_2
    # vec_b_2 = (vec_a + vec_b * 2)*bond_length_2
    # print('vec_a_2', vec_a_2)
    # print('vec_b_2', vec_b_2)
    N = CoordSys3D('N')
    # v_a = -sympy.Rational(3/2)*N.i -sympy.sqrt(3)/2*N.j + 0*N.k
    # v_b = sympy.Rational(3/2)*N.i -sympy.sqrt(3)/2*N.j + 0*N.k
    v_a = -sympy.Rational(3/2)*sympy.sqrt(3)*N.i -sympy.Rational(3/2)*N.j + 0*N.k
    v_b = sympy.Rational(3/2)*sympy.sqrt(3)*N.i -sympy.Rational(3/2)*N.j + 0*N.k
    v_c = 1*N.k
    h = sympy.Symbol('h')
    k = sympy.Symbol('k')
    print('a.dot(b)', v_a.dot(v_b))
    print('b.cross(c)', v_b.cross(v_c))
    print('c.cross(a)', v_c.cross(v_a))
    v_n = h*v_b.cross(v_c)+k*v_c.cross(v_a)
    print('v_n', v_n)
    volume = (v_a.cross(v_b)).dot(v_c)
    print('volume', volume)
    print('v_n.dot(v_n)', v_n.dot(v_n))
    d = volume/sympy.sqrt(v_n.dot(v_n))
    print('d', d.simplify())

    for h in range(-5,6):
        for k in range(-5,6):
            result = h**2+k**2+h*k
            if result > 10:
                continue
            print('{}, {}'.format(h, k), result)

if __name__ == '__main__':

    bond_length = 1
    vec_a = np.array((-0.5, -np.sqrt(3)/2))*bond_length
    vec_b = np.array((1.0, 0.0))*bond_length

    # fig, ax = plot_graphene_framework(
    #     save_fig=True,
    #     show_fig=True,
    # )

    fig, ax = plot_1a(
        save_fig=True,
        show_fig=True,
    )

    calc_1b()
