"""Teaching about functions in Python."""

a = 3

y = input("Enter number: ")  # returns a string
y = int(y)  # convert string to number


def is_multiple(numer, denom):
    """return if number is divisible by another."""
    return numer % denom == 0


def see_div(x):
    """Check if number is divisible by 3."""
    if is_multiple(x, 3):
        print("Divisible by 3")
    else:
        print("Not divisible by 3")


print(is_multiple(1171, 17))

see_div(y)
