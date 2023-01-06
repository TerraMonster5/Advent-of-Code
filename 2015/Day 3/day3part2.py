with open("input.txt","r") as file: line = file.readline().strip()
houses = {(0, 0) : 1}; currentS = [0, 0]; currentR = [0, 0]
for count, char in enumerate(line):
    if count % 2:
        if char == "^": currentR[0] += 1
        elif char == ">": currentR[1] += 1
        elif char == "v": currentR[0] -= 1
        elif char == "<": currentR[1] -=1

        if tuple(currentR) in houses.keys(): houses[tuple(currentR)] += 1
        else: houses[tuple(currentR)] = 1
    else:
        if char == "^": currentS[0] += 1
        elif char == ">": currentS[1] += 1
        elif char == "v": currentS[0] -= 1
        elif char == "<": currentS[1] -=1

        if tuple(currentS) in houses.keys(): houses[tuple(currentS)] += 1
        else: houses[tuple(currentS)] = 1

print(len(houses))