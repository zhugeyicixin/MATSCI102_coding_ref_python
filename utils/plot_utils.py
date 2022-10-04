from matplotlib import pyplot as plt
from typing import (
    Union,
    Optional,
    List,
)
import numpy as np


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
        point[0],
        point[1],
        **kwargs,
    )


def plot_a_line(
    point_1: np.ndarray,
    point_2: np.ndarray,
    ax: plt.Axes,
    **kwargs,
):
    ax.plot(
        [point_1[0], point_2[0]],
        [point_1[1], point_2[1]],
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