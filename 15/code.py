import re

# PART 1

with open('data.txt') as f:
    inputs = [[int(num) for num in re.findall('-?\d+', line.strip())] for line in f]

Y = 2000000

no_beacon = set()
for sx, sy, bx, by in inputs:
    dist = abs(sx-bx) + abs(sy-by)
    remaining = dist - abs(sy - Y)
    for x in range(sx-remaining, sx+remaining + 1):
        if not (bx == x and by == Y):
            no_beacon.add(x)

print(len(no_beacon))


# PART 2

with open('data.txt') as f:
    inputs = [[int(num) for num in re.findall('-?\d+', line.strip())] for line in f]

MAX = 4000000

SENSOR_DIST = [(sx, sy, abs(sx-bx)+abs(sy-by)) for sx, sy, bx, by in inputs]

def undetected(x, y):
    return all(abs(x-sx) + abs(y-sy) > dist for sx, sy, dist in SENSOR_DIST)

# Since there is only one possible spot it must be on dist+1 perimiter of a sensor
def perimiter(sx, sy, dist):
    for dx in range(-dist, dist+1):
        dy = dist - abs(dx)
        yield (sx+dx, sy+dy)
        yield (sx+dx, sy-dy)

for sx, sy, dist in SENSOR_DIST:
    for x, y in perimiter(sx, sy, dist+1):
        if 0<=x<=MAX and 0<=y<=MAX and undetected(x, y):
            print(4000000*x + y)
            assert False # Hack to break out of nested loop
