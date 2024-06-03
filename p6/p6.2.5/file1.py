# file1.py

class GreetingCard:
    def __init__(self):
        self._recipient = "Dana Ev"
        self._sender = "Eyal Ch"

    def greeting_msg(self):
        print(f"Sender: {self._sender}")
        print(f"Recipient: {self._recipient}")