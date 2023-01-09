with open("input.txt", "r") as file: line = file.readline().strip(); floor = 0; basement = None
for count, char in enumerate(line, start=1):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    if not basement and floor < 0:
        basement = count
print(floor, basement)