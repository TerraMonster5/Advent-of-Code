with open("input.txt", "r") as file: print(sum(map(lambda y: abs(y[0]-y[1]), zip(*map(lambda x: sorted(list(x)), zip(*[list(map(int, line.strip().split())) for line in file]))))))