from functools import reduce

with open('input') as f:
    print(reduce(lambda a,b: a + int(b), f, 0))
