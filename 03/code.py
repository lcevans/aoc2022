# PART 1

def clean(rucksack):
    mid = len(rucksack) // 2
    return (rucksack[:mid], rucksack[mid:])

with open('data.txt') as f:
    rucksacks = [clean(line.strip()) for line in f]

def priority(c):
    if c.isupper():
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1

print(sum(priority(c) for first, second in rucksacks for c in (set(first) & set(second))))

# PART 2

with open('data.txt') as f:
    rucksacks = [line.strip() for line in f]

triples = zip(rucksacks[0::3], rucksacks[1::3], rucksacks[2::3])

print(sum(priority(c) for x,y,z in triples for c in (set(x) & set(y) & set(z))))
