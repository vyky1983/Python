def concatenation(*params):
    res: str = ''
    for item in params:
        res += item
    return res


print(concatenation('a', 's', 'd', 'w'))  # asdw
print(concatenation('a', '1', 'd', '2'))  # a1d2
# print(concatenation(1, 2, 3, 4)) # Type Error


