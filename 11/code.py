# Hardcoding the monkeys since only 8

def get_monkeys():
    return [
        {
            'items': [92, 73, 86, 83, 65, 51, 55, 93],
            'operation': (lambda x: x*5),
            'test': (lambda x: x % 11 == 0),
            True: 3,
            False: 4,
            'inspections': 0,
        },
        {
            'items': [99, 67, 62, 61, 59, 98],
            'operation': (lambda x: x*x),
            'test': (lambda x: x % 2 == 0),
            True: 6,
            False: 7,
            'inspections': 0,
        },
        {
            'items': [81, 89, 56, 61, 99],
            'operation': (lambda x: x*7),
            'test': (lambda x: x % 5 == 0),
            True: 1,
            False: 5,
            'inspections': 0,
        },
        {
            'items': [97, 74, 68],
            'operation': (lambda x: x+1),
            'test': (lambda x: x % 17 == 0),
            True: 2,
            False: 5,
            'inspections': 0,
        },
        {
            'items': [78, 73],
            'operation': (lambda x: x+3),
            'test': (lambda x: x % 19 == 0),
            True: 2,
            False: 3,
            'inspections': 0,
        },
        {
            'items': [50],
            'operation': (lambda x: x+5),
            'test': (lambda x: x % 7 == 0),
            True: 1,
            False: 6,
            'inspections': 0,
        },
        {
            'items': [95, 88, 53, 75],
            'operation': (lambda x: x+8),
            'test': (lambda x: x % 3 == 0),
            True: 0,
            False: 7,
            'inspections': 0,
        },
        {
            'items': [50, 77, 98, 85, 94, 56, 89],
            'operation': (lambda x: x+2),
            'test': (lambda x: x % 13 == 0),
            True: 4,
            False: 0,
            'inspections': 0,
        },
    ]

## PART 1

MONKEYS = get_monkeys()
for _ in range(20):
    for monkey in MONKEYS:
        while monkey['items']:
            monkey['inspections'] += 1
            item = monkey['items'].pop(0)
            item = monkey['operation'](item)
            item = item // 3
            cond = monkey['test'](item)
            MONKEYS[monkey[cond]]['items'].append(item)

activity = [monkey['inspections'] for monkey in MONKEYS]
x, y = list(sorted(activity))[-2:]
print(x * y)


## PART 2

MONKEYS = get_monkeys()
product_of_primes = 11 * 2 * 5 * 17 * 19 * 7 * 3 * 13 # Distinct primes in the tests
for _ in range(10000):
    for monkey in MONKEYS:
        while monkey['items']:
            monkey['inspections'] += 1
            item = monkey['items'].pop(0)
            item = monkey['operation'](item)
            item = item % product_of_primes
            cond = monkey['test'](item)
            MONKEYS[monkey[cond]]['items'].append(item)

activity = [monkey['inspections'] for monkey in MONKEYS]
x, y = list(sorted(activity))[-2:]
print(x * y)
