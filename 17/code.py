with open('data.txt') as f:
    inputs = f.read().strip()

## PART 1

def jets_gen():
    while True:
        for char in inputs:
            if char == '<':
                yield -1
            elif char == '>':
                yield 1

# Lower left is the coordinate
PIECE_OFFSETS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)], # Horizontal Line
    [(1, 0), (0, 1), (1, 1), (1, 2), (2, 1)], # Plus
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], # L
    [(0, 0), (0, 1), (0, 2), (0, 3)], # Vertical Line
    [(0, 0), (1, 0), (0, 1), (1, 1)], # Square
]

highest_height = None
blocked = None
jets = None
def reset():
    global blocked, highest_height, jets
    highest_height = 0
    blocked = set()
    jets = jets_gen()
    for x in range(7):
        blocked.add((x, highest_height)) # Build floor

def get_height(iterations):
    global blocked, highest_height, jets

    def try_move(x, y, offsets, dx, dy):
        new_x = x + dx
        new_y = y + dy
        if any((new_x + ox, new_y + oy) in blocked or not (0 <= new_x + ox < 7) for ox, oy in offsets):
            return (False, x, y)
        else:
            return (True, new_x, new_y)

    for idx in range(iterations):
        offsets = PIECE_OFFSETS[idx % len(PIECE_OFFSETS)]
        x = 2
        y = highest_height + 4
        while True:
            # Push by jet
            dx = next(jets)
            _, x, y = try_move(x, y, offsets, dx, 0)

            # Fall
            succeeded, x, y = try_move(x, y, offsets, 0, -1)
            if not succeeded:
                for ox, oy in offsets:
                    blocked.add((x + ox, y + oy))
                    highest_height = max(highest_height, y + oy)
                break
    return highest_height

reset()
print(get_height(2022))




## PART 2
import math
period = math.lcm(len(inputs), len(PIECE_OFFSETS))

reset()
old = 0
for _ in range(200):
    new = get_height(period)
    print(new - old)
    old = new



num_periods = 1000000000000 // period
remainder = 1000000000000 % period



PATTERN = [
    59, # Extra + 7 the first time
    59,
    59,
    64,
    60,
    61,
    62,
]

height_from_periods = (num_periods // len(PATTERN)) * sum(PATTERN) + sum(PATTERN[:num_periods % len(PATTERN)])

reset()
old = 0
for _ in range(len(PATTERN)):
    new = get_height(period)
    print(new - old)
    old = new
height_from_remainder = get_height(remainder) - old

print(7 + height_from_periods + height_from_remainder)

# TEST:
reset()
old = 0
for i in range(1000):
    new = get_height(period)
    diff = new - old
    old = new
    if i == 0:
        continue
    assert diff == PATTERN[i % len(PATTERN)]
