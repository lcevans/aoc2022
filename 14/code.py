with open('data.txt') as f:
    multi_lines = [[(int(pair.split(',')[0]), int(pair.split(',')[1]))for pair in line.strip().split(' -> ')] for line in f]


def interval(a, b): # inclusive
    lower = min(a, b)
    upper = max(a, b)
    for x in range(lower, upper+1):
        yield x

rocks = set()
for multi_line in multi_lines:
    for start, end in zip(multi_line, multi_line[1:]):
        if start[0] == end[0]: # Vertical
            for x in interval(start[1], end[1]):
                rocks.add((start[0], x))
        if start[1] == end[1]: # Horizontal
            for x in interval(start[0], end[0]):
                rocks.add((x, start[1]))

## PART 1


ABYSS = max(point[1] for multi_line in multi_lines for point in multi_line)

def blocked(i, j):
    return (i, j) in rocks or (i, j) in sand

sand = set()
def drop_sand(i, j):
    if j > ABYSS:
        return False

    if not blocked(i, j+1):
        return drop_sand(i, j+1)
    elif not blocked(i-1, j+1):
        return drop_sand(i-1, j+1)
    elif not blocked(i+1, j+1):
        return drop_sand(i+1, j+1)
    else:
        sand.add((i,j))
        return True

while drop_sand(500, 0):
    pass

print(len(sand))

## PART 2

BOTTOM = max(point[1] for multi_line in multi_lines for point in multi_line) + 2

def blocked(i, j):
    return (i, j) in rocks or (i, j) in sand or j == BOTTOM

def drop_sand(i, j):
    if not blocked(i, j+1):
        return drop_sand(i, j+1)
    elif not blocked(i-1, j+1):
        return drop_sand(i-1, j+1)
    elif not blocked(i+1, j+1):
        return drop_sand(i+1, j+1)
    else:
        sand.add((i,j))
        return False if (i==500 and j==0) else True

sand = set()
while drop_sand(500, 0):
    pass

print(len(sand))
