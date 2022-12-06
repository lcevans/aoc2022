## PART 1

with open('data.txt') as f:
    signal = f.read()

for i in range(4, len(signal)):
    chars = signal[i-4:i]
    if len(set(chars)) == 4:
        print(i)
        break

## PART 2

for i in range(14, len(signal)):
    chars = signal[i-14:i]
    if len(set(chars)) == 14:
        print(i)
        break
