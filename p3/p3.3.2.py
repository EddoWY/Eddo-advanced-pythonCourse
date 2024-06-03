class UnderAge(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        years_left = 18 - self.age
        return f"Your age is {self.age}. You will be able to attend the birthday in {years_left} year(s)."


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


send_invitation("Alice", 17)
send_invitation("Bob", 20)
