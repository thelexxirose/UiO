'''
This test file has three test functions that test different values of the velfield function to ensure that it
returns the correct expected answers. Use the pytest module to use this test file.
'''

from velfield import velfield
from numpy import pi


def test_velfield_at_origin():
    '''Tests values at coordinates (0, 0)'''
    expected = (0.0, 0.0, 0.0, 0.0)
    x, y, u, v = velfield(5)

    e = 10e-10

    assert abs(x[2][2] - expected[0]) < e
    assert abs(y[2][2] - expected[1]) < e
    assert abs(u[2][2] - expected[2]) < e
    assert abs(v[2][2] - expected[3]) < e


def test_velfield_at_pihalf_pihalf():
    '''Tests values at coordinates (pi/2, pi/2)'''
    expected = (0.5*pi, 0.5*pi, 0.0, 0.0)
    x, y, u, v = velfield(5)

    e = 10e-10

    assert abs(x[4][4] - expected[0]) < e
    assert abs(y[4][4] - expected[1]) < e
    assert abs(u[4][4] - expected[2]) < e
    assert abs(v[4][4] - expected[3]) < e


def test_velfield_at_pihalf_zero():
    '''Tests values at coordinates (pi/2, 0)'''
    expected = (0.5*pi, 0.0, 0.0, -1.0)
    x, y, u, v = velfield(5)

    e = 10e-10

    assert abs(x[2][4] - expected[0]) < e
    assert abs(y[2][4] - expected[1]) < e
    assert abs(u[2][4] - expected[2]) < e
    assert abs(v[2][4] - expected[3]) < e
