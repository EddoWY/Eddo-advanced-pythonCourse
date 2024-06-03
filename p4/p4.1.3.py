def prime_generator(start):
    num = start
    while True:
        num += 1
        if is_prime(num):
            yield num


def first_prime_over(n):
    gen = prime_generator(n)
    return next(gen)


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(first_prime_over(1000000))
