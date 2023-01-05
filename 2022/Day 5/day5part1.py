import structs

def move(amount: int, origin: int, target: int) -> None:
    for x in range(amount):
        stacks[target-1].push(stacks[origin-1].pop())

with open("input.txt","r") as file: lines = [line.replace("\n","") for line in file]; CRATE_SIZE = 3

count = 0

for count, line in enumerate(lines):
    if line.startswith(" 1"): break

stacks = [structs.Stack() for x in range(int(lines[count].rstrip()[-1]))]
moves = [line.split() for line in lines[count+2::]]
inputStacks = [[row[i:i+CRATE_SIZE] for i in range(0, len(row), CRATE_SIZE+1)] for row in lines[:count:]][::-1]

[[stacks[index].push(row[index]) for index in range(len(row)) if row[index] != "   "] for row in inputStacks]

for line in moves:
    move(int(line[1]), int(line[3]), int(line[5]))

for stack in stacks:
    print(stack.peek())