with open('data.txt') as f:
    grid = [list(line.strip()) for line in f]

## PART 1

# Find Start and End
start = None
end = None
for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char == 'S':
            start = (i, j)
        if char == 'E':
            end = (i, j)

HEIGHT = len(grid)
WIDTH = len(grid[0])

def elevation(char):
    if char == 'S':
        return ord('a')
    elif char == 'E':
        return ord('z')
    else:
        return ord(char)


# Dist to End starting from (i, j)
dists = [[10**4 for _ in range(WIDTH)] for _ in range(HEIGHT)]
dists[end[0]][end[1]] = 0

for _ in range(HEIGHT * WIDTH):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (not ((0 <= i+di < HEIGHT) and (0 <= j+dj < WIDTH)) # Must stay in bounds
                    or elevation(grid[i+di][j+dj]) > elevation(grid[i][j]) + 1): # Too steep
                    continue
                dists[i][j] = min(dists[i][j], 1 + dists[i+di][j+dj])

si, sj = start
print(dists[si][sj])


## PART 2
print(min(dists[i][j] for i in range(HEIGHT) for j in range(WIDTH) if elevation(grid[i][j]) == elevation('a')))
