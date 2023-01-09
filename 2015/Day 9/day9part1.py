from structs import Graph

with open("input.txt", "r") as file: lines = [line.strip().split() for line in file]
refTable = tuple(dict.fromkeys(path[0] for path in lines))
paths: dict = {}
for line in lines:
    if line[2] == "Arbre":
        continue
    elif line[0] in paths.keys():
        paths[line[0]][refTable.index(line[2])] = int(line[-1])
    else:
        paths[line[0]] = {}
        paths[line[0]][refTable.index(line[2])] = int(line[-1])

world = Graph()

for path in paths.values():
    world.vertices.append(world.Vertex(path))