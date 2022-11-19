import numpy as np

from utils.constants import (
    permittivity_vacuum,
    charge_elementary,
    eV_to_J,
    ang_to_m,
)


__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'



def calc_Madelung_KCl_2D_uv(value_range=100):
    """
    Seems not correct? Why?

    :param value_range:
    :return:
    """

    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v = np.meshgrid(u_, v_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    A_1 = (u**2 + v**2)
    A_1 = A_1.flatten()
    A_1 = np.power(A_1, 0.5)
    A_1 = 1.0 / A_1
    A_1[np.isinf(A_1)] = 0.0

    # A_2 = ((u+v+1)**2 + (v+w+1)**2 + (w+u+1)**2)/4
    A_2 = ((u+0.5)**2 + (v+0.5)**2 )
    A_2 = A_2.flatten()
    A_2 = np.power(A_2, 0.5)
    A_2 = 1.0 / A_2

    result = A_1 - A_2
    result = np.sum(result)

    return result


def calc_Madelung_KCl_2D_ij(value_range=100):
    """
    Seems not correct? Why?

    :param value_range:
    :return:
    """

    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v = np.meshgrid(u_, v_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    A_1 = (-1.0)**(u+v)/np.sqrt(u**2 + v**2)
    A_1 = A_1.flatten()
    A_1[np.isinf(A_1)] = 0.0

    result = np.sum(A_1)

    return result





def calc_LJ_KCl_2D_uv(value_range=100):
    """
    Seems not correct? Why?

    :param value_range:
    :return:
    """

    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v = np.meshgrid(u_, v_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    A_1 = (u**2 + v**2)
    A_1 = A_1.flatten()
    A_1 = np.power(A_1, 6)
    A_1 = 1.0 / A_1
    A_1[np.isinf(A_1)] = 0.0

    # A_2 = ((u+v+1)**2 + (v+w+1)**2 + (w+u+1)**2)/4
    A_2 = ((u+0.5)**2 + (v+0.5)**2 )
    A_2 = A_2.flatten()
    A_2 = np.power(A_2, 6)
    A_2 = 1.0 / A_2

    result = A_1 + A_2
    result = np.sum(result)

    return result


def calc_LJ_KCl_2D_ij(value_range=100):
    """
    Seems not correct? Why?

    :param value_range:
    :return:
    """

    u_ = np.arange(-value_range, value_range+1, dtype=float)
    v_ = np.arange(-value_range, value_range+1, dtype=float)

    u, v = np.meshgrid(u_, v_, indexing='ij')

    # assert np.all(u[:, 0, 0] == u_)
    # assert np.all(v[0, :, 0] == v_)
    # assert np.all(w[0, 0, :] == w_)

    A_1 = 1.0/(u**2 + v**2)**6
    A_1 = A_1.flatten()
    A_1[np.isinf(A_1)] = 0.0

    result = np.sum(A_1)

    return result



def calc_distance_KCl(
    sigma: float,
    epsilon: float,
    value_range=100,
):
    sum_1 = calc_Madelung_KCl_2D_ij(
        value_range=value_range,
    )
    sum_2 = calc_LJ_KCl_2D_ij(
        value_range=value_range,
    )
    coeff_1 = charge_elementary**2/4/np.pi/permittivity_vacuum*sum_1
    coeff_2 = 4*epsilon*sigma**12*sum_2

    d_0 = np.power(-12*coeff_2/coeff_1, 1./11.)

    return d_0


def calc_cohesive_energy_KCl(
    d: float,
    sigma: float,
    epsilon: float,
    value_range=100,
):
    sum_1 = calc_Madelung_KCl_2D_ij(
        value_range=value_range,
    )
    sum_2 = calc_LJ_KCl_2D_ij(
        value_range=value_range,
    )
    coeff_1 = charge_elementary**2/4/np.pi/permittivity_vacuum*sum_1
    coeff_2 = 4*epsilon*sigma**12*sum_2

    energy = coeff_1/d + coeff_2/d**12
    return energy



if __name__ == '__main__':

    sigma = 3.40*ang_to_m
    epsilon = 0.0104*eV_to_J

    d_0 = calc_distance_KCl(
        sigma=sigma,
        epsilon=epsilon,
        value_range=1000,
    )
    print('d_0', d_0/ang_to_m)

    e_coh = calc_cohesive_energy_KCl(
        d=d_0,
        sigma=sigma,
        epsilon=epsilon,
        value_range=1000,
    )
    print('e_coh', e_coh/eV_to_J)

