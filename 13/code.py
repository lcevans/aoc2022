def clean(input_str):
    first, second = input_str.strip().split('\n')
    return (eval(first), eval(second))
    
with open('data.txt') as f:
    inputs = [clean(input_str) for input_str in f.read().split('\n\n')]

## PART 1
    
def compare(left, right):
    # Return -1, 0, 1  for left should be before right, same, right should be before left
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) == 0:
            return 0
        elif len(left) == 0 and len(right) > 0:
            return -1
        elif len(left) > 0 and len(right) == 0:
            return 1
        else:
            sub =  compare(left[0], right[0])
            if sub != 0:
                return sub
            else:
                return compare(left[1:], right[1:])
    else: # One is a list, the other is an integer
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]
        return compare(left, right)


print(sum(i+1 for i, pair in enumerate(inputs) if compare(*pair) in [-1, 0]))

## PART 2

divider1 = [[2]]
divider2 = [[6]]
packets = [packet for input in inputs for packet in input] + [divider1] + [divider2]

import functools
packets.sort(key=functools.cmp_to_key(compare))

print((packets.index(divider1) + 1) * (packets.index(divider2) + 1))
