"""
Given a 2D matrix containing all positive and distinct integers in the rankge
[1, N^2] compute the longest path containing consecutive integers in this
matrix.
"""

from collections import deque


def longestPath(grid):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    lp = [[0] * cols for _ in range(rows)]
    # order to explore in
    edq = deque()
    # order to calc in
    cdq = deque()
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    maxlp = 0
    for r in range(rows):
        for c in range(cols):
            if lp[r][c] > 0:
                continue
            edq.append((r, c))
            while edq:
                (er, ec) = edq[0]
                edq.popleft()
                cdq.append((er, ec))
                for d in dirs:
                    nr, nc = er + d[0], ec + d[1]
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if (grid[nr][nc] == grid[er][ec] + 1) and (lp[nr][nc] == 0):
                        lp[nr][nc] = 1
                        edq.append((nr, nc))
            while cdq:
                (er, ec) = cdq[-1]  # last in first out : stack
                lp[er][ec] = 1
                cdq.pop()
                for d in dirs:
                    nr, nc = er + d[0], ec + d[1]
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == grid[er][ec] + 1:
                        lp[er][ec] = max(lp[er][ec], 1 + lp[nr][nc])
                print(
                    f"With grid value {grid[er][ec]}, lp[{er}][{ec}] = {lp[er][ec]}"
                )
            maxlp = max(maxlp, lp[r][c])
    return maxlp


grid = [[1, 2, 3], [4, 9, 5], [8, 7, 6]]
pathlen = longestPath(grid)
expected = 4
print(f"{expected} vs {pathlen}")
