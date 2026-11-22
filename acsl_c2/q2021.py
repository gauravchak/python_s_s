debug = False


def transfer(prev: list, new: list):
    seen_set = set()
    new_prev = []
    what_to_add_to_new = []
    for c in prev:
        if c not in seen_set:
            # first occurrence of character
            what_to_add_to_new.append(c)
            seen_set.add(c)
        else:
            # retain seen characters
            new_prev.append(c)
    if debug:
        print(f"non sorted addition = {what_to_add_to_new}")
    what_to_add_to_new = list(sorted(what_to_add_to_new))
    return new_prev, new + what_to_add_to_new


def process(s: str) -> str:
    s = s.lower()
    ls = list(s)
    inls = [x for x in ls if x.isalpha()]
    newls = []
    while len(inls) > 0:
        inls, newls = transfer(inls, newls)
        if debug:
            print(f"{inls} --> {newls}")
    # remove adjacent letters
    final_ls = []
    prev_char = None
    for c in newls:
        if prev_char is None:
            final_ls.append(c)
        else:
            if c != prev_char:
                final_ls.append(c)
        prev_char = c
    return "".join(final_ls)


input = "A good sorting algorithm."
res = process(input)
print(f"For {input} result is {res}")

input = "Einstein was a genius."
res = process(input)
print(f"For {input} result is {res}")
