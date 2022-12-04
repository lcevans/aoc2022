# PART 1

def clean(line):
    return [int(num) for rng in line.split('-') for num in rng.split(',')]

with open('data.txt') as f:
    assignments = [clean(line.strip()) for line in f]

def contained(assignment): # Is one contained entirely in the other
    start1, end1, start2, end2 = assignment
    sections1 = set(range(start1, end1+1))
    sections2 = set(range(start2, end2+1))
    intersection = (sections1 & sections2)
    return ((intersection == sections1) or (intersection == sections2))

print(sum(int(contained(assignment)) for assignment in assignments))


# PART 2

def overlap(assignment):
    start1, end1, start2, end2 = assignment
    sections1 = set(range(start1, end1+1))
    sections2 = set(range(start2, end2+1))
    return bool(sections1 & sections2)

print(sum(int(overlap(assignment)) for assignment in assignments))
