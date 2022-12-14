def clean(line):
    line = line.strip()
    letter, number = line.split(' ')
    return (letter, int(number))

with open('data.txt') as f:
    instructions = [clean(line) for line in f]


    
def head_move(direction):
    global position
    head = positions[0]
    if direction == 'U':
        head[1] += 1
    if direction == 'D':
        head[1] -= 1
    if direction == 'R':
        head[0] += 1
    if direction == 'L':
        head[0] -= 1

def rest_move():
    global position
    for idx in range(1, N):
      curr = positions[idx]
      prev = positions[idx-1]
      if abs(prev[0] - curr[0]) <= 1 and abs(prev[1] - curr[1]) <= 1:
          continue
      if curr[0] != prev[0]:
          curr[0] += int((prev[0] - curr[0]) / abs(prev[0] - curr[0]))
      if curr[1] != prev[1]:
          curr[1] += int((prev[1] - curr[1]) / abs(prev[1] - curr[1]))


## PART 1
          
N = 2
          
positions = [[0, 0] for _ in range(N)]
visited = {(0, 0)}
for direction, times in instructions:
    for _ in range(times):
        head_move(direction)
        rest_move()
        visited.add((positions[N-1][0], positions[N-1][1]))

print(len(visited))


## PART 2
          
N = 10
          
positions = [[0, 0] for _ in range(N)]
visited = {(0, 0)}
for direction, times in instructions:
    for _ in range(times):
        head_move(direction)
        rest_move()
        visited.add((positions[N-1][0], positions[N-1][1]))

print(len(visited))
