from functools import reduce

print(reduce(lambda a,b: a + int(b), open('input'), 0))
