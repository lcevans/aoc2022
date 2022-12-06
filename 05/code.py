## PART 1

import re
stacks = [[] for _ in range(9)]

with open('data.txt') as f:
    diagram, movements = f.read().split('\n\n')

    # Parse diagram to build stacks
    for line in reversed(diagram.split('\n')[:-1]):
        for i in range(9):
            if (len(line) <= 1 + 4*i):
                continue
            c = line[1 + 4*i]
            if c != ' ':
                stacks[i].append(c)

    # Parse movements
    steps = [[int(num) for num in re.findall('\d+', line.strip())] for line in movements.split('\n')]

# Perform steps
for step in steps:
    num, src, dst = step
    for _ in range(num):
        stacks[dst-1].append(stacks[src-1].pop())
        
# Get answer from top of stacks
answer = ''.join(stack.pop() for stack in stacks)
print(answer)


## PART 2

# Reset stacks
stacks = [[] for _ in range(9)]

with open('data.txt') as f:
    diagram, movements = f.read().split('\n\n')

    for line in reversed(diagram.split('\n')[:-1]):
        for i in range(9):
            if (len(line) <= 1 + 4*i):
                continue
            c = line[1 + 4*i]
            if c != ' ':
                stacks[i].append(c)


# This time push all into tmp stack, then push all into dst => moves N as a group in order
for step in steps:
    tmp_stack = []
    num, src, dst = step
    for _ in range(num):
        tmp_stack.append(stacks[src-1].pop())
    for _ in range(num):
        stacks[dst-1].append(tmp_stack.pop())

# Get answer from top of stacks
answer = ''.join(stack.pop() for stack in stacks)
print(answer)
