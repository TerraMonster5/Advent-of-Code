with open("input.txt","r") as file: lines = [[list(map(int,sections.split("-"))) for sections in [elf for elf in line.strip().split(",")]] for line in file]; total = 0
for x in lines:
    range1 = set(range(x[0][0],x[0][1]+1))
    range2 = set(range(x[1][0],x[1][1]+1))
    intersect = range1.intersection(range2)
    if len(intersect) != 0:
        total += 1