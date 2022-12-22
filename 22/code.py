with open('data.txt') as f:
    map, instructions = f.read().split('\n\n')
    width = max(len(line) for line in map.split('\n'))
    map = [list(line.ljust(width)) for line in map.split('\n')]
    instructions = list(instructions.strip())


## PART 1

HEIGHT = len(map)
WIDTH = len(map[0])

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
facing = 0

# Get start
i = j = 0
while map[i][j] != '.':
    i += 1

while instructions:
    ins = instructions.pop(0)
    while ins.isdigit() and instructions and instructions[0].isdigit():
        ins += instructions.pop(0)
    if ins.isdigit():
        moves = int(ins)
        di, dj = DIRECTIONS[facing]
        for _ in range(moves):
            ni = (i+di) % HEIGHT
            nj = (j+dj) % WIDTH
            while map[ni][nj] == ' ':
                ni = (ni+di) % HEIGHT
                nj = (nj+dj) % WIDTH
            if map[ni][nj] == '.':
                i = ni
                j = nj
    elif ins == 'R':
        facing = (facing+1) % 4
    elif ins == 'L':
        facing = (facing-1) % 4
    else:
        assert(False)

print(1000*(i+1) + 4*(j+1) + facing)
