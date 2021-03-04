from two_b import *


def test_mesh_grid():
    expected = (1, 2)
    x, y = mesh_grid(0, 10, 11)
    e = 10e-10

    # the x and y values are expressed as x[y-coord][x-coord]
    assert abs(expected[0] - x[2][1]) < e
    assert abs(expected[1] - y[2][1]) < e


def test_streamlines_at_2_3():
    expected = 6
    x, y = mesh_grid(0, 10, 11)
    f = streamlines(x, y, x*y)
    e = 10e-10

    assert abs(expected - f[2][3]) < e


def test_vec_field_at_2_4():
    expected = (2, 4)
    x, y = mesh_grid(0, 10, 11)
    # Only includes every second element from the whole range.
    u, v, skip = vec_field(x, y, x, y, 2)
    e = 10e-10

    print(f'{u}\n\n')
    print(f'{v}\n\n')
    print(f'{x}\n\n')
    print(f'{y}\n\n')

    # The x and y values are expressed as x[y-coord/2][x-coord/2]
    assert abs(expected[0] - u[2][1]) < e
    assert abs(expected[1] - v[2][1]) < e
