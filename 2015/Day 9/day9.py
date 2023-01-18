from itertools import permutations

with open("input.txt", "r") as file: lines = [line.strip().split() for line in file]
refTable = {(path[0], path[2]): int(path[-1]) for path in lines} | {(path[2], path[0]): int(path[-1]) for path in lines}

def calcDist(route: list) -> int:
    total = 0
    for index in range(0,len(route)-1):
        total += refTable[(route[index], route[index+1])]
    return total

routes = list(map(list, permutations(list(dict.fromkeys(path[0] for path in lines))+[lines[-1][2]])))
distances = list(map(calcDist, routes))

print(min(distances), max(distances))