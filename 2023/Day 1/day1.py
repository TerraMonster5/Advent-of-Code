with open("input.txt", "r") as file: print(sum([int([x for x in line.rstrip() if x.isdigit()][0]+[x for x in line.rstrip() if x.isdigit()][-1]) for line in file]))