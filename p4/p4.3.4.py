def get_fibo():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
