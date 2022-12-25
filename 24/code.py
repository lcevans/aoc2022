from collections import defaultdict

## PART 1

with open('data.txt') as f:
    map = [[c for c in line.strip()[1:-1]] for line in f]
    map = map[1:-1]

char2dir = {
    '>' : (0, 1),
    '^' : (-1, 0),
    '<' : (0, -1),
    'v' : (1, 0),
}

blizzards = []
for i, row in enumerate(map):
    for j, c in enumerate(row):
        if c != '.':
            blizzards.append((i, j, char2dir[c]))


HEIGHT = len(map)
WIDTH = len(map[0])

def is_empty(i, j, time):
    for bi, bj, dir in blizzards:
        di, dj = dir
        if (bi + time*di) % HEIGHT == i and (bj + time*dj) % WIDTH == j:
            return False
    return True

assert is_empty(0, 0, 1)

import math
LCM = math.lcm(HEIGHT, WIDTH)


def time_when_reach_goal(i, j, goal_i, goal_j, start_time):
    visited = set((i, j, start_time%LCM))
    q = [(i, j, start_time)]
    while q:
        i, j, time = q.pop(0)
        if i == goal_i and j == goal_j:
            return time
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            ni = (i+di)
            nj = (j+dj)
            if (0<=ni<HEIGHT and 0<=nj<WIDTH) and is_empty(ni, nj, time+1) and (ni, nj, (time+1) % LCM) not in visited:
                visited.add((ni, nj, (time+1) % LCM))
                q.append((ni, nj, time+1))
    return None

## PART 1

print(1 + time_when_reach_goal(0, 0, HEIGHT-1, WIDTH-1, 1)) # Extra step to leave maze


## PART 2

time1 = time_when_reach_goal(0, 0, HEIGHT-1, WIDTH-1, 1)
time1 += 2
while True:
    if not is_empty(HEIGHT-1, WIDTH-1, time1):
        time1 += 1
        continue
    time2 = time_when_reach_goal(HEIGHT-1, WIDTH-1, 0, 0, time1)
    if time2:
        break
    time1 += 1

time2 += 2
while True:
    if not is_empty(0, 0, time2):
        time2 += 1
        continue
    time3 = time_when_reach_goal(0, 0, HEIGHT-1, WIDTH-1, time2)
    if time3:
        break
    time2 += 1

print("Answer: ", 1+time3)
