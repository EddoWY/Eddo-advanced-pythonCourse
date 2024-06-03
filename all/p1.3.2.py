def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))


print(is_prime(42))
print(is_prime(43))
