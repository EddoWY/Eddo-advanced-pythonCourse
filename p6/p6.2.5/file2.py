# file2.py

from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self):
        super().__init__()
        self._sender_age = 0

    def greeting_msg(self):
        super().greeting_msg()
        print(f"Happy birthday! Sender's age: {self._sender_age}")