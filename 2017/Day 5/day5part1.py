with open("input.txt","r") as file: instructions = [int(line.strip()) for line in file]

pos = 0
steps = 0

while True:
    if pos < 0 or pos > len(instructions)-1:
        break

    temp = instructions[pos]
    instructions[pos] += 1
    pos += temp

    steps += 1

print(steps)