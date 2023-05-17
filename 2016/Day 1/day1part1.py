with open("input.txt", "r") as file: directions = file.readline().rstrip().split(", "); facing = 0; loc = [0, 0]
for d in directions:
    if d[0] == "R": facing += 1
    else: facing -= 1
    match facing % 4:
        case 0: loc[1] += int(d[1:])
        case 1: loc[0] += int(d[1:])
        case 2: loc[1] -= int(d[1:])
        case 3: loc[0] -= int(d[1:])
print(sum(map(abs, loc)))