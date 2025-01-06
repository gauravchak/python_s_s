x = input("Enter the number to search: ")  # Taking input from user

x = int(x)  # Before this x was a word ( or string ) and now it is a number
# ( or integer )

print("You entered the number to search:", x)

# Now we will take a list of numbers from the user. We will want the user to
# enter numbers separated by space.
# We will then search the number entered by the user in the list.
# the user will enter something like "2 3 17 12"
l = input("Enter the list of numbers separated by space: ")
print("You entered list:", l)

# We will now convert the string of numbers to a list of numbers
# We will use the split() function to split the string into words
list_of_numbers_as_text = l.split(sep=",")
print("The list of numbers is", list_of_numbers_as_text)

# This converts the list of strings to list of a numbers
list_of_numbers_as_ints = [int(x) for x in list_of_numbers_as_text]

# Now we will search the number in the list
found = False
for i in list_of_numbers_as_ints:
    if i == x:
        print("The number", x, "is in the list")
        found = True
        break
if not found:
    print("The number", x, "is not in the list")
