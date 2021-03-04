import numpy as np


def velfield(n):
    '''Calculates a grid and vectors for the vector field.'''

    x = np.linspace(-0.5*np.pi, 0.5*np.pi, n)

    [X, Y] = np.meshgrid(x, x)
    u = np.cos(X)*np.sin(Y)
    v = -np.sin(X)*np.cos(Y)

    return X, Y, u, v
