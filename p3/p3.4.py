import re
import string


class UsernameContainsIllegalCharacter(Exception):
    """
    Exception raised when the username contains an illegal character.

    Attributes
    ----------
    username : str
        The username that caused the exception
    character : str
        The illegal character in the username
    index : int
        The index of the illegal character in the username
    """

    def __init__(self, username, character, index):
        self.username = username
        self.character = character
        self.index = index

    def __str__(self):
        return f"Username '{self.username}' contains an illegal character '{self.character}' at index {self.index}"


class UsernameTooShort(Exception):
    """
    Exception raised when the username is too short.

    Attributes
    ----------
    username : str
        The username that caused the exception
    """

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"Username '{self.username}' is too short. It must be at least 3 characters long."


class UsernameTooLong(Exception):
    """
    Exception raised when the username is too long.

    Attributes
    ----------
    username : str
        The username that caused the exception
    """

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"Username '{self.username}' is too long. It must be at most 16 characters long."


class PasswordMissingCharacter(Exception):
    """
    Base exception class for missing character types in the password.

    Attributes
    ----------
    password : str
        The password that caused the exception
    missing_type : str
        The type of character that is missing in the password
    """

    def __init__(self, password, missing_type):
        self.password = password
        self.missing_type = missing_type

    def __str__(self):
        return f"Password is missing a {self.missing_type}."


class PasswordMissingUppercase(PasswordMissingCharacter):
    """
    Exception raised when the password is missing an uppercase letter.
    """

    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    """
    Exception raised when the password is missing a lowercase letter.
    """

    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    """
    Exception raised when the password is missing a digit.
    """

    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    """
    Exception raised when the password is missing a special character.
    """

    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    """
    Exception raised when the password is too short.

    Attributes
    ----------
    password : str
        The password that caused the exception
    """

    def __init__(self, password):
        self.password = password

    def __str__(self):
        return f"Password is too short. It must be at least 8 characters long."


class PasswordTooLong(Exception):
    """
    Exception raised when the password is too long.

    Attributes
    ----------
    password : str
        The password that caused the exception
    """

    def __init__(self, password):
        self.password = password

    def __str__(self):
        return f"Password is too long. It must be at most 40 characters long."


def check_input(username, password):
    """
    Checks if the username and password meet the required conditions.

    Parameters
    ----------
    username : str
        The username to be checked
    password : str
        The password to be checked

    Raises
    ------
    UsernameContainsIllegalCharacter
        If the username contains an illegal character
    UsernameTooShort
        If the username is too short
    UsernameTooLong
        If the username is too long
    PasswordTooShort
        If the password is too short
    PasswordTooLong
        If the password is too long
    PasswordMissingLowercase
        If the password is missing a lowercase letter
    PasswordMissingUppercase
        If the password is missing an uppercase letter
    PasswordMissingDigit
        If the password is missing a digit
    PasswordMissingSpecial
        If the password is missing a special character
    """
    # Check if the username contains illegal characters
    if not re.match(r'^[A-Za-z0-9_]+$', username):
        for index, char in enumerate(username):
            if not re.match(r'^[A-Za-z0-9_]+$', char):
                raise UsernameContainsIllegalCharacter(username, char, index)

    # Check if the username is too short
    if len(username) < 3:
        raise UsernameTooShort(username)

    # Check if the username is too long
    if len(username) > 16:
        raise UsernameTooLong(username)

    # Check if the password is too short
    if len(password) < 8:
        raise PasswordTooShort(password)

    # Check if the password is too long
    if len(password) > 40:
        raise PasswordTooLong(password)

    # Check if the password contains all required character types
    if not any(c.islower() for c in password):
        raise PasswordMissingLowercase(password, "lowercase letter")
    if not any(c.isupper() for c in password):
        raise PasswordMissingUppercase(password, "uppercase letter")
    if not any(c.isdigit() for c in password):
        raise PasswordMissingDigit(password, "digit")
    if not any(c in string.punctuation for c in password):
        raise PasswordMissingSpecial(password, "special character")

    # If all checks pass, print OK
    print("OK")


def main():
    """
    Main function to get user input and check if the credentials are valid.
    """
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            check_input(username, password)
            break  # Exit loop if input is valid
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()