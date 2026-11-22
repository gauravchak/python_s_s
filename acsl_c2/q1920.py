debug = False


def removechars(s: list) -> list:
    prev_char = None
    out_list = []
    for a in s:
        if prev_char is None:
            prev_char = a
            out_list.append(a)
        else:
            if (a not in ["A", "E", "I", "O", "U"]) and (a != prev_char):
                out_list.append(a)
            prev_char = a
    return out_list


def process(is1: str, is2: str) -> str:
    s1 = list(is1)
    s2 = list(is2)

    # delete second occurrence for both strings and vowels
    s1 = removechars(s1)
    s2 = removechars(s2)
    if debug:
        print(f"After removechars {s1} & {s2}")

    # align left to right and delete all like characters
    ls1 = []
    ls2 = []
    i = 0
    while i < min(len(s1), len(s2)):
        if s1[i] != s2[i]:
            ls1.append(s1[i])
            ls2.append(s2[i])
        i += 1
    if debug:
        print(f"After lskips-part1 {ls1} & {ls2}")
    # Now add the rest for the longer list.
    j = i
    while j < len(s1):
        ls1.append(s1[j])
        j += 1
    j = i
    while j < len(s2):
        ls2.append(s2[j])
        j += 1
    if debug:
        print(f"After lskips-part2 {ls1} & {ls2}")

    # align right to left and delete all like characters
    s1 = []
    s2 = []
    i = 0
    while i < min(len(ls1), len(ls2)):
        if ls1[len(ls1) - 1 - i] != ls2[len(ls2) - 1 - i]:
            s1.append(ls1[len(ls1) - 1 - i])
            s2.append(ls2[len(ls2) - 1 - i])
        i += 1
    if debug:
        print(f"After rskips-part1 {s1} & {s2}")
    # Now add the rest for the longer list.
    j = i
    while j < len(ls1):
        s1.append(ls1[len(ls1) - 1 - j])
        j += 1
    j = i
    while j < len(ls2):
        s2.append(ls2[len(ls2) - 1 - j])
        j += 1
    if debug:
        print(f"After rskips-part2 {s1} & {s2}")
    s1 = list(reversed(s1))
    s2 = list(reversed(s2))

    # return shorter of two strings or first in alphabetical order.
    rs1 = "".join(s1)
    rs2 = "".join(s2)
    if len(rs1) < len(rs2):
        return rs1
    if len(rs2) < len(rs1):
        return rs2
    if rs1 <= rs2:
        return rs1
    return rs2


input1, input2 = "MISSISSIPPI", "MISSOURI"
res = process(input1, input2)
print(f"For {input1}, {input2} result is {res}")

input1, input2 = "CATHERINE", "KATHERYNE"
res = process(input1, input2)
print(f"For {input1}, {input2} result is {res}")

input1, input2 = "CONSTITUTIONAL", "CONVENTIONAL"
res = process(input1, input2)
print(f"For {input1}, {input2} result is {res}")

input1, input2 = "COMPARTMENTALIZATION", "SEMIAUTOBIOGRAPHICAL"
res = process(input1, input2)
print(f"For {input1}, {input2} result is {res}")

input1, input2 = "PHYSICIAN", "PHARMACY"
res = process(input1, input2)
print(f"For {input1}, {input2} result is {res}")

input1, input2 = "MYLOLLIPOPS", "MYLARBALLOONS"
res = process(input1, input2)
print(f"For {input1}, {input2} result is {res}")
