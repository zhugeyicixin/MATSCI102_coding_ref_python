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


def plot_seq_score_framework(
    x_lim: list,
    y_lim: list,
    fig: Optional[plt.Figure] = None,
    ax: Optional[plt.Axes] = None,
    max_score: Optional[float] = None,
    **kwargs,
):
    fig, ax = fig_from_fig_or_none(fig=fig, ax=ax)

    if max_score is not None:
        ax.plot(
            x_lim,
            [max_score, max_score],
            linestyle='--',
            color='g',
        )

    ax.set_xlim(left=x_lim[0], right=x_lim[1])
    ax.set_ylim(bottom=y_lim[0], top=y_lim[1])
    ax.set_xlabel('Number of samples', size=36)
    ax.set_ylabel('Score', size=36)
    ax.tick_params(axis='x', which='major', labelsize=32)
    ax.tick_params(axis='y', which='major', labelsize=32)

    return fig, ax


def plot_seq_score_data(
    scores: Union[list, np.ndarray],
    ax: plt.Axes,
    color: str = 'tab:blue',
    label: Optional[str] = None,
    **kwargs,
):
    scores = list(scores)
    scores.insert(0, 0.0)
    p_1 = ax.plot(
        scores,
        marker='o',
        markersize=10,
        color=color,
        label=label,
    )[0]
    return p_1


def plot_seq_score(
    scores: Union[list, np.ndarray],
    max_score: Optional[float] = None,
    x_lim: Optional[list] = None,
    y_lim: Optional[list] = None,
    show_fig: bool = True,
):
    if max_score is None:
        max_score = max(scores)
    if x_lim is None:
        x_lim = [-0.5, len(scores) + 0.5]
    if (y_lim is None):
        y_lim = [-0.05, max_score*1.05]

    fig, ax = plot_seq_score_framework(
        x_lim=x_lim,
        y_lim=y_lim,
        max_score=max_score,
    )
    p_1 = plot_seq_score_data(
        scores=scores,
        ax=ax,
    )

    if show_fig:
        plt.show()

    return fig