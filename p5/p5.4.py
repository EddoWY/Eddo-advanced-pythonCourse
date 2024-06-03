def check_id_valid(id_number):
    """
    Checks if the given ID number is valid according to the checksum algorithm.

    :param id_number: ID number to be checked
    :type id_number: int
    :return: True if the ID number is valid, False otherwise
    :rtype: bool
    """
    # Convert the ID number to a string and create a list of its digits
    id_str = str(id_number).zfill(9)  # Ensure it's 9 digits by padding with zeros if necessary
    id_digits = [int(digit) for digit in id_str]

    # Multiply each digit by 1 or 2 based on its position
    multiplied_digits = [(digit if i % 2 == 0 else digit * 2) for i, digit in enumerate(id_digits)]

    # Sum the digits of each number, splitting those greater than 9
    summed_digits = [digit if digit < 10 else digit - 9 for digit in multiplied_digits]

    # Sum all the results
    total_sum = sum(summed_digits)

    # Check if the sum is divisible by 10
    return total_sum % 10 == 0


class IDIterator:
    """
    An iterator class that generates valid ID numbers starting from a given ID.
    """

    def __init__(self, start_id):
        """
        Initializes the IDIterator with a starting ID.

        :param start_id: The starting ID number
        :type start_id: int
        :raise ValueError: If the starting ID is not between 0 and 999999999
        """
        if not (0 <= start_id <= 999999999):
            raise ValueError("ID must be between 0 and 999999999")
        self._id = start_id + 1  # Start from the next ID

    def __iter__(self):
        """
        Returns the iterator object itself.

        :return: The iterator object
        :rtype: IDIterator
        """
        return self

    def __next__(self):
        """
        Returns the next valid ID number.

        :return: The next valid ID number
        :rtype: int
        :raise StopIteration: If the end of the ID range is reached
        """
        while self._id <= 999999999:
            current_id = self._id
            self._id += 1
            if check_id_valid(current_id):
                return current_id
        raise StopIteration


def id_generator(start_id):
    """
    A generator function that yields valid ID numbers starting from a given ID.

    :param start_id: The starting ID number
    :type start_id: int
    :yield: The next valid ID number
    :rtype: int
    """
    current_id = start_id + 1  # Start from the next ID
    while current_id <= 999999999:
        if check_id_valid(current_id):
            yield current_id
        current_id += 1


def main():
    """
    The main function to run the ID number generator or iterator based on user input.
    """
    user_input = input("Enter ID: ")
    start_id = int(user_input)

    method = input("Generator or Iterator? (gen/it): ").strip().lower()

    if method == 'it':
        iterator = IDIterator(start_id)
        for _ in range(10):
            try:
                print(next(iterator))
            except StopIteration:
                break
    elif method == 'gen':
        generator = id_generator(start_id)
        for _ in range(10):
            try:
                print(next(generator))
            except StopIteration:
                break
    else:
        print("Invalid input. Please enter 'gen' or 'it'.")


if __name__ == "__main__":
    main()