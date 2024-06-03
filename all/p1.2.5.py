import functools


def function(acc, item):
    # return num + 1
    return acc + 1
    # return acc + item


password = input("Enter Your password (integers only): ")
lst = list(map(int, password))
magic = functools.reduce(function, lst)
result = (lambda x: x % 4 == 0)(magic)
if result:
    print("Correct password!")
else:
    print("Wrong password.")

print(result)
def mod4(x):
    return x % 4 == 0


print(mod4(magic))
