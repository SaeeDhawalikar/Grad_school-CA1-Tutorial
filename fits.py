import numpy as np
from astropy.io import fits

def read_this(f1):
    '''Reads the given fits file f1, and returns 6 arrays'''
    with fits.open(f1) as hdul:
        hdul.info()
        data = hdul[1].data
        A = data['A'][0]
        B = data['B'][0]
        C = data['C'][0]
        D = data['D'][0]
        E = data['E'][0]
        F = data['F'][0]

    O=[A, B, C, D, E, F]
    return O



