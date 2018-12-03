from functools import reduce
import re

import numpy as np

PARSER_PATTERN = re.compile(
    r"\#(?P<id>\d+) \@ (?P<x>\d+),(?P<y>\d+)\: (?P<width>\d+)x(?P<height>\d+)"
)
DIMENSIONS = (1000, 1000)

fabric = np.zeros(DIMENSIONS)


def parse_line(line):
    result = re.match(PARSER_PATTERN, line)
    result = tuple(map(int, result.group(1, 2, 3, 4, 5)))
    return result


def reduce_helper(fabric, line):
    (i, x, y, width, height) = parse_line(line)
    new_cut = np.zeros(DIMENSIONS)
    new_cut[x:x+width, y:y+height] = 1
    return np.add(fabric, new_cut)


with open('input') as f:
    fabric = reduce(reduce_helper, f, fabric)
    print(fabric)
    print()
    print(len(fabric[fabric>1]))
