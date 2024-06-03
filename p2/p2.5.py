class Animal:
    """
    A class used to represent an animal in the zoo.

    Attributes
    ----------
    zoo_name : str
        The name of the zoo shared by all instances of Animal
    """
    # Class attribute shared by all instances
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """
        Initialize the animal with a name and hunger level.

        Parameters
        ----------
        name : str
            The name of the animal
        hunger : int, optional
            The hunger level of the animal (default is 0)
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        Return the name of the animal.

        Returns
        -------
        str
            The name of the animal
        """
        return self._name

    def is_hungry(self):
        """
        Return True if the animal is hungry (hunger level > 0), otherwise False.

        Returns
        -------
        bool
            True if the animal is hungry, False otherwise
        """
        return self._hunger > 0

    def feed(self):
        """
        Decrease the hunger level by 1 if the animal is hungry.
        """
        if self._hunger > 0:
            self._hunger -= 1

    def talk(self):
        """
        Placeholder method to be overridden in subclasses.
        """
        pass


class Dog(Animal):
    def talk(self):
        """
        Dog's way of talking.
        """
        print("woof woof")

    def fetch_stick(self):
        """
        Unique method for Dog.
        """
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        """
        Cat's way of talking.
        """
        print("meow")

    def chase_laser(self):
        """
        Unique method for Cat.
        """
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger, stink_count=6):
        """
        Initialize the skunk with name, hunger level, and stink count.

        Parameters
        ----------
        name : str
            The name of the skunk
        hunger : int
            The hunger level of the skunk
        stink_count : int, optional
            The stink count of the skunk (default is 6)
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """
        Skunk's way of talking.
        """
        print("tsssss")

    def stink(self):
        """
        Unique method for Skunk.
        """
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        """
        Unicorn's way of talking.
        """
        print("Good day, darling")

    def sing(self):
        """
        Unique method for Unicorn.
        """
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger, color="Green"):
        """
        Initialize the dragon with name, hunger level, and color.

        Parameters
        ----------
        name : str
            The name of the dragon
        hunger : int
            The hunger level of the dragon
        color : str, optional
            The color of the dragon (default is "Green")
        """
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """
        Dragon's way of talking.
        """
        print("Raaaawr")

    def breath_fire(self):
        """
        Unique method for Dragon.
        """
        print("$@#$#@$")


def main():
    """
    The main function to create animal instances and simulate zoo operations.
    """
    # Create a list of animal instances with specific attributes
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky", 0),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80)
    ]

    # Iterate over the list of animals
    for animal in zoo_lst:
        # Check if the animal is hungry
        if animal.is_hungry():
            print(f"{type(animal).__name__} {animal.get_name()}")
            # Feed the animal until it is no longer hungry
            while animal.is_hungry():
                animal.feed()
        # Make the animal talk
        animal.talk()
        # Call the unique method based on the animal's type
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    # Print the zoo name
    print(f"Zoo name: {Animal.zoo_name}")


if __name__ == "__main__":
    main()