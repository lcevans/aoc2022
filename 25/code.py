with open('data.txt') as f:
    inputs = [line.strip() for line in f]

def snafu2decimal(snafu):
    total = 0
    for c in snafu:
        total *= 5
        dec = -1 if c == '-' else -2 if c == '=' else int(c)
        total += dec
    return total

def decimal2snafu(dec):
    if dec == 0:
        return ''
    snafu = ''
    quot = dec // 5
    rem = dec % 5
    if rem in [3, 4]:
        quot += 1
    print(quot, rem)
    snafu = decimal2snafu(quot) + ('-' if rem == 4 else '=' if rem == 3 else str(rem))
    return snafu


total = sum(snafu2decimal(line) for line in inputs)
print(decimal2snafu(total))
