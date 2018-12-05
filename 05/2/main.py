from collections import defaultdict
from itertools import tee, zip_longest
import operator
from string import ascii_lowercase

import numpy as np


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip_longest(a, b)


def run(lst):
    modified = False
    skip = False
    tmp = []
    for s0, s1 in pairwise(lst):
        if skip:
            skip = False
            continue
        if s1 is None:
            tmp.append(s0)
            break
        if s0 != s1 and s0.lower() == s1.lower():
            modified = True
            skip = True
            continue
        else:
            tmp.append(s0)
    return tmp, modified


def main():
    counter = defaultdict(int)

    with open('input') as f:
        lst = list(f.read()[:-1])

    lst = np.array(lst)

    for c in ascii_lowercase:
        print(c)
        tmp = lst[
            (lst != c) &
            (lst != c.upper())
        ].tolist()
        rerun = True
        while rerun:
            tmp, rerun = run(tmp)
        counter[c] = len(tmp)

    m = min(counter.items(), key=operator.itemgetter(1))
    return m


if __name__ == "__main__":
    print(main())
