import itertools

f = open('input')

lst_iter = itertools.cycle(
    map(lambda x: int(x[:-1]), f)
)

temp = 0
freq = dict()

for i in lst_iter:
    v = freq.get(temp, 0)
    if not v == 0:
        print(temp)
        break
    v = v+1
    freq[temp] = v
    temp = temp + i

f.close()
