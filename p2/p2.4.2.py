class BigThing:
    def __init__(self, thing):
        self.thing = thing

    def size(self):
        if isinstance(self.thing, (list, dict, str)):
            return len(self.thing)
        elif isinstance(self.thing, (int, float)):
            return self.thing
        else:
            raise TypeError("Unsupported type")


class BigCat(BigThing):
    def __init__(self, thing, weight):
        super().__init__(thing)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return "Very Fat"
        elif self.weight > 15:
            return "Fat"
        else:
            return "OK"


if __name__ == '__main__':
    my_thing = BigThing("balloon")
    print(my_thing.size())  # Output: 7

    my_thing = BigThing([1, 2, 3, 4])
    print(my_thing.size())  # Output: 4

    my_thing = BigThing(123)
    print(my_thing.size())  # Output: 123

    my_thing = BigThing({"key": "value"})
    print(my_thing.size())  # Output: 1

    cutie = BigCat("mitzy", 22)
    print(cutie.size())  # Output: Very Fat

    cutie = BigCat("mitzy", 18)
    print(cutie.size())  # Output: Fat

    cutie = BigCat("mitzy", 10)
    print(cutie.size())  # Output: OK
