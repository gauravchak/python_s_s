def arrow(size,targets):
    t = targets.split(" ")
    grid = []
    for i in range(0,int(size)):
        x = []
        for i in range(0,int(size)):
            x.append("E")
        grid.append(x)
    for i in t:
        j = int(i[0])
        a = grid[j]
        a[int(i[1])] = "T"
    print(grid)
    allcounts = []
    locs = []
    for i in range(len(grid[0])):
        y = grid[0]
        j = i
        count = 0
        while j - 1 != -1:
            while y[j] == "T":
                if j - 1 != -1:
                    if y[j-1] == "E":
                        count = count + 1
                    else:
                        j = j - 1
        allcounts.append(count)
        y = "0"+str(j)+"A"
        locs.append(y)
        while j + 1 != 6:
            while y[j] == "T":
                if j + 1 != 6:
                    if y[j+1] == "E":
                        count = count + 1
                    else:
                        j = j + 1
        allcounts.append(count)
        y = "0"+str(j)+"C"
        locs.append(y)
        print(y[i])
        print(j)
    print(allcounts)
    return "thething"

print(arrow("6","13 21 41 42 44"))

"""
PROBLEM: Given an n x n grid with target locations and with empty border cells,
find which arrow when placed in a border cell would hit the most consecutive
targets without passing through any empty cell. The arrow directions are:
(A) ←, (B) ↑, (C) →, (D) ↓, (E) ↖, (F) ↗, (G) ↘, and (H) ↙. Output the location
and the position of the arrow as a 3-character string. The upper left corner is
identified as row=0 and column=0 in row-major order.
EXAMPLE: In the grid below, the size is 6 x 6 with 5 targets.

By checking every border location, there are more targets that can be hit with
a C arrow in location (4,0) than any other, since it hits 2 targets. An F arrow
from that same location would not hit any target without going through an empty
cell first. From location (5,0), an F arrow would hit one target and an H arrow
would be off the grid. Checking elsewhere, a B arrow from location (5,1) would
only hit one target as would an A arrow from location (4,5). The output is 40C.

INPUT: There will be one integer representing the size of the grid and another
string representing the locations of the targets, each separated by a single
space. We guarantee that the grid will be no larger than 10 x 10.

OUTPUT: For each grid, output a 3-character string representing the location
and direction of the arrow that would hit the most targets without encountering
any empty space. In the case of a tie, output the string that comes first in
order by ASCII codes (e.g. “05F” < “50A”).
"""

test_cases = [
    {"numrows": "6", "targets": "13 21 41 42 44", "expected": "40C"},
    # {"numrows": "5", "targets": "31 21 13 32 11 12", "expected": "01D"},
    # {
    #     "numrows": "10",
    #     "targets": "81 84 86 87 88 71 73 75 77 32 33 45 47 48 11 13 15 16",
    #     "expected": "89A",
    # },
    # {"numrows": "4", "targets": "12 22 21", "expected": "02D"},
    # {
    #     "numrows": "9",
    #     "targets": "11 14 17 33 44 24 31 35 37 45 41 53 57 62 64 66 71 77",
    #     "expected": "80F",
    # },
    # {
    #     "numrows": "7",
    #     "targets": "15 23 24 32 35 31 45 55 44",
    #     "expected": "65B",
    # },
    # {
    #     "numrows": "10",
    #     "targets": "25 71 82 63 54 45 56 75 77 88 21 24 26 27 28 12 13 15 34 35 33 37",
    #     "expected": "29A",
    # },
]

for test_case in test_cases:
    retval = arrow(test_case["numrows"], test_case["targets"])
    assert (
        retval == test_case["expected"]
    ), f"returned {retval} not {test_case["expected"]}"
