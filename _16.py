import functools
print(functools.reduce(lambda x, y: int(x) + int(y), list(str(2**1000))))
