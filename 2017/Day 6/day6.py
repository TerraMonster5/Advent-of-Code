with open("input.txt","r") as file: banks = list(map(int, file.readline().strip().split()))

# Part 1
previous = [banks.copy()]
cycles = 0
while True:
    cycles += 1
    pntr = banks.index(max(banks))
    size = banks[pntr]
    banks[pntr] = 0
    for x in range(size):
        banks[(pntr + x + 1) % len(banks)] += 1
    if banks in previous:
        break
    else:
        previous.append(banks.copy())
print(cycles)

# Part 2
cycles = 0
loop = banks.copy()
while True:
    cycles += 1
    pntr = banks.index(max(banks))
    size = banks[pntr]
    banks[pntr] = 0
    for x in range(size):
        banks[(pntr + x + 1) % len(banks)] += 1
    if banks == loop:
        break
print(cycles)