# Implement the function find_roots to find the roots of the quadratic equation: ax2 + bx + c = 0. The
# function should return a tuple containing roots in any order. If the equation has only one solution, the
# function should return that solution as both elements of the tuple. The equation will always have at least one
# solution.
# The roots of the quadratic equation can be found with the following formula:
# For example, find_roots(2, 10, 8) should return (-1, -4) or (-4, -1) as the roots of the equation 2x2 + 10x + 8
# = 0 are -1 and -4.
import numpy as np


def find_roots(a, b, c):
    root_1 =int((-b + np.sqrt(np.square(b) - 4 * a * c)) / (2 * a))
    root_2 = int((-b - np.sqrt(np.square(b) - 4 * a * c)) / (2 * a))
    root = [root_1, root_2]
    return tuple(root)


print((find_roots(2, 10, 8)))
