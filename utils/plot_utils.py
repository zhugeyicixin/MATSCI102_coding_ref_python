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


def plot_an_edge(
    site_1: np.ndarray,
    site_2: np.ndarray,
    ax: plt.Axes,
    **kwargs
):
    ax.plot(
        [site_1[0], site_2[0]],
        [site_1[1], site_2[1]],
        **kwargs
    )

