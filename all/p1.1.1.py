def magic(a, b):
    return a * b


list_one = [1, 2, -5, 6]
list_two = [2, -1, 3, 4]
print(list(map(magic, list_one, list_two)))
