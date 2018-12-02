from collections import Counter
from functools import reduce


def filter_count(cntrs, allowed_value):
    return reduce(
        lambda acc, cntr: acc+1 if allowed_value in cntr.values() else acc,
        cntrs,
        0
    )

with open('input') as f:
    box_id_counts = list(map(lambda x: Counter(x[:-1]), f))

filtered_2 = filter_count(box_id_counts, 2)
filtered_3 = filter_count(box_id_counts, 3)

print(filtered_2)
print(filtered_3)

print(filtered_2*filtered_3)
