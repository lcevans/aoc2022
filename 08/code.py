## PART 1

with open('data.txt') as f:
    grid = [[int(c) for c in line.strip()] for line in f]

HEIGHT = len(grid)
WIDTH = len(grid[0])

visibility = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Horizontal viz
for i in range(HEIGHT):
    largest = -1
    for j in range(WIDTH):
        if grid[i][j] > largest:
            largest = grid[i][j]
            visibility[i][j] = 1
    largest = -1
    for j in reversed(range(WIDTH)):
        if grid[i][j] > largest:
            largest = grid[i][j]
            visibility[i][j] = 1

# Vertical viz
for j in range(WIDTH):
    largest = -1
    for i in range(HEIGHT):
        if grid[i][j] > largest:
            largest = grid[i][j]
            visibility[i][j] = 1
    largest = -1
    for i in reversed(range(HEIGHT)):
        if grid[i][j] > largest:
            largest = grid[i][j]
            visibility[i][j] = 1

print(sum(sum(row) for row in visibility))

## PART 2

# Brute force
def viewing_dist(i, j, direction):
    tree_height = grid[i][j]
    di, dj = direction
    count = 0
    while True:
        i += di
        j += dj
        if not ( 0 <= i < HEIGHT and 0 <= j < WIDTH):
            break
        count += 1
        if tree_height <= grid[i][j]:
            break
    return count

from functools import reduce
def prod(lst):
    return reduce(lambda x, y: x * y, lst)

print(max(prod(viewing_dist(i, j, d) for d in [(0,1),(1,0),(0,-1),(-1,0)]) for i in range(HEIGHT) for j in range(WIDTH)))
