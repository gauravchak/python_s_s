def checkcard(t,a):
    if t != "E":
        if t[1] == "H" or t[1] == "D":
            if a[1] == "S" or a[1] == "C":
                if t[0] == "K" and a[0] == "Q":
                    return True
                elif t[0] == "Q" and a[0] == "J":
                    return True
                elif t[0] == "J" and a[0] == "T":
                    return True
                elif t[0] == "T" and a[0] == "9":
                    return True
                elif t[0] == "9" and a[0] == "8":
                    return True
                elif t[0] == "8" and a[0] == "7":
                    return True
                elif t[0] == "7" and a[0] == "6":
                    return True
                elif t[0] == "6" and a[0] == "5":
                    return True
                elif t[0] == "5" and a[0] == "4":
                    return True
                elif t[0] == "4" and a[0] == "3":
                    return True
                elif t[0] == "3" and a[0] == "2":
                    return True
                elif t[0] == "2" and a[0] == "1":
                    return True
                elif t[0] == "1" and a[0] == "A":
                    return True
    if t != "E":
        if t[1] == "S" or t[1] == "C":
            if a[1] == "D" or a[1] == "H":
                if t[0] == "K" and a[0] == "Q":
                    return True
                elif t[0] == "Q" and a[0] == "J":
                    return True
                elif t[0] == "J" and a[0] == "T":
                    return True
                elif t[0] == "T" and a[0] == "9":
                    return True
                elif t[0] == "9" and a[0] == "8":
                    return True
                elif t[0] == "8" and a[0] == "7":
                    return True
                elif t[0] == "7" and a[0] == "6":
                    return True
                elif t[0] == "6" and a[0] == "5":
                    return True
                elif t[0] == "5" and a[0] == "4":
                    return True
                elif t[0] == "4" and a[0] == "3":
                    return True
                elif t[0] == "3" and a[0] == "2":
                    return True
                elif t[0] == "2" and a[0] == "1":
                    return True
                elif t[0] == "1" and a[0] == "A":
                    return True

def place_hands(hand: str, piles: str) -> str:
    """
    looks at cards in hand and places on piles and returns final state
    """
    print(hand)
    print(piles)
    h = hand.split(" ")
    p = piles.split(" ")
    x1 = "E"
    x2 = "E"
    x3 = "E"
    x4 = "E"
    x5 = "E"
    x6 = "E"
    x7 = "E"
    x8 = "E"

    # I am given piles which are 4 cards.
    # I need to enter them in the cross.
    for i in p:
        if x1 == "E":
            x1 = i
        elif x3 == "E":
            x3 = i
        elif x5 == "E":
            x5 = i
        elif x7 == "E":
            x7 = i
    # Looking at all the kings and placing them in the firs available corner
    for i in h:
        if i[0] == "K":
            if x2 == "E":
                x2 = i
            elif x4 == "E":
                x4 = i
            elif x6 == "E":
                x6 = i
            elif x8 == "E":
                x8 = i
    placed = True
    while placed == True:
        placed = False
        for i in h:
            if checkcard(x1,i):
                x1 = i
                placed = True
                h.remove(i)
            elif checkcard(x2,i):
                x2 = i
                placed = True
                h.remove(i)
            elif checkcard(x3,i):
                x3 = i
                placed = True
                h.remove(i)
            elif checkcard(x4,i):
                x4 = i
                placed = True
                h.remove(i)
            elif checkcard(x5,i):
                x5 = i
                placed = True
                h.remove(i)
            elif checkcard(x6,i):
                x6 = i
                placed = True
                h.remove(i)
            elif checkcard(x7,i):
                x7 = i
                placed = True
                h.remove(i)
            elif checkcard(x8,i):
                x8 = i
                placed = True
                h.remove(i)
    y = (x1+" "+x2+" "+x3+" "+x4+" "+x5+" "+x6+" "+x7+" "+x8)
    return y

def test_full():
    # simple test case
    hand = "5C"
    piles = "6C 7S 6H 9H"
    print(f"place_hands({hand}, {piles}) = {place_hands(hand, piles)}")

    # two cards dependent on each other
    hand = "4H 5C"
    piles = "6C 7S 6H 9H"
    print(f"place_hands({hand}, {piles}) = {place_hands(hand, piles)}")

    # two cards dependent on each other with T
    hand = "9D TC"
    piles = "6C 7S JH 9H"
    print(f"place_hands({hand}, {piles}) = {place_hands(hand, piles)}")

    # when card in hadn matches two piles
    hand = "9D TC 8S"
    piles = "6C 7S JH 9H"
    print(f"place_hands({hand}, {piles}) = {place_hands(hand, piles)}")

    # two Kings
    hand = "KH KC"
    piles = "6C 7S 6H 9H"
    print(f"place_hands({hand}, {piles}) = {place_hands(hand, piles)}")

    # given test case
    hand = "JC 5C 7D QD KC 8S KS"
    piles = "6C 7S 6H 9H"
    print(f"place_hands({hand}, {piles}) = {place_hands(hand, piles)}")


# test_card_check()
test_full()
