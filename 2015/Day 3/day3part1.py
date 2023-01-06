with open("input.txt","r") as file: line = file.readline().strip()
houses = {(0, 0) : 1}; current = [0, 0]
for char in line:
    if char == "^": current[0] += 1
    elif char == ">": current[1] += 1
    elif char == "v": current[0] -= 1
    elif char == "<": current[1] -=1

    if tuple(current) in houses.keys(): houses[tuple(current)] += 1
    else: houses[tuple(current)] = 1

print(len(houses))