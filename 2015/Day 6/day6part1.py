with open("input.txt", "r") as file: instructions = [line.strip().split() for line in file]
def formatRaw(instruction: list) -> list:
    if "turn" in instruction: instruction.remove("turn")
    instruction.remove("through")
    instruction[1], instruction[2] = list(map(int, instruction[1].split(","))), list(map(int, instruction[2].split(",")))
    return instruction
raw = list(map(formatRaw, instructions))
lights = [[False for x in range(1000)] for x in range(1000)]
print(raw)