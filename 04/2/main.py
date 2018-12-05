from functools import reduce
from collections import Counter, defaultdict
import operator
import re


PARSER_PATTERN = re.compile(
    r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] ([\w #]+)"
)
GUARD_PATTERN = re.compile(
    r"Guard #(\d+) begins shift"
)


def parse_line(line):
    result = re.match(PARSER_PATTERN, line).group(1, 2)
    return result


def reduce_helper(d, line):
    (k, v) = parse_line(line)
    d[k] = v
    return d


def parse_events(d):
    guard_id = None
    asleep = None
    total_sleep = defaultdict(int)

    def get_min(t):
        return int(t[-2:])

    for k in sorted(d.keys()):
        v = d[k]
        if v[0] == 'w':
            awake = get_min(k)
            for i in range(asleep, awake):
                total_sleep[(guard_id, i)] += 1
        elif v[0] == 'f':
            asleep = get_min(k)
        elif v[0] == 'G':
            guard_id = re.match(GUARD_PATTERN, v).group(1)

    return total_sleep


def main():
    d = dict()
    with open('input') as f:
        d = reduce(reduce_helper, f, d)
    ts = parse_events(d)
    m = max(ts.items(), key=operator.itemgetter(1))[0]
    return int(m[0]) * int(m[1])


if __name__ == "__main__":
    print(main())
