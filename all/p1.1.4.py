def secret(a):
    return a % 3 != 0 and a % 5 != 0

result = filter(secret, range(1, 31))
print(list(result))
