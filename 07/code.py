## PART 1

with open('data.txt') as f:
    lines = [line.strip() for line in f]

# Will just create dirs as we cd into them
# Use 'files' to store files (assumes no directory named 'files')
root = dict()
root['files'] = dict()

def build(curr):
    while lines:
        command = lines.pop(0)
        if command.startswith('$ cd'):
            directory = command[5:]
            if directory == '..':
                return
            if directory not in curr:
                curr[directory] = dict()
                curr[directory]['files'] = dict()
            build(curr[directory])
        elif command.startswith('$ ls'):
            while lines and lines[0][0] != '$':
                size, filename = lines.pop(0).split(' ')
                if size == 'dir':
                    continue
                curr['files'][filename] = int(size)
    return

build(root)


def sum_of_large_dirs(curr):
    """
    Returns (running_total, size_of_dir)
    """
    total = 0
    size = 0
    for k, v in curr.items():
        if k == 'files':
            size += sum(v.values())
        else:
            child_total, child_size = sum_of_large_dirs(v)
            total += child_total
            size += child_size
    if size <= 100000:
        total += size
    return (total, size)

total, size = sum_of_large_dirs(root)
print(total)


## PART 2

min_size = size - 40000000

def smallest_above_threshold(curr, threshold):
    """
    Returns (smallest, size)
    """
    smallest = 10**13 # Large number
    size = 0
    for k, v in curr.items():
        if k == 'files':
            size += sum(v.values())
        else:
            child_smallest, child_size = smallest_above_threshold(v, threshold)
            smallest = min(smallest,  child_smallest)
            size += child_size
    if size >= threshold:
        smallest = min(smallest, size)
    return (smallest, size)

smallest, size = smallest_above_threshold(root, min_size)
print(smallest)
