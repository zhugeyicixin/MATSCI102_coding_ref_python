import numpy as np


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'


def get_polar_coordinate(radius: float, anlge: float):
    """

    :param radius:
    :param anlge: in radians
    :return:
    """
    return np.array((
        radius*np.cos(anlge), radius*np.sin(anlge)
    ))
