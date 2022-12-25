from collections import defaultdict

elf2next = dict()
with open('data.txt') as f:
    for i, line in enumerate(f.read().split('\n')):
        for j, c in enumerate(line):
            if c == '#':
                elf2next[(i,j)] = None


## PART 1

DIRECTIONS = [
    [(-1, -1), (-1, 0), (-1, 1)], # North
    [(1, -1), (1, 0), (1, 1)],    # South
    [(-1, -1), (0, -1), (1, -1)], # West
    [(-1, 1), (0, 1), (1, 1)],    # East
]
start_dir = 0

def pair_sum(pair1, pair2):
    i1, j1 = pair1
    i2, j2 = pair2
    return (i1+i2, j1+j2)

def print_grid():
    print('')
    min_i = min(i for i, j in elf2next.keys())
    min_j = min(j for i, j in elf2next.keys())
    max_i = max(i for i, j in elf2next.keys())
    max_j = max(j for i, j in elf2next.keys())

    HEIGHT = (max_i + 1 - min_i)
    WIDTH = (max_j + 1 - min_j)
    grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for elf in elf2next.keys():
        i, j = elf
        grid[i-min_i][j-min_j] = '#'
    for row in grid:
        print(''.join(row))


for _ in range(10):
    # Propose direction
    location_count = defaultdict(int)
    for elf in elf2next.keys():
        if all(pair_sum(elf, delta) not in elf2next  for cluster in DIRECTIONS for delta in cluster):
            elf2next[elf] = elf
            continue
        d = start_dir
        for _ in range(4):
            if all(pair_sum(elf, delta) not in elf2next for delta in DIRECTIONS[d]):
                elf2next[elf] = pair_sum(elf, DIRECTIONS[d][1])
                location_count[pair_sum(elf, DIRECTIONS[d][1])] += 1
                break
            d = (d + 1) % 4
        else:
            elf2next[elf] = elf # All ways blocked

    # Move
    elf2next = {(next if location_count[next] < 2 else elf) : None for elf, next in elf2next.items()}
    start_dir = (start_dir+1) % 4


min_i = min(i for i, j in elf2next.keys())
min_j = min(j for i, j in elf2next.keys())
max_i = max(i for i, j in elf2next.keys())
max_j = max(j for i, j in elf2next.keys())
print((max_i + 1 - min_i) * (max_j + 1 - min_j) - len(elf2next.keys()))



## PART 2

elf2next = dict()
with open('data.txt') as f:
    for i, line in enumerate(f.read().split('\n')):
        for j, c in enumerate(line):
            if c == '#':
                elf2next[(i,j)] = None

start_dir = 0
round = 0
while True:
    round += 1
    # Propose direction
    location_count = defaultdict(int)
    for elf in elf2next.keys():
        if all(pair_sum(elf, delta) not in elf2next  for cluster in DIRECTIONS for delta in cluster):
            elf2next[elf] = elf
            continue
        d = start_dir
        for _ in range(4):
            if all(pair_sum(elf, delta) not in elf2next for delta in DIRECTIONS[d]):
                elf2next[elf] = pair_sum(elf, DIRECTIONS[d][1])
                location_count[pair_sum(elf, DIRECTIONS[d][1])] += 1
                break
            d = (d + 1) % 4
        else:
            elf2next[elf] = elf # All ways blocked

    # Check for no-move
    if all((next == elf) or location_count[next] >= 2  for elf, next in elf2next.items()):
        break

    # Move
    elf2next = {(next if location_count[next] < 2 else elf) : None for elf, next in elf2next.items()}
    start_dir = (start_dir+1) % 4

print(round)
