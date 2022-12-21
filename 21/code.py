with open('data.txt') as f:
    monkey2rule = dict()
    for line in f:
        line = line.strip()
        monkey, rule = line.split(': ')
        if rule.isdigit():
            rule = ('d', int(rule))
        else:
            monkey1, op, monkey2 = rule.split(' ')
            rule = (op, monkey1, monkey2)
        monkey2rule[monkey] = rule


def process(monkey):
    rule = monkey2rule[monkey]
    if rule[0] == 'd':
        return rule[1]
    op, m1, m2 = rule
    if op == '+':
        return process(m1) + process(m2)
    elif op == '-':
        return process(m1) - process(m2)
    elif op == '*':
        return process(m1) * process(m2)
    elif op == '/':
        return process(m1) / process(m2)

print(int(process('root')))


# PART 2
old_root = monkey2rule['root']
monkey2rule['root'] = ('=', old_root[1], old_root[2])

import numpy as np
def process(monkey):
    if monkey == 'humn':
        return np.poly1d([1, 0]) # polynomial is 'x'

    rule = monkey2rule[monkey]
    if rule[0] == 'd':
        return np.poly1d([rule[1]])
    op, m1, m2 = rule
    if op == '+':
        return process(m1) + process(m2)
    elif op == '-':
        return process(m1) - process(m2)
    elif op == '*':
        return process(m1) * process(m2)
    elif op == '/': # poly1d division was wonky => I do it manually
        p1 = process(m1)
        p2 = process(m2)
        assert(p2.order == 0) # Thankfully this is true so no fractions of polynomials
        ret = np.poly1d(np.array(p1) / p2[0])
        return ret
    elif op == '=':
        diff = process(m1) - process(m2)
        return diff.r[0] # only one root
print(int(process('root')))
