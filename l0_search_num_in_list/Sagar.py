import random
x = random.randint(1,10)
y = 0
print("Number game!")
print("3 tries!")
z = 0
while y != x:
    z = z + 1
    y = int(input("Guess a number:"))
    if y == x:
        print("Good guess! You got it! You took",z,"tries")
    elif y > x:
        print("Too high")
    elif y < x:
        print("Too low")
    if z > 3:
        print("You lose. You took too many tries.")
        break
