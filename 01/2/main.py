import itertools

f = open('input')

lst_iter = itertools.cycle(
    map(lambda x: int(x[:-1]), f)
)

temp = 0
freq = set()

for i in lst_iter:
    if temp in freq:
        print(temp)
        break
    freq.add(temp)
    temp += i

f.close()
