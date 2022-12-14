def clean(line):
    line = line.strip()
    if line == 'noop':
        return ('noop', None)
    else:
        cmd, num = line.split(' ')
        return (cmd, int(num))

with open('data.txt') as f:
    instructions = [clean(line) for line in f]


## PART 1

X = 1
cmd, num = instructions.pop(0)
wait = 1 if cmd == 'noop' else 2
total = 0
for cycle in range(1, 221):
    if (cycle - 20) % 40 == 0:
        total += cycle * X

    wait -= 1
    if wait > 0:
        continue
    
    # Execute and fetch new instruction
    if cmd == 'addx':
        X += num
    cmd, num = instructions.pop(0)
    wait = 1 if cmd == 'noop' else 2
    
print(total)    
    

## PART 2

with open('data.txt') as f:
    instructions = [clean(line) for line in f]

# Going to use 0-indexing...
screen = [None for _ in range(240)]
    
X = 1
cmd, num = instructions.pop(0)
wait = 1 if cmd == 'noop' else 2
total = 0
for cycle in range(0, 240):
    screen[cycle] = '#' if abs(cycle % 40 - X) <= 1 else '.'

    wait -= 1
    if wait > 0:
        continue
    
    # Execute and fetch new instruction
    if cmd == 'addx':
        X += num
    if not instructions:
        break
    cmd, num = instructions.pop(0)
    wait = 1 if cmd == 'noop' else 2

for j in range(6):
    row = screen[40*j:40*(j+1)]
    print(''.join(row))
    
