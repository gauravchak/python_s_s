from typing import List

EMPTYCHAR = ""

def placelet(ch,tree,pos):
    if len(tree) < pos+1:
        ad = pos + 1 - len(tree)
        for i in range(ad):
            tree.append(EMPTYCHAR)
    if tree[pos] == EMPTYCHAR:
        tree[pos] = ch
    elif ch <= tree[pos]:
        x = 2 * pos + 1
        placelet(ch,tree,x)
    elif ch > tree[pos]:
        x = 2 * pos + 2
        placelet(ch,tree,x)
        

def maketree(word:str) -> List[str]:
    letters = []
    for ch in word:
        placelet(ch, letters, 0)
    return(letters)

def countspaces(tree:List[str]) -> List[int]:
    thing = []
    last = 0
    for i in range(1, len(tree)):
        if tree[i] != EMPTYCHAR:
            count = i - last - 1
            last = i
            thing.append(count)
    return thing

def count(word:str) -> List[int]:
    tree = maketree(word)
    return countspaces(tree)


def test_maketree():
    word = "ABC"
    expected = ["A", EMPTYCHAR, "B", EMPTYCHAR, EMPTYCHAR, EMPTYCHAR, "C"]
    tree = maketree(word)
    assert expected == tree, f"expected = {expected} got {tree}"

    word = "CBA"
    expected = ["C", "B", EMPTYCHAR, "A"]
    tree = maketree(word)
    assert expected == tree, f"expected = {expected} got {tree}"

    word = "GASTON"
    expected = [
        "G",
        "A",
        "S",
        EMPTYCHAR,
        EMPTYCHAR,
        "O",
        "T",
        EMPTYCHAR,
        EMPTYCHAR,
        EMPTYCHAR,
        EMPTYCHAR,
        "N",
    ]
    tree = maketree(word)
    assert expected == tree, f"expected = {expected} got {tree}"


def test_count():
    word = "ABC"
    expected = [1, 3]  # ["A", EMPTYCHAR, "B", EMPTYCHAR, EMPTYCHAR, EMPTYCHAR, "C"]
    counts = count(word)
    assert expected == counts, f"expected = {expected} got {counts}"
    word = "CBA"
    expected = [0, 1]
    counts = count(word)
    assert expected == counts, f"expected = {expected} got {counts}"
    word = "GASTON"
    expected = [0, 0, 2, 0, 4]
    counts = count(word)
    assert expected == counts, f"expected = {expected} got {counts}"


# test_maketree()
test_count()
