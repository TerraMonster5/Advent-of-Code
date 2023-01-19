with open("input.txt","r") as file: moves = file.readline().strip().split(", "); coords = [0, 0]; dir = 0
for move in moves:
    if move[0] == "R":
        dir += 1
    elif move[0] == "L":
        dir += 3
    for block in range(int(move[1])):
        match dir % 4:
            case 0: coords[1] += 1
            case 1: coords[0] += 1
            case 2: coords[1] -= 1
            case 3: coords[0] -= 1