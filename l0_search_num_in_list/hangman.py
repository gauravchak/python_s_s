import random
import os
import time

print("Today, we are going...")
time.sleep(1)
print()
print("to play")
time.sleep(1)
print()
print("HANGMAN!!!!")
time.sleep(1)
os.system("clear")
words = [
    "Butterfly", "Torch", "Lantern", "Moon", "Castle", "Landscape", "Climb",
    "Notebook", "Silent", "Rainbow", "Grass", "Ship", "Planet", "Adventure",
    "Star", "Harvest", "Playground", "Sunlight", "Apple", "Waterfall", "Tree",
    "Yellow", "Rock", "Journey", "Frost", "Treasure", "Discovery"
]
#27 words
word_index = random.randint(0, 26)
y = words[word_index].lower()
print(f"This is your word: {y}")

s = [False] * len(y)
#Variables:
#y:word s:list of states x:letter guessed

def print_word(s,y):
    for i in range(len(y)):
        if s[i] == False:
            print("_",end = " ")
        else:
            print(y[i], end = " ")

#Variables:
#y:word s:list of states x:letter guessed

def change(s,y,x):
    found = False
    for i in range(len(y)):
        if x == y[i]:
            s[i] = True
            found = True
    return found

def all_true(s):
    "return False if any of the values in s is false"
    #    for i in range(len(s)):
    for x in s:
        # x takes values in s
        if x == False:
            return False
    return True

#Main code
#m:mistakes

m = 0
while m < 10:
    print_word(s,y)
    x = input("What letter do you want to guess?")
    found_letter = change(s,y,x)
    if found_letter == True:
        print("Good job! You guessed a letter!")
        if all_true(s) == True:
            print("You guessed the word!")
            break
    elif found_letter == False:
        m = m + 1
        n = 10 - m
        print("Wrong letter. You have ",n," mistakes left.")




