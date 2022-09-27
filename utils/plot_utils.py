from matplotlib import pyplot as plt
from typing import (
    Union,
    Optional,
)
import numpy as np


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


