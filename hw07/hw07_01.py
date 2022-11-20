import numpy as np
from matplotlib import pyplot as plt

from utils.constants import hbar, m_e, k_B, J_to_eV

__author__ = 'Tanjin He'
__maintainer__ = 'Tanjin He'
__email__ = 'tanjin_he@berkeley.edu'

def calc_1d():
    L = 4.28E-10
    n = 2
    k_f = ((3*(np.pi**2)*n)**(1/3))/L
    E_f = ((hbar*k_f)**2)/2/m_e
    v_f = hbar*k_f/m_e
    T_f = E_f/k_B
    print('E_f', E_f*J_to_eV)
    print('v_f', v_f)
    print('T_f', T_f)


if __name__ == '__main__':

    calc_1d()