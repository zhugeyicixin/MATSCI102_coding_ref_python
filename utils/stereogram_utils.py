import itertools
from typing import (
    List,
)
import numpy as np
from copy import deepcopy

from utils.math_utils import get_polar_coordinate
from utils.constants import NEAR_ZERO

__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


class GeometryBase(object):

    ID_Order = {
        'origin': -1,
    }

    def __init__(self):
        pass

    @classmethod
    def _get_id_order(cls, id: str):
        return cls.ID_Order.get(id, len(id))

    @classmethod
    def get_composite_id_from_vertex_ids(cls, vertex_ids: List[str]):
        composite_id = '_'.join(
            sorted(
                vertex_ids,
                key=cls._get_id_order,
            )
        )
        return composite_id

class SimpleCube(GeometryBase):

    def __init__(self, scale=1.0):
        super().__init__()
        self.scale = scale

        # Define vertices
        self.cube_vertices = np.array((
            (0, 0, 0),
            (1, 0, 0),
            (1, 1, 0),
            (0, 1, 0),
            (0, 1, 1),
            (0, 0, 1),
            (1, 0, 1),
            (1, 1, 1),
        ))*scale

        # Define faces
        self.cube_front_faces = np.array((
            self.cube_vertices[[1, 2, 7, 6,]],
            self.cube_vertices[[2, 3, 4, 7,]],
            self.cube_vertices[[4, 5, 6, 7,]],
        ))
        self.cube_back_faces = np.array((
            self.cube_vertices[[0, 5, 4, 3,]],
            self.cube_vertices[[0, 1, 6, 5,]],
            self.cube_vertices[[0, 3, 2, 1,]],
        ))
        self.cube_faces = np.concatenate(
            [self.cube_front_faces, self.cube_back_faces],
            axis=0,
        )
        # define centers
        self.cube_edge_centers = {
            '01': (self.cube_vertices[0]+self.cube_vertices[1])/2.0,
            '12': (self.cube_vertices[1]+self.cube_vertices[2])/2.0,
            '23': (self.cube_vertices[2]+self.cube_vertices[3])/2.0,
            '03': (self.cube_vertices[0]+self.cube_vertices[3])/2.0,
            '45': (self.cube_vertices[4]+self.cube_vertices[5])/2.0,
            '56': (self.cube_vertices[5]+self.cube_vertices[6])/2.0,
            '67': (self.cube_vertices[6]+self.cube_vertices[7])/2.0,
            '47': (self.cube_vertices[4]+self.cube_vertices[7])/2.0,
            '05': (self.cube_vertices[0]+self.cube_vertices[5])/2.0,
            '16': (self.cube_vertices[1]+self.cube_vertices[6])/2.0,
            '27': (self.cube_vertices[2]+self.cube_vertices[7])/2.0,
            '34': (self.cube_vertices[3]+self.cube_vertices[4])/2.0,
        }
        self.cube_face_centers = {
            '0123': (
                        self.cube_vertices[0] + self.cube_vertices[1]
                        + self.cube_vertices[2] + self.cube_vertices[3]
                    ) / 4.0,
            '2347': (
                        self.cube_vertices[2] + self.cube_vertices[3]
                        + self.cube_vertices[4] + self.cube_vertices[7]
                    ) / 4.0,
            '0345': (
                        self.cube_vertices[0] + self.cube_vertices[3]
                        + self.cube_vertices[4] + self.cube_vertices[5]
                    ) / 4.0,
            '0156': (
                        self.cube_vertices[0] + self.cube_vertices[1]
                        + self.cube_vertices[5] + self.cube_vertices[6]
                    ) / 4.0,
            '1267': (
                        self.cube_vertices[1] + self.cube_vertices[2]
                        + self.cube_vertices[6] + self.cube_vertices[7]
                    ) / 4.0,
            '4567': (
                        self.cube_vertices[4] + self.cube_vertices[5]
                        + self.cube_vertices[6] + self.cube_vertices[7]
                    ) / 4.0,
        }
        # define important points
        self.important_points = {
            '0': self.cube_vertices[0],
            '1': self.cube_vertices[1],
            '2': self.cube_vertices[2],
            '3': self.cube_vertices[3],
            '4': self.cube_vertices[4],
            '5': self.cube_vertices[5],
            '6': self.cube_vertices[6],
            '7': self.cube_vertices[7],
            **self.cube_edge_centers,
            **self.cube_face_centers,
        }

    def get_vertices_of_area(self, area_id: str):
        # goal
        if 'origin' in area_id:
            if len(set(area_id) & {'0', '1', '2', '3'}) > 0:
                area_id = area_id.replace('origin', '0123')
            else:
                area_id = area_id.replace('origin', '4567')

        vertex_ids = area_id.split('_')
        vertices = [
            self.important_points[id] for id in vertex_ids
        ]
        return vertices


class Stereogram(GeometryBase):

    def __init__(
        self,
        radius=1.0,
        resolution=1000,
        rounding_decimals=6,
    ):
        super().__init__()
        self.radius = radius
        self.resolution = resolution
        self.rounding_decimals = rounding_decimals

        self.radius_arc = self.radius * np.sqrt(3)
        self.pos_arc = self.radius * np.sqrt(2)
        self.radius_inner_1 = self.radius_arc - self.pos_arc
        self.radius_inner_2 = (np.sqrt(2)-1)*self.radius
        self.angle_arc = 2 * np.arctan(1 / np.sqrt(2)) / np.pi * 180

        self.origin = np.array((0.0, 0.0))
        self.all_xs, self.all_ys = self._init_grid_xy()

        # define keypoints
        self.important_points = {
            '2347': np.array((self.radius, 0.0)),
            '0345': np.array((0.0, self.radius)),
            '0156': np.array((-self.radius, 0.0)),
            '1267': np.array((0.0, -self.radius)),
            '34': get_polar_coordinate(self.radius, np.pi/4),
            '05': get_polar_coordinate(self.radius, np.pi*3/4),
            '16': get_polar_coordinate(self.radius, np.pi*5/4),
            '27': get_polar_coordinate(self.radius, np.pi*7/4),
            '47': np.array((self.radius_inner_1, 0.0)),
            '45': np.array((0.0, self.radius_inner_1)),
            '56': np.array((-self.radius_inner_1, 0.0)),
            '67': np.array((0.0, -self.radius_inner_1)),
            '23': np.array((self.radius_inner_1, 0.0)),
            '03': np.array((0.0, self.radius_inner_1)),
            '01': np.array((-self.radius_inner_1, 0.0)),
            '12': np.array((0.0, -self.radius_inner_1)),
            '4': get_polar_coordinate(self.radius_inner_2, np.pi / 4),
            '5': get_polar_coordinate(self.radius_inner_2, np.pi * 3 / 4),
            '6': get_polar_coordinate(self.radius_inner_2, np.pi * 5 / 4),
            '7': get_polar_coordinate(self.radius_inner_2, np.pi * 7 / 4),
            '3': get_polar_coordinate(self.radius_inner_2, np.pi / 4),
            '0': get_polar_coordinate(self.radius_inner_2, np.pi * 3 / 4),
            '1': get_polar_coordinate(self.radius_inner_2, np.pi * 5 / 4),
            '2': get_polar_coordinate(self.radius_inner_2, np.pi * 7 / 4),
        }

        self.important_curves = {
            'origin_47': self._get_points_between_points_on_line_0(
                self.origin,
                self.important_points['47'],
            ),
            '47_2347': self._get_points_between_points_on_line_0(
                self.important_points['47'],
                self.important_points['2347'],
            ),
            'origin_56': self._get_points_between_points_on_line_0(
                self.origin,
                self.important_points['56'],
            ),
            '56_0156': self._get_points_between_points_on_line_0(
                self.important_points['56'],
                self.important_points['0156'],
            ),
            'origin_4': self._get_points_between_points_on_line_45(
                self.origin,
                self.important_points['4'],
            ),
            '4_34': self._get_points_between_points_on_line_45(
                self.important_points['4'],
                self.important_points['34'],
            ),
            'origin_6': self._get_points_between_points_on_line_45(
                self.origin,
                self.important_points['6'],
            ),
            '6_16': self._get_points_between_points_on_line_45(
                self.important_points['6'],
                self.important_points['16'],
            ),
            'origin_45': self._get_points_between_points_on_line_90(
                self.origin,
                self.important_points['45'],
            ),
            '45_0345': self._get_points_between_points_on_line_90(
                self.important_points['45'],
                self.important_points['0345'],
            ),
            'origin_67': self._get_points_between_points_on_line_90(
                self.origin,
                self.important_points['67'],
            ),
            '67_1267': self._get_points_between_points_on_line_90(
                self.important_points['67'],
                self.important_points['1267'],
            ),
            'origin_5': self._get_points_between_points_on_line_135(
                self.origin,
                self.important_points['5'],
            ),
            '5_05': self._get_points_between_points_on_line_135(
                self.important_points['5'],
                self.important_points['05'],
            ),
            'origin_7': self._get_points_between_points_on_line_135(
                self.origin,
                self.important_points['7'],
            ),
            '7_27': self._get_points_between_points_on_line_135(
                self.important_points['7'],
                self.important_points['27'],
            ),
            '6_56': self._get_points_between_points_on_arc_cr(
                self.important_points['6'],
                self.important_points['56'],
            ),
            '6_1267': self._get_points_between_points_on_arc_cr(
                self.important_points['6'],
                self.important_points['1267'],
            ),
            '5_56': self._get_points_between_points_on_arc_cr(
                self.important_points['5'],
                self.important_points['56'],
            ),
            '5_0345': self._get_points_between_points_on_arc_cr(
                self.important_points['5'],
                self.important_points['0345'],
            ),
            '4_47': self._get_points_between_points_on_arc_cl(
                self.important_points['4'],
                self.important_points['47'],
            ),
            '4_0345': self._get_points_between_points_on_arc_cl(
                self.important_points['4'],
                self.important_points['0345'],
            ),
            '7_47': self._get_points_between_points_on_arc_cl(
                self.important_points['7'],
                self.important_points['47'],
            ),
            '7_1267': self._get_points_between_points_on_arc_cl(
                self.important_points['7'],
                self.important_points['1267'],
            ),
            '7_67': self._get_points_between_points_on_arc_ct(
                self.important_points['7'],
                self.important_points['67'],
            ),
            '7_2347': self._get_points_between_points_on_arc_ct(
                self.important_points['7'],
                self.important_points['2347'],
            ),
            '6_67': self._get_points_between_points_on_arc_ct(
                self.important_points['6'],
                self.important_points['67'],
            ),
            '6_0156': self._get_points_between_points_on_arc_ct(
                self.important_points['6'],
                self.important_points['0156'],
            ),
            '4_45': self._get_points_between_points_on_arc_cb(
                self.important_points['4'],
                self.important_points['45'],
            ),
            '4_2347': self._get_points_between_points_on_arc_cb(
                self.important_points['4'],
                self.important_points['2347'],
            ),
            '5_45': self._get_points_between_points_on_arc_cb(
                self.important_points['5'],
                self.important_points['45'],
            ),
            '5_0156': self._get_points_between_points_on_arc_cb(
                self.important_points['5'],
                self.important_points['0156'],
            ),
            '34_2347': self._get_points_between_points_on_circle_t(
                self.important_points['34'],
                self.important_points['2347'],
            ),
            '34_0345': self._get_points_between_points_on_circle_t(
                self.important_points['34'],
                self.important_points['0345'],
            ),
            '05_0345': self._get_points_between_points_on_circle_t(
                self.important_points['05'],
                self.important_points['0345'],
            ),
            '05_0156': self._get_points_between_points_on_circle_t(
                self.important_points['05'],
                self.important_points['0156'],
            ),
            '27_2347': self._get_points_between_points_on_circle_b(
                self.important_points['27'],
                self.important_points['2347'],
            ),
            '27_1267': self._get_points_between_points_on_circle_b(
                self.important_points['27'],
                self.important_points['1267'],
            ),
            '16_1267': self._get_points_between_points_on_circle_b(
                self.important_points['16'],
                self.important_points['1267'],
            ),
            '16_0156': self._get_points_between_points_on_circle_b(
                self.important_points['16'],
                self.important_points['0156'],
            ),
            'origin_23': self._get_points_between_points_on_line_0(
                self.origin,
                self.important_points['23'],
            ),
            '23_2347': self._get_points_between_points_on_line_0(
                self.important_points['23'],
                self.important_points['2347'],
            ),
            'origin_01': self._get_points_between_points_on_line_0(
                self.origin,
                self.important_points['01'],
            ),
            '01_0156': self._get_points_between_points_on_line_0(
                self.important_points['01'],
                self.important_points['0156'],
            ),
            'origin_3': self._get_points_between_points_on_line_45(
                self.origin,
                self.important_points['3'],
            ),
            '3_34': self._get_points_between_points_on_line_45(
                self.important_points['3'],
                self.important_points['34'],
            ),
            'origin_1': self._get_points_between_points_on_line_45(
                self.origin,
                self.important_points['1'],
            ),
            '1_16': self._get_points_between_points_on_line_45(
                self.important_points['1'],
                self.important_points['16'],
            ),
            'origin_03': self._get_points_between_points_on_line_90(
                self.origin,
                self.important_points['03'],
            ),
            '03_0345': self._get_points_between_points_on_line_90(
                self.important_points['03'],
                self.important_points['0345'],
            ),
            'origin_12': self._get_points_between_points_on_line_90(
                self.origin,
                self.important_points['12'],
            ),
            '12_1267': self._get_points_between_points_on_line_90(
                self.important_points['12'],
                self.important_points['1267'],
            ),
            'origin_0': self._get_points_between_points_on_line_135(
                self.origin,
                self.important_points['0'],
            ),
            '0_05': self._get_points_between_points_on_line_135(
                self.important_points['0'],
                self.important_points['05'],
            ),
            'origin_2': self._get_points_between_points_on_line_135(
                self.origin,
                self.important_points['2'],
            ),
            '2_27': self._get_points_between_points_on_line_135(
                self.important_points['2'],
                self.important_points['27'],
            ),
            '1_01': self._get_points_between_points_on_arc_cr(
                self.important_points['1'],
                self.important_points['01'],
            ),
            '1_1267': self._get_points_between_points_on_arc_cr(
                self.important_points['1'],
                self.important_points['1267'],
            ),
            '0_01': self._get_points_between_points_on_arc_cr(
                self.important_points['0'],
                self.important_points['01'],
            ),
            '0_0345': self._get_points_between_points_on_arc_cr(
                self.important_points['0'],
                self.important_points['0345'],
            ),
            '3_23': self._get_points_between_points_on_arc_cl(
                self.important_points['3'],
                self.important_points['23'],
            ),
            '3_0345': self._get_points_between_points_on_arc_cl(
                self.important_points['3'],
                self.important_points['0345'],
            ),
            '2_23': self._get_points_between_points_on_arc_cl(
                self.important_points['2'],
                self.important_points['23'],
            ),
            '2_1267': self._get_points_between_points_on_arc_cl(
                self.important_points['2'],
                self.important_points['1267'],
            ),
            '2_12': self._get_points_between_points_on_arc_ct(
                self.important_points['2'],
                self.important_points['12'],
            ),
            '2_2347': self._get_points_between_points_on_arc_ct(
                self.important_points['2'],
                self.important_points['2347'],
            ),
            '1_12': self._get_points_between_points_on_arc_ct(
                self.important_points['1'],
                self.important_points['12'],
            ),
            '1_0156': self._get_points_between_points_on_arc_ct(
                self.important_points['1'],
                self.important_points['0156'],
            ),
            '3_03': self._get_points_between_points_on_arc_cb(
                self.important_points['3'],
                self.important_points['03'],
            ),
            '3_2347': self._get_points_between_points_on_arc_cb(
                self.important_points['3'],
                self.important_points['2347'],
            ),
            '0_03': self._get_points_between_points_on_arc_cb(
                self.important_points['0'],
                self.important_points['03'],
            ),
            '0_0156': self._get_points_between_points_on_arc_cb(
                self.important_points['0'],
                self.important_points['0156'],
            ),
        }

    def _init_grid_xy(self):
        xs_1 = np.linspace(
            start=0,
            stop=self.radius,
            num=self.resolution+1,
        )
        ys_1 = xs_1
        xs_2 = np.sqrt(self.radius_arc**2 - ys_1**2) - self.pos_arc
        xs_3 = np.concatenate([xs_1, xs_2])
        xs_4 = np.concatenate([xs_3, -xs_3])
        all_xs = np.unique(np.sort(xs_4))
        all_xs = np.around(all_xs, decimals=self.rounding_decimals)

        return all_xs, deepcopy(all_xs)

    def _get_xs_in_range(self, left: float, right: float):
        return self.all_xs[np.logical_and(
            (self.all_xs >= left),
            (self.all_xs <= right),
        )]

    def _get_ys_in_range(self, bottom: float, top: float):
        return self.all_ys[np.logical_and(
            (self.all_ys >= bottom),
            (self.all_ys <= top),
        )]

    def _get_xs_between_points(
        self,
        point_1: np.ndarray,
        point_2: np.ndarray
    ):
        x_left = min(point_1[0], point_2[0])
        x_right = max(point_1[0], point_2[0])
        if x_right - x_left < NEAR_ZERO:
            raise ValueError(
                "x_right == x_left for _get_xs_between_points"
            )
        return self._get_xs_in_range(
            left=x_left,
            right=x_right,
        )

    def _get_ys_between_points(self, point_1, point_2):
        y_bottom = min(point_1[1], point_2[1])
        y_top = max(point_1[1], point_2[1])
        if y_top - y_bottom < NEAR_ZERO:
            raise ValueError(
                "y_top == y_bottom for _get_ys_between_points"
            )
        return self._get_ys_in_range(
            bottom=y_bottom,
            top=y_top,
        )

    def _get_points_from_xy(self, xs, ys):
        xs = np.around(xs, decimals=self.rounding_decimals)
        ys = np.around(ys, decimals=self.rounding_decimals)
        return np.stack([xs, ys], axis=-1)

    def _get_points_on_line_0(self, xs):
        ys = np.zeros_like(xs)
        return self._get_points_from_xy(xs, ys)

    def _get_points_on_line_45(self, xs):
        ys = deepcopy(xs)
        return self._get_points_from_xy(xs, ys)

    def _get_points_on_line_90(self, ys):
        xs = np.zeros_like(ys)
        return self._get_points_from_xy(xs, ys)

    def _get_points_on_line_135(self, xs):
        ys = -xs
        return self._get_points_from_xy(xs, ys)

    def _get_points_between_points_on_line_0(self, point_1, point_2):
        xs = self._get_xs_between_points(
            point_1=point_1,
            point_2=point_2,
        )
        return self._get_points_on_line_0(xs=xs)

    def _get_points_between_points_on_line_45(self, point_1, point_2):
        xs = self._get_xs_between_points(
            point_1=point_1,
            point_2=point_2,
        )
        return self._get_points_on_line_45(xs=xs)

    def _get_points_between_points_on_line_90(self, point_1, point_2):
        ys = self._get_ys_between_points(
            point_1=point_1,
            point_2=point_2,
        )
        return self._get_points_on_line_90(ys=ys)

    def _get_points_between_points_on_line_135(self, point_1, point_2):
        xs = self._get_xs_between_points(
            point_1=point_1,
            point_2=point_2,
        )
        return self._get_points_on_line_135(xs=xs)

    def _get_points_on_arc_cr(self, ys):
        xs = - (np.sqrt(self.radius_arc**2-ys**2) - self.pos_arc)
        return self._get_points_from_xy(xs, ys)

    def _get_points_on_arc_cl(self, ys):
        xs = np.sqrt(self.radius_arc**2-ys**2) - self.pos_arc
        return self._get_points_from_xy(xs, ys)

    def _get_points_on_arc_ct(self, xs):
        ys = - (np.sqrt(self.radius_arc**2-xs**2) - self.pos_arc)
        return self._get_points_from_xy(xs, ys)

    def _get_points_on_arc_cb(self, xs):
        ys = np.sqrt(self.radius_arc**2-xs**2) - self.pos_arc
        return self._get_points_from_xy(xs, ys)

    def _get_points_between_points_on_arc_cr(self, point_1, point_2):
        ys = self._get_ys_between_points(point_1, point_2)
        return self._get_points_on_arc_cr(ys=ys)

    def _get_points_between_points_on_arc_cl(self, point_1, point_2):
        ys = self._get_ys_between_points(point_1, point_2)
        return self._get_points_on_arc_cl(ys=ys)

    def _get_points_between_points_on_arc_ct(self, point_1, point_2):
        xs = self._get_xs_between_points(point_1, point_2)
        return self._get_points_on_arc_ct(xs=xs)

    def _get_points_between_points_on_arc_cb(self, point_1, point_2):
        xs = self._get_xs_between_points(point_1, point_2)
        return self._get_points_on_arc_cb(xs=xs)

    def _get_points_on_circle_t(self, xs):
        ys = np.sqrt(self.radius**2-xs**2)
        return self._get_points_from_xy(xs, ys)

    def _get_points_on_circle_b(self, xs):
        ys = - np.sqrt(self.radius**2-xs**2)
        return self._get_points_from_xy(xs, ys)

    def _get_points_between_points_on_circle_t(self, point_1, point_2):
        xs = self._get_xs_between_points(point_1, point_2)
        return self._get_points_on_circle_t(xs=xs)

    def _get_points_between_points_on_circle_b(self, point_1, point_2):
        xs = self._get_xs_between_points(point_1, point_2)
        return self._get_points_on_circle_b(xs=xs)

    def get_edges_of_area(self, area_id: str):
        # goal
        edges = []

        vertex_ids = area_id.split('_')
        for ids in itertools.combinations(vertex_ids, 2):
            curve_id = self.__class__.get_composite_id_from_vertex_ids(ids)
            edges.append(self.important_curves[curve_id])
        return edges






