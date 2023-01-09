with open("input.txt", "r") as file: connections = [line.strip() for line in file]
wires = {connection.split()[-1]: None for connection in connections}