import numpy as np
from sympy import Point, Line, Polygon
from pprint import pprint
from typing import Optional


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def get_lattice_2D(
    vec_a: np.ndarray,
    vec_b: np.ndarray,
    range_a: Optional[tuple]=None,
    range_b: Optional[tuple]=None,
    range_x: Optional[tuple]=None,
    range_y: Optional[tuple]=None,
):
    if range_a is not None:
        mesh_a = np.arange(range_a[0], range_a[1]+1)
        mesh_b = np.arange(range_b[0], range_b[1]+1)
    elif range_x is not None:
        mesh_a = np.arange(
            int(2*range_x[0]/max(abs(vec_a[0]), abs(vec_b[0]))),
            int(2*range_x[1]/max(abs(vec_a[0]), abs(vec_b[0])))+1,
        )
        mesh_b = np.arange(
            int(2*range_y[0]/max(abs(vec_a[1]), abs(vec_b[1]))),
            int(2*range_y[1]/max(abs(vec_a[1]), abs(vec_b[1])))+1,
        )
    else:
        raise NotImplementedError

    mesh_aa, mesh_bb = np.meshgrid(mesh_a, mesh_b)
    mesh_grid = np.stack([mesh_aa, mesh_bb], axis=-1)
    vec_cell = np.stack([vec_a, vec_b])
    all_points = mesh_grid@vec_cell
    all_points = np.reshape(all_points, (-1, 2))

    # screen points
    lattice_points = []
    if range_x is not None:
        for p in all_points:
            if (
                range_x[0] < p[0] < range_x[1]
                and range_y[0] < p[1] < range_y[1]
            ):
                lattice_points.append(p)
    else:
        lattice_points = all_points

    return np.array(lattice_points)


def get_bisector_line(
    point_end: np.array,
    point_start=np.array((0.,0.)),
    relative_magnitude=2,
):
    """
    for drawing a Wigner-Seitz cell

    :return:
    """

    midpoint = (point_end + point_start)/2.0
    direction_vec = point_end - point_start
    normal_vec = np.array(
        (-direction_vec[1], direction_vec[0])
    )
    endpoint_1 = midpoint + normal_vec*relative_magnitude
    endpoint_2 = midpoint - normal_vec*relative_magnitude

    return np.array([endpoint_1, endpoint_2])


def get_line_intersection(
    line_1: np.ndarray,
    line_2: np.ndarray,
):
    l1 = Line(Point(line_1[0]), Point(line_1[1]))
    l2 = Line(Point(line_2[0]), Point(line_2[1]))
    intersection = l1.intersection(l2)
    return np.array(intersection[0]).astype(np.float)


def get_polygon_area(vertices):
    polygon_1 = Polygon(*vertices)
    return float(polygon_1.area)


def get_reciprocal_vectors_2D(
    vec_a: np.ndarray,
    vec_b: np.ndarray,
    scale_factor=1.0
):
    ...
    cross_bc = np.array((vec_b[1], -vec_b[0]))
    reciprocal_a = (
        2*np.pi*scale_factor**2
        *cross_bc/np.dot(vec_a, cross_bc)
    )
    cross_ca = np.array((-vec_a[1], vec_a[0]))
    reciprocal_b = (
        2 * np.pi * scale_factor ** 2
        * cross_ca / np.dot(vec_b, cross_ca)
    )
    return reciprocal_a, reciprocal_b


def get_coordinate_by_combination(
    pt_coeffs,
    ref_points,
):
    result = None
    for pt, coeff in pt_coeffs.items():
        if result is None:
            result = ref_points[pt]*coeff
        else:
            result += ref_points[pt]*coeff
    return result

