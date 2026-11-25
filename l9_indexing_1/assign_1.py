x = ("SOPHIA")
try:
    y = int(input("Type a number between 1 and 6 to find the corresponding letter in SOPHIA: "))
    y = y-1
    if y < 6 and y>=0:
        print(x[y])
    else:
        print()
        print(" I would APPRECIATE IT if you")
        print("WOULD NOT enter A NUMBER WHICH YOU KNOW is TOO HIGH!!!") 
        print("THANK you(but not thank you).")
except ValueError:
    print("Please enter a NUMBER. THANK you.")