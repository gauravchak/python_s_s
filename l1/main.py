import time

x = int(input("Enter a number: "))

# in a loop from 1 to 10 keep doing this: if odd then add 5, else divide by 2
# and print the result and sleep for 1 second
for i in range(1, 11):
    if x % 2 == 1:
        # This means that the remainder when divided by 2 is 1, which means it
        # is an odd number
        x += 5
    else:
        # This means that the remainder when divided by 2 is 0, which means it
        # is an even number
        x //= 2  # This is same as x = int(x / 2)
    print(x)
    time.sleep(1)
