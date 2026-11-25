import os

def checkaround (grid,row,col):
    around = []
    if grid[row][col] == "0":
        if row != 0:
            around.append(grid[row-1][col])
        if col != 0:
            around.append(grid[row][col-1])
        if row != 3:
            around.append(grid[row+1][col])
        if col != 3:
            around.append(grid[row][col+1])
    print(around)
    return around

def print_grid(grid):
    print("Grid:")
    for row in grid:
        print(row)


def make_and_fill_grid(n, numbers):
    m = numbers.split()
    n = []
    for i in m:
        n.append(int(i))
    r1 = [n[0],n[1],n[2],n[3]]
    r2 = [n[4],n[5],n[6],n[7]]
    r3 = [n[8],n[9],n[10],n[11]]
    r4 = [n[12],n[13],n[14],n[15]]
    grid = [r1,r2,r3,r4]
    missing = []
    for i in range (1,17):
        if str(i) not in n:
            missing.append(i)
    while len(missing) != 0:
        for row in range(0,len(grid)):
            for col in range(0,len(grid[row])):
                r = grid[row]
                if r[col] == "0":
                    around = checkaround(grid,row,col)
        break
    return grid


def fillPuzzle(n, numbers):
    grid = make_and_fill_grid(n, numbers)
    print_grid(grid)
    # Write your code here
    return ""


if __name__ == "__main__":
    n = 4

    # First get this numbers to work
    numbers = "1 4 5 0 0 3 8 7 11 10 0 16 0 13 14 15"
    # Then this is the harder case where you will need to
    # solve one empty at a time.
    # numbers = "1 0 5 0 0 3 0 7 0 10 0 16 0 0 14 0"

    result = fillPuzzle(n, numbers)

    print(result)
