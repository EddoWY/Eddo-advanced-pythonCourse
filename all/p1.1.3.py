import functools


def f(a, b):
    if a < b:
        return a
    else:
        return b


print(functools.reduce(f, [47, 11, 42, 102, 13]))
