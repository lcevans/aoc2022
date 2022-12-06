lines = None
with open('data.txt') as f:
    lines = [line.strip() for line in f]

elves = '*'.join(lines).split('**')
elves = [[int(calories) for calories in x.split('*')] for x in elves]

totals = [sum(elf) for elf in elves]


most_calories = max(totals)
print(most_calories)


print(sum(sorted(totals)[-3:]))
