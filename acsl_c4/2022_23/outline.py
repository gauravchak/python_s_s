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

Sample Input	Sample Output
6
13 21 41 42 44
40C

5
31 21 13 32 11 12
01D

10
81 84 86 87 88 71 73 75 77 32 33 45 47 48 11 13 15 16
89A

8
65 45 55 32 42 54 13 14 41 61 24
05D

4
12 22 21
02D

9
11 14 17 33 44 24 31 35 37 45 41 53 57 62 64 66 71 77
80F

7
15 23 24 32 35 31 45 55 44
65B

6
43 33 44 14 23 41
03D

10
25 71 82 63 54 45 56 75 77 88 21 24 26 27 28 12 13 15 34 35 33 37
29A

8
12 13 16 21 22 31 34 35 36 45 43 41 52 54 56 66 65 64 63 61
27H
"""

from typing import List

debug = False


def make_grid(numrows: int) -> List[List[int]]:
    """returns the list of lists"""
    x = []
    for i in range(0,numrows):
        j = []
        for i in range(0,numrows):
            j.append(0)
        x.append(j)
    return x


def fill_grid(grid: List[List[int]], targets: str):
    """Fill in targets in the given grid"""
    thetargets = targets.split(" ")
    for i in thetargets:
        t = []
        for j in i:
            t.append(j)
        row = grid[int(t[0])]
        row[int(t[1])] = 1
    return 
    


def print_grid(grid):
    print('Grid:')
    for row in grid:
        print(row)


def build_trials(numrows):
    """Return all possible trails where each trial has (row, col, dirn) indicating the starting row and col and then the dirn letter to take"""
    trials = []
    dir_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
    # just 
    for i in range(0,numrows):
        for j in dir_list:
            ya = (0,i,j)
            trials.append(ya)
    for i in range(1,numrows-1):
        for j in dir_list:
            ya = (i, 0, j)
            trials.append(ya)
        for j in dir_list:
            ya = (i, numrows-1, j)
            trials.append(ya)
    for i in range(0,numrows):
        for j in dir_list:
            ya = (numrows-1,i,j)
            trials.append(ya)

    return trials


def get_count(grid, num_rows, row, col, dirn) -> int:
    """Change this function start with row and col and check the count of targets in the direction letter dirn"""
    if dirn == "A":
        count = 0
        while col > 0:
            rty = grid[row][col]
            if rty == 1:
                count = count + 1
            elif rty == 0 and count > 0:
                break
            col = col - 1
    elif dirn == "B":
        count = 0
        while row > 0:
            rty = grid[row][col]
            if rty == 1:
                count = count + 1
            elif rty == 0 and count > 0:
                break
            row = row - 1
    elif dirn == "C":
        count = 0
        while col < num_rows:
            rty = grid[row][col]
            if rty == 1:
                count = count + 1
            elif rty == 0 and count > 0:
                break
            col = col + 1
    elif dirn == "D":
        count = 0
        while row < num_rows:
            rty = grid[row][col]
            if rty == 1:
                count = count + 1
            elif rty == 0 and count > 0:
                break
            row = row + 1
    elif dirn == "E":
        count = 0
        while row > 0 and col > 0:
            rty = grid[row][col]
            if rty == 1:
                count = count + 1
            elif rty == 0 and count > 0:
                break
            row = row - 1
            col = col - 1
    elif dirn == "F":
        count = 0
        while row > 0 and col < num_rows:
            rty = grid[row][col]
            # print(f'row {row} col {col} rty {rty} count {count}')
            if rty == 1:
                count = count + 1
            elif rty == 0 and count > 0:
                break
            row = row - 1
            col = col + 1
    elif dirn == "G":
        count = 0
        while row < num_rows and col < num_rows:
            rty = grid[row][col]
            if rty == 1:
                count = count + 1
            elif rty == 0 and count > 0:
                break
            row = row + 1
            col = col + 1
    elif dirn == "H":
        count = 0
        while row < num_rows and col > 0:
            rty = grid[row][col]
            if rty == 1:
                count = count + 1
            elif rty == 0 and count > 0:
                break
            row = row + 1
            col = col - 1
    return count


def arrow(numrows: str, targets: str) -> str:
    num_rows = int(numrows)
    grid = make_grid(num_rows)
    fill_grid(grid, targets)
    if debug:
        print_grid(grid)
    trials = build_trials(num_rows)  # 22 * 8 tuples
    if debug:
        print(trials)
    maxcount = 0
    maxtrial = ""
    for trial in trials:
        row, col, dirn = trial
        count = get_count(grid, num_rows, row, col, dirn)
        if debug:
            print(f"getcount ({row}, {col}, {dirn}) --> {count}")
        trial = str(row) + str(col) + dirn
        if maxcount < count:
            maxcount = count
            maxtrial = trial
        elif maxcount == count:            
            if trial < maxtrial:
                # that mean trail is a alphabetiicaly smaller string than
                # maxtrial. Hence make this maxtrial.
                maxtrial = trial

    return maxtrial


test_cases = [
    {"numrows": "6", "targets": "13 21 41 42 44", "expected": "40C"},
    {"numrows": "5", "targets": "31 21 13 32 11 12", "expected": "01D"},
    {
        "numrows": "10",
        "targets": "81 84 86 87 88 71 73 75 77 32 33 45 47 48 11 13 15 16",
        "expected": "89A",
    },
    {
        "numrows": "8",
        "targets": "65 45 55 32 42 54 13 14 41 61 24",
        "expected": "05D",
    },
    {"numrows": "4", "targets": "12 22 21", "expected": "02D"},
    {
        "numrows": "9",
        "targets": "11 14 17 33 44 24 31 35 37 45 41 53 57 62 64 66 71 77",
        "expected": "80F",
    },
    {
        "numrows": "7",
        "targets": "15 23 24 32 35 31 45 55 44",
        "expected": "65B",
    },
    {"numrows": "6", "targets": "43 33 44 14 23 41", "expected": "03D"},
    {
        "numrows": "10",
        "targets": "25 71 82 63 54 45 56 75 77 88 21 24 26 27 28 12 13 15 34 35 33 37",
        "expected": "29A",
    },
    {
        "numrows": "8",
        "targets": "12 13 16 21 22 31 34 35 36 45 43 41 52 54 56 66 65 64 63 61",
        "expected": "27H",
    },
]

for test_case in test_cases:
    retval = arrow(numrows=test_case["numrows"], targets=test_case["targets"])
    assert (
        retval == test_case["expected"]
    ), f"returned {retval} not {test_case["expected"]}"
