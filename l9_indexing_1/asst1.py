def printfn(x: int):
    """
    A recursive function that prints numbers from x down to 0, inclusive.
    When it reaches 0, it prints "Blastoff!".
    """
    if x == 0:
        print("Blastoff!")
    else:
        print(x)
        printfn(x - 1)


printfn(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Blastoff!
