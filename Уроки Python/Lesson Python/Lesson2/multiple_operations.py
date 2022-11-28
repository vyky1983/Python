a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()
u = a.union(b)
i = a.intersection(b)
dl = a.difference(b)
dr = b.difference(a)

q = a\
    .union(b)\
    .difference(a.intersection(b))
print(dl)

s = frozenset(a)
print(a)
print(u)
print(s)
