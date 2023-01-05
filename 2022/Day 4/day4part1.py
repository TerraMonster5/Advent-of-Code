with open("input.txt","r") as file: lines = [[list(map(int,sections.split("-"))) for sections in [elf for elf in line.strip().split(",")]] for line in file]
subsetList = [set(range(x[0][0],x[0][1]+1)).issubset(range(x[1][0],x[1][1]+1)) or set(range(x[1][0],x[1][1]+1)).issubset(range(x[0][0],x[0][1]+1)) for x in lines]
print(subsetList.count(True))