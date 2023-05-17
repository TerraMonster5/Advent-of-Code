with open("input.txt", "r") as file: directions = file.readline().rstrip().split(", "); facing = 0; loc = [0, 0]; prev = []; found = False
for d in directions:
    if found:
        break
    if d[0] == "R": facing += 1
    else: facing -= 1
    match facing % 4:
        case 0:
            for x in range(int(d[1:])):
                loc[1] += 1
                if loc in prev:
                    found = True
                    break
                prev.append(loc.copy())
        case 1:
            for x in range(int(d[1:])):
                loc[0] += 1
                if loc in prev:
                    found = True
                    break
                prev.append(loc.copy())
        case 2:
            for x in range(int(d[1:])):
                loc[1] -= 1
                if loc in prev:
                    found = True
                    break
                prev.append(loc.copy())
        case 3:
            for x in range(int(d[1:])):
                loc[0] -= 1
                if loc in prev:
                    found = True
                    break
                prev.append(loc.copy())
print(sum(map(abs, loc)))