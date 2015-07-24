class ShapeException(Exception):
    pass


def shape(x):
    return (len(x),)

def shape_check(x, y):
    if shape(x) != shape(y):
        raise ShapeException


def dot():
    pass


def magnitude():
    pass


def vector_add(x, y):
    v_add = []
    for index, variable in enumerate(x):
        v_add.append(variable + y[index])
    return v_add


def vector_sub(x, y):
    v_sub = []
    for index, variable in enumerate(x):
        v_sub.append(variable - y[index])
    return v_sub


def vector_sum(*args):

    pass


def vector_multiply():
    pass


def vector_mean():
    pass


def matrix_row():
    pass


def matrix_col():
    pass


def matrix_scalar_multiply():
    pass


def matrix_vector_multiply():
    pass


def matrix_matrix_multiply():
    pass
