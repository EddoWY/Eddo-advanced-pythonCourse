numbers = iter(list(range(1, 101)))

while True:
    try:
        # Print the current number (every third number)
        print(next(numbers))

        # Skip the next two numbers
        next(numbers)
        next(numbers)
    except StopIteration:
        # If StopIteration is raised, break from loop
        break
        