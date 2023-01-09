from structs import Graph

with open("input.txt", "r") as file: paths = [line.strip().split() for line in file]
places = [path[0] for path in paths]