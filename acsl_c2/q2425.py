debug = False


def matched(l1: list, l2: list) -> bool:
    if len(l1) != 3:
        return False
    if len(l2) != 3:
        return False
    matches = (l1[0] == l2[0]) + (l1[1] == l2[1]) + (l1[2] == l2[2])
    return matches == 2


def process(start_card: str, cardlist: str) -> str:
    sc = list(start_card)
    cl = cardlist.split(" ")  # list of strings
    found = True
    output = [start_card]
    while found:
        found = False
        next_cl = []
        if debug:
            print(f"Top {sc} against {cl}")
        for i in range(len(cl)):
            string_card = cl[i]
            # from left
            if debug:
                print(f"To match {sc} & {string_card}")
            card = list(string_card)
            if matched(sc, card):
                if debug:
                    print(f"{sc} matched {card}")
                found = True
                output.append("".join(card))
                sc = card
                # add the remaining cards after this one
                i = i + 1
                while i < len(cl):
                    next_cl.append(cl[i])
                    i = i + 1
                break  # start again
            else:
                next_cl.append(string_card)
        cl = next_cl
    return " ".join(output)


card = "B3O"
hand = "R3X B1T B2T R1X B3X B1X Y4O"
res = process(card, hand)
print(f"result = {res}")

card = "R4S"
hand = "R4X B4X B3X B3T G3T G1T R1O"
res = process(card, hand)
print(f"result = {res}")

card = "B1T"
hand = "G1O B1O R1T B4T G4O R4O R1X"
res = process(card, hand)
print(f"result = {res}")

card = "G3S"
hand = "R3S G1O B4X G2S Y4S G3T G3X"
res = process(card, hand)
print(f"result = {res}")

card = "Y4O"
hand = "Y1S G4S B4S G2S R1T G2X Y2T"
res = process(card, hand)
print(f"result = {res}")
