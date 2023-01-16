from itertools import permutations

with open("input.txt", "r") as file: lines = [line.strip().split() for line in file]
refTable = {(path[0], path[2]): path[-1] for path in lines} | {(path[2], path[0]): path[-1] for path in lines}

def calcDist(temp: list) -> int:
    return 0

routes = list(permutations(list(dict.fromkeys(path[0] for path in lines))+[lines[-1][2]]))

print(routes)