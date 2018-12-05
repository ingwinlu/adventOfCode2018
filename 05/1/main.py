from itertools import tee, zip_longest


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
    with open('input') as f:
        lst = f.read()[:-1]

    rerun = True
    while rerun:
        lst, rerun = run(lst)

    return len(lst)


if __name__ == "__main__":
    print(main())
