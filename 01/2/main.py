import itertools

lst = []
with open('input') as f:
    lst = [int(line[:-1]) for line in f]

lst_iter = itertools.cycle(lst)

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
