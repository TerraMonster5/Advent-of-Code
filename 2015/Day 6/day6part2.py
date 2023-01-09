with open("input.txt", "r") as file: instructions = [line.strip().split() for line in file]

def formatRaw(instruction: list) -> list:
    if "turn" in instruction: instruction.remove("turn")
    instruction.remove("through")
    instruction[1], instruction[2] = list(map(int, instruction[1].split(","))), list(map(int, instruction[2].split(",")))
    return instruction

raw = list(map(formatRaw, instructions))
lights = [[0 for x in range(1000)] for x in range(1000)]

def lightControl(rawInstruction: list) -> None:
    global lights
    for x in range(rawInstruction[1][0], rawInstruction[2][0]+1):
        for y in range(rawInstruction[1][1], rawInstruction[2][1]+1):
            match rawInstruction[0]:
                case "toggle":
                    lights[x][y] += 2
                case "on":
                    lights[x][y] += 1
                case "off":
                    if lights[x][y] > 0:
                        lights[x][y] -= 1

for command in raw:
    lightControl(command)

total = 0
for row in lights:
    total += sum(row)

print(total)