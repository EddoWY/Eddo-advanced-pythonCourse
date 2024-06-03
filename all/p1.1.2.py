def func(x):
    # return x % 2 != 0
    return x % 2 == 0


print(list(filter(func, range(10))))
