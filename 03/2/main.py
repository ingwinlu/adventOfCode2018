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

    existing = fabric[x:x+width, y:y+height]
    existing = existing[existing > 0]

    if np.any(existing > 0):
        values_in_existing = np.unique(existing)
        for v in values_in_existing:
            fabric[fabric == v] = np.inf
        fabric[x:x+width, y:y+height] = np.inf
    else:
        fabric[x:x+width, y:y+height] = i
    return fabric


with open('input') as f:
    fabric = reduce(reduce_helper, f, fabric)
    unique = np.unique(fabric)
    unique = unique[(unique > 0) & (unique < np.inf)]
    print(unique[0])
