class Animal:
    count_animals = 0

    def __init__(self, age, name='Octavio'):
        self._name = name
        self._age = age
        Animal.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age


if __name__ == '__main__':
    o1 = Animal(10)
    o2 = Animal(7, 'Cat')
    o1.birthday()
    print(f'{o1.get_name()}, {o1.get_age()}')
    print(f'{o2.get_name()}, {o2.get_age()}')
    o1.set_name('Dog')
    print(f'{o1.get_name()}, {o1.get_age()}')
    print(f'{o2.get_name()}, {o2.get_age()}')
    print(f'count animals {Animal.count_animals}')
